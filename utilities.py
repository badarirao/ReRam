"""Utilities file with useful classes and functions."""

from datetime import datetime
from os.path import abspath, join, exists
from pyvisa import ResourceManager, VisaIOError
from os import makedirs
from copy import copy
from re import sub
from sys import exit as exitprogram
from MyKeithley2450 import Keithley2450
from MyKeithley2700 import Keithley2700
from MyAFG1022 import AFG1022 
from PyQt5.QtCore import QTimer, QEventLoop
from PyQt5.QtWidgets import QTimeEdit
from math import log10
from numpy import logspace, linspace, diff

SMU = 111
AFG = 112
SAMPLE1 = 101
SAMPLE2 = 102
SAMPLE3 = 103
SAMPLE4 = 104
SAMPLE5 = 105
SAMPLE6 = 106
SAMPLE7 = 107
SAMPLE8 = 108
SAMPLE9 = 109
SAMPLE10 = 110

sample_id = {
                1 : SAMPLE1,
                2 : SAMPLE2,
                3 : SAMPLE3,
                4 : SAMPLE4,
                5 : SAMPLE5,
                6 : SAMPLE6,
                7 : SAMPLE7,
                8 : SAMPLE8,
                9 : SAMPLE9,
                10 : SAMPLE10}

class MyTimeEdit(QTimeEdit):
    def stepBy(self,steps):
        cur = self.time()
        QTimeEdit.stepBy(self,steps)
        if self.currentSection() == self.SecondSection:
            sec = cur.second()
            if sec == 0 and steps < 0:
                self.setTime(cur.addSecs(-1))
            elif sec == 59 and steps > 0:
                self.setTime(cur.addSecs(1))
        elif self.currentSection() == self.MinuteSection:
            minute = cur.minute()
            if minute == 0 and steps < 0:
                self.setTime(cur.addSecs(-60))
            elif minute == 59 and steps > 0:
                self.setTime(cur.addSecs(60))
        

class FakeAdapter():
    """Provides a fake adapter for debugging purposes.

    Bounces back the command so that arbitrary values testing is possible.

    Note: Adopted from Pymeasure package

    .. code-block:: python

        a = FakeAdapter()
        assert a.read() == ""
        a.write("5")
        assert a.read() == "5"
        assert a.read() == ""
        assert a.ask("10") == "10"
        assert a.values("10") == [10]

    """

    _buffer = ""

    def __init__(self):
        self.address = ''

    def read(self):
        """Return last commands given after the last read call."""
        result = copy(self._buffer)
        # Reset the buffer
        self._buffer = ""
        return result

    def write(self, command):
        """Write the command to a buffer, so that it can be read back."""
        self._buffer += command

    def __repr__(self):
        """Return the class name as a string."""
        return "<FakeAdapter>"

    def __getattr__(self,name):  
        """If any undefined method is called, do nothing."""
        def method(*args):
            pass
        return method



def unique_filename(directory, prefix='DATA', suffix='', ext='csv',
                    dated_folder=False, index=True, datetimeformat="%Y-%m-%d"):
    """
    Return a unique filename based on the directory and prefix.

    Note: adopted from Pymeasure Package.
    """
    now = datetime.now()
    directory = abspath(directory)
    if dated_folder:
        directory = join(directory, now.strftime('%Y-%m-%d'))
    if not exists(directory):
        makedirs(directory)
    if index:
        i = 1
        basename = "%s%s" % (prefix, now.strftime(datetimeformat))
        basepath = join(directory, basename)
        filename = "%s_%d%s.%s" % (basepath, i, suffix, ext)
        while exists(filename):
            i += 1
            filename = "%s_%d%s.%s" % (basepath, i, suffix, ext)
    else:
        basename = "%s%s%s.%s" % (
            prefix, now.strftime(datetimeformat), suffix, ext)
        filename = join(directory, basename)
    return filename


def get_valid_filename(s):
    """
    Check if given filename is valid, and correct it if its not.

    Parameters
    ----------
    s : string
        file-name

    Returns
    -------
    string
        Valid file-name

    """
    s = str(s).strip().replace(' ', '_')
    return sub(r'(?u)[^-\w.]', '', s)


def connectDevice(inst,addr,test = False):
    try:
        return inst(addr), 1
    except VisaIOError:
        if test == True:
            return FakeAdapter(), 0
        else:
            # TODO: prompt a gui message instead
            print("Instrument not connected! Check connections!")
            exitprogram()
        
