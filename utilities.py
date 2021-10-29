"""Utilities file with useful classes and functions."""

from datetime import datetime
from os.path import abspath, join, exists
from pyvisa import ResourceManager, VisaIOError
from os import makedirs
from copy import copy
from re import sub
from sys import exit as exitprogram
from pymeasure.instruments.keithley import Keithley2450
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QTimeEdit, QSpinBox

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
        
def checkInstrument(k2450Addr = None, test = False):
    """
    Obtain instrument address of K2450.

    Returns: k2450 object
    -------
    Instrument objects pointing to K2450
    if test is True,
        return FakeAdapter if instrument is not found,
    else exit program
    """
    deviceAddr = k2450Addr
    rm = ResourceManager()
    k2450Status =  0
    if k2450Addr:
        k2450, k2450Status = connectDevice(Keithley2450,k2450Addr,test=True)
    status = k2450Status
    deviceInfo = ['KEITHLEY','2450']
    if status == 0:
        instList = rm.list_resources()
        for inst in instList:
            try:
                myInst = rm.open_resource(inst)
                instID = myInst.query('*IDN?').split(',')
                if deviceInfo[0] in instID[0] and deviceInfo[1] in instID[1]:
                    deviceAddr = inst
                    break
            except VisaIOError:
                pass
        k2450Addr = deviceAddr
        if k2450Status == 0:
                k2450,_ = connectDevice(Keithley2450,k2450Addr,test)
    return k2450