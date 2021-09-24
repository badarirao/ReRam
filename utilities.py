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


def checkInstrument(test = False):
    """
    Obtain instrument address of K2450, K2700 and function generator.

    Returns: list of instrument objects
    -------
    Instrument objects pointing to K2450, K2700 and AFG1022
    if test is True,
        return FakeAdapter if any instrument is not found
    else exit program
    """
    rm = ResourceManager()
    instList = rm.list_resources()
    k2450Addr = ''
    k2700Addr = ''
    AFG1022Addr = ''
    for inst in instList:
        try:
            myInst = rm.open_resource(inst)
            instID = myInst.query('*IDN?').split(',')
            if 'KEITHLEY' in instID[0] and '2450' in instID[1]:
                k2450Addr = inst
            elif 'KEITHLEY' in instID[0] and '2700' in instID[1]:
                k2700Addr = inst
            elif 'TEKTRONIX' in instID[0] and 'AFG1022' in instID[1]:
                AFG1022Addr = inst
        except VisaIOError:
            pass
    try:
        k2450 = Keithley2450(k2450Addr)
        k2700 = Keithley2700(k2700Addr)
        afg = AFG1022(AFG1022Addr)
    except VisaIOError:
        if test is True:
            if not k2450Addr:
                k2450 = FakeAdapter()
            if not k2700Addr:
                k2700 = FakeAdapter()
            if not AFG1022Addr:
                afg = FakeAdapter()
        else:
            # TODO: Prompt a GUI message instead
            print("Instrument not connected! Check connections!")
            exitprogram()
    return k2450, k2700, afg