def checkInstrument(k2450Addr = None, k2700Addr = None, AFG1022Addr = None, 
                    test = False):
    """
    Obtain instrument address of K2450, K2700 and function generator.

    Returns: list of instrument objects
    -------
    Instrument objects pointing to K2450, K2700 and AFG1022
    if test is True,
        return FakeAdapter if any instrument is not found
    else exit program
    """
    deviceAddr = [k2450Addr,k2700Addr,AFG1022Addr]
    rm = ResourceManager()
    k2450Status = k2700Status = afgStatus = 0
    if k2450Addr:
        k2450, k2450Status = connectDevice(Keithley2450,k2450Addr,test=True)
    if k2700Addr:
        k2700, k2700Status = connectDevice(Keithley2700,k2700Addr,test=True)
    if AFG1022Addr:
        afg, afgStatus = connectDevice(AFG1022,AFG1022Addr,test=True)
    status = [k2450Status,k2700Status,afgStatus]
    deviceInfo = [['KEITHLEY','2450'],['KEITHLEY','2700'],['TEKTRONIX','AFG1022']]
    notConnected = [x for x,y in enumerate(status) if y == 0]
    if notConnected:
        instList = rm.list_resources()
        for inst in instList:
            for deviceNo in notConnected:
                try:
                    myInst = rm.open_resource(inst)
                    instID = myInst.query('*IDN?').split(',')
                    if deviceInfo[deviceNo][0] in instID[0] and deviceInfo[deviceNo][1] in instID[1]:
                        deviceAddr[deviceNo] = inst
                        notConnected.remove(deviceNo)
                        break
                except VisaIOError:
                    pass
        k2450Addr = deviceAddr[0]
        k2700Addr = deviceAddr[1]
        AFG1022Addr = deviceAddr[2]
        if k2450Status == 0:
                k2450,_ = connectDevice(Keithley2450,k2450Addr,test)
        if k2700Status == 0:
            k2700,_ = connectDevice(Keithley2700,k2700Addr,test)
        if afgStatus == 0:
            afg,_ = connectDevice(AFG1022,AFG1022Addr,test)
    return k2450, k2700, afg

def connect_sample_with_AFG(k2700,sample_no=1):
    """
    Connect the function generator with sample using multiplexer.

    Parameters
    ----------
    k2700 : Keithley2700 multiplexer adapter
    sample_no : int, optional
        The default is 1.

    Returns
    -------
    None.

    """
    closed_channels = list(map(int,k2700.ask("ROUTe:MULTiple:CLOSe?")[2:-1].split(',')))
    required_channels = [sample_id[sample_no],AFG]
    channels_to_close = [x for x in required_channels if x not in closed_channels]
    channels_to_open = [x for x in closed_channels if x not in required_channels]
    k2700.close_Channels(channels_to_close)
    k2700.open_Channels(channels_to_open)
    waitFor(20) # wait for 20msec to ensure switching is complete

def connect_sample_with_SMU(k2700,sample_no=1):
    """
    Connect the function generator with sample using multiplexer.

    Parameters
    ----------
    k2700 : Keithley2700 multiplexer adapter
    sample_no : int, optional
        The default is 1.

    Returns
    -------
    None.

    """
    closed_channels = list(map(int,k2700.ask("ROUTe:MULTiple:CLOSe?")[2:-1].split(',')))
    required_channels = [sample_id[sample_no],SMU]
    channels_to_close = [x for x in required_channels if x not in closed_channels]
    channels_to_open = [x for x in closed_channels if x not in required_channels]
    k2700.close_Channels(channels_to_close)
    k2700.open_Channels(channels_to_open)
    waitFor(20) # wait for 20msec to ensure switching is complete
    
def waitFor(self, wtime): # wtime is in msec
    loop = QEventLoop()
    QTimer.singleShot(wtime, loop.quit)
    loop.exec_()
    
def linlogspace(counts,start=1,points_per_order=9):
    max_order = int(log10(counts))
    lin_ranges = logspace(start,max_order,(max_order-start)+1)
    npoints = [1]
    for i in range(len(lin_ranges)-1):
        npoints.extend(list(linspace(lin_ranges[i],lin_ranges[i+1],points_per_order,endpoint=False)))
    if points_per_order <= 9:
        last_order_divisions = int(counts/10**max_order)
    else:
        last_order_divisions = int(counts*points_per_order/(9*10**max_order)-1)
    npoints.extend(list(linspace(10**max_order,counts,last_order_divisions)))
    npoints = list(dict.fromkeys(npoints))
    return npoints

def getBinnedPoints(points):
    fpoints = [1]
    fpoints.extend(list(diff(points)))
    return fpoints
    
    
        
        
        