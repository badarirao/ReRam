"""Utilities file with useful classes and functions."""

from datetime import datetime
from os.path import abspath, join, exists
from pyvisa import ResourceManager, VisaIOError
from os import makedirs
from copy import copy
from re import sub
from MyKeithley2450 import Keithley2450
from MyKeithley2700 import Keithley2700
from MyAFG1022 import AFG1022 
from PyQt5.QtCore import QObject, QTimer, QEventLoop, pyqtSignal
from PyQt5.QtWidgets import QTimeEdit, QSpinBox
from math import log10
from numpy import logspace, linspace, diff
from time import sleep
from PyQt5.QtWidgets import QMessageBox

SMU = 101
AFG = 102
SMU4PROBE = 115
SAMPLE1 = 106
SAMPLE2 = 107
SAMPLE3 = 108
CRYOCHAMBER1 = 109
CRYOCHAMBER2 = 110

CONNECTION = 1

sample_id = {
                0 : SAMPLE1,
                1 : SAMPLE2,
                2 : SAMPLE3,
                3 : CRYOCHAMBER1,
                4 : CRYOCHAMBER2
            }

sample_key = {
                106 : 0,
                107 : 1,
                108 : 2,
                109 : 3,
                110 : 4
            }

inst_id = {
                0 : SMU,
                1 : AFG,
                4 : SMU4PROBE
            }

inst_key = {
                101 : 0,
                102 : 1,
                115 : 4
            }

class MyTimeEdit(QTimeEdit):
    def stepBy(self,steps):
        cur = self.time()
        QTimeEdit.stepBy(self,steps)
        if self.currentSection() == self.SecondSection:
            sec = cur.second()
            if sec == 0 and steps < 0:
                self.setTime(cur.addSecs(-steps))
            elif sec == 59 and steps > 0:
                self.setTime(cur.addSecs(steps))
        elif self.currentSection() == self.MinuteSection:
            minute = cur.minute()
            if minute == 0 and steps < 0:
                self.setTime(cur.addSecs(-60*steps))
            elif minute == 59 and steps > 0:
                self.setTime(cur.addSecs(60*steps))
       
class Communicate(QObject):
    message = pyqtSignal(int)

class connectedSpinBox(QSpinBox):
    def __init__(self,*args,**kwargs):
        super(connectedSpinBox,self).__init__(*args,**kwargs)
        self.hasWrapped = Communicate()
        
    def stepBy(self,steps):
        cur = self.value()
        QSpinBox.stepBy(self,steps)
        if cur == 1 and steps < 0:
            self.hasWrapped.message.emit(-1)
        elif cur == 9 and steps > 0:
            self.hasWrapped.message.emit(1)
        
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
        self.ID = 'Fake'

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
            msg = QMessageBox()
            title = "No Instrument connected"
            text = "Cannot find required instruments. Check connections again and restart program."
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowTitle(title)
            msg.setText(text)
            msg.exec()
            return 0,0
        
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
            if _ == 0 and test == False:
                return 0,0,0
        if k2700Status == 0:
            k2700,_ = connectDevice(Keithley2700,k2700Addr,test)
            if _ == 0 and test == False:
                return 0,0,0
        if afgStatus == 0:
            afg,_ = connectDevice(AFG1022,AFG1022Addr,test)
            if _ == 0 and test == False:
                return 0,0,0
    return k2450, k2700, afg

def connect_sample_with_AFG(k2700,sample_no=0):
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
    closed_CHs = k2700.ask("ROUTe:MULTiple:CLOSe?")
    if closed_CHs is not None:
        if closed_CHs == '(@)\n':
            closed_channels = []
        else:
            closed_channels = list(map(int,closed_CHs[2:-2].split(',')))
        if CONNECTION == 1: # SMU connected through connection 1 of MUX
            closed_channels = [x for x in closed_channels if x <= 110]
            required_channels = [sample_id[sample_no],AFG]
            k2700.open_Channels([sample_id[sample_no]+10,AFG+10])
        elif CONNECTION == 2:
            closed_channels = [x for x in closed_channels if x > 110 and x <= 120]
            required_channels = [sample_id[sample_no]+10,AFG+10]
            k2700.open_Channels([sample_id[sample_no],AFG])
        channels_to_close = [x for x in required_channels if x not in closed_channels]
        channels_to_open = [x for x in closed_channels if x not in required_channels]
        k2700.close_Channels(channels_to_close)
        k2700.open_Channels(channels_to_open)
        sleep(0.2)
        #waitFor(20) # wait for 20msec to ensure switching is complete

def connect_sample_with_SMU(k2700,sample_no=0):
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
    closed_CHs = k2700.ask("ROUTe:MULTiple:CLOSe?")
    if closed_CHs is not None:
        if closed_CHs == '(@)\n':
            closed_channels = []
        else:
            closed_channels = list(map(int,closed_CHs[2:-2].split(',')))
        if CONNECTION == 1: # SMU connected through connection 1 of MUX
            closed_channels = [x for x in closed_channels if x <= 110]
            required_channels = [sample_id[sample_no],SMU]
            k2700.open_Channels([sample_id[sample_no]+10,SMU+10])
        elif CONNECTION == 2:
            closed_channels = [x for x in closed_channels if x > 110 and x <= 120]
            required_channels = [sample_id[sample_no]+10,SMU+10]
            k2700.open_Channels([sample_id[sample_no],SMU])
        channels_to_close = [x for x in required_channels if x not in closed_channels]
        channels_to_open = [x for x in closed_channels if x not in required_channels]
        k2700.close_Channels(channels_to_close)
        k2700.open_Channels(channels_to_open)
        sleep(0.2)
        #waitFor(20) # wait for 20msec to ensure switching is complete
    
def waitFor(wtime): # wtime is in msec
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

def getBinnedPoints(points,start=1):
    fpoints = [start]
    fpoints.extend(list(diff(points).astype(float)))
    return fpoints

def check_mux(self):
    # If mux is connected, get connection details directly from mux
    # If mux is not accessible, get connection details from saved file
    pass
    
    
        
        
        