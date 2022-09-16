# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:47:30 2021
USER5 is pospulse # custom positive pulse, already set in the instrument
USER6 is negpulse # custom negative pulse, already set in the instrument
@author: Badari
"""
# USB::0x0699::0x0353::1643763::INSTR
from pyvisa import ResourceManager, VisaIOError
from PyQt5.QtCore import QEventLoop, QTimer, QSize, QRect, QMetaObject, QCoreApplication
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QWidget, QPushButton, QStatusBar, QApplication, QMainWindow, QMessageBox
from numpy import zeros, uint16, int32, min as npmin, max as npmax
from time import sleep

# afg = AFG1022("USB::0x0699::0x0353::1643763::INSTR")
class AFG1022:
    def __init__(self,adapter,**kwargs):
        if isinstance(adapter,str):
            rm = ResourceManager()
            self.inst = rm.open_resource(adapter)
            self.address = adapter
            self.instrument_limits = {
                "frequency lims": ({"min": 1e-6, "max": 25e6}, "Hz"),
                "voltage lims": (
                    {"50ohm": {"min": -5, "max": 5}, "highZ": {"min": -10, "max": 10}},
                    "V",
                ),
                "amplitude lims": (
                    {
                        "50ohm": {"min": 0.001, "max": 10},
                        "highZ": {"min": 0.002, "max": 20},
                    },
                    "Vpp",
                ),
            }
            self._arbitrary_waveform_length = [2, 8192]  # min length, max length
            self._arbitrary_waveform_resolution = 16383  # 14 bit
            self._max_waveform_memory_user_locations = 255
            self.output(1)
            self.ID = 'AFG1022'
            self.name = 'Tektronix AFG1022 Function generator'
        else:
            raise VisaIOError(-1073807346)
        
    def _set_custom_waveform(
        self,
        waveform: "numpy array",
        normalise: bool = True,
        memory_num: int = 0
    ):
        """Transfer waveform data to edit memory and then user memory.
        NOTE: Will overwrite without warnings
        Parameters
        ----------
        waveform : ndarray
            Either unnormalised arbitrary waveform (then use `normalise=True`),
            or ints spanning the resolution of the function generator
        normalise : bool
            Choose whether to normalise the waveform to ints over the
            resolution span of the function generator
        memory_num : str or int {0,...,255}, default 0
            Select which user memory to copy to
        verify : bool, default `True`
            Verify that the waveform has been transferred and is what was sent
        Returns
        -------
        waveform : ndarray
            The normalised waveform transferred
        Raises
        ------
        ValueError
            If the waveform is not within the permitted length or value range
        RuntimeError
            If the waveform transferred to the instrument is of a different
            length than the waveform supplied
        """
        if not 0 <= memory_num <= self._max_waveform_memory_user_locations:
            raise ValueError(
                f"The memory location {memory_num} is not a valid "
                "memory location for this model"
            )
        # Check if waveform data is suitable
        self._check_arb_waveform_length(waveform)
        try:
            self._check_arb_waveform_type_and_range(waveform)
        except ValueError as err:
            waveform = self._normalise_to_waveform(waveform)
        # Transfer waveform
        self.inst.write_binary_values(
            "DATA:DATA EMEMory,", waveform, datatype="H", is_big_endian=True
        )
        # Check for errors and check lengths are matching
        transfer_error = self.get_error()
        emem_wf_length = self.ask("DATA:POINts? EMEMory")
        if emem_wf_length == "" or not int(emem_wf_length) == len(waveform):
            msg = (
                f"Waveform in temporary EMEMory has a length of {emem_wf_length}"
                f", not of the same length as the waveform ({len(waveform)})."
                f"\nError from the instrument: {transfer_error}"
            )
            raise RuntimeError(msg)
        self.write(f"DATA:COPY USER{memory_num},EMEMory")
        return waveform
    
    def _check_arb_waveform_length(self, waveform: "numpy array"):
        """Checks if waveform is within the acceptable length
        Parameters
        ----------
        waveform : array_like
            Waveform or voltage list to be checked
        Raises
        ------
        ValueError
            If the waveform is not within the permitted length
        """
        if (len(waveform) < self._arbitrary_waveform_length[0]) or (
            len(waveform) > self._arbitrary_waveform_length[1]
        ):
            msg = (
                "The waveform is of length {}, which is not within the "
                "acceptable length {} < len < {}"
                "".format(len(waveform), *self._arbitrary_waveform_length)
            )
            raise ValueError(msg)
    
    def _check_arb_waveform_type_and_range(self, waveform: "numpy array"):
        """Checks if waveform is of int/np.int32 type and within the resolution
        of the function generator
        Parameters
        ----------
        waveform : array_like
            Waveform or voltage list to be checked
        Raises
        ------
        ValueError
            If the waveform values are not int, np.uint16 or np.int32, or the
            values are not within the permitted range
        """
        for value in waveform:
            if not isinstance(value, (int, uint16, int32)):
                raise ValueError(
                    "The waveform contains values that are not"
                    "int, np.uint16 or np.int32"
                )
            if (value < 0) or (value > self._arbitrary_waveform_resolution):
                raise ValueError(
                    f"The waveform contains values out of range "
                    f"({value} is not within the resolution "
                    f"[0, {self._arbitrary_waveform_resolution}])"
                )
    
    def _normalise_to_waveform(self, shape:"numpy array"):
        """Normalise a shape of any discretisation and range to a waveform that
        can be transmitted to the function generator
        .. note::
            If you are transferring a flat/constant waveform, do not use this
            normaisation function. Transfer a waveform like
            `int(self._arbitrary_waveform_resolution/2)*np.ones(2).astype(np.int32)`
            without normalising for a well behaved flat function.
        Parameters
        ----------
        shape : array_like
            Array to be transformed to waveform, can be ints or floats,
            any normalisation or discretisation
        Returns
        -------
        waveform : ndarray
            Waveform as ints spanning the resolution of the function gen
        """
        # Check if waveform data is suitable
        self._check_arb_waveform_length(shape)
        # Normalise
        waveform = shape - npmin(shape)
        normalisation_factor = npmax(waveform)
        waveform = waveform / normalisation_factor * self._arbitrary_waveform_resolution
        return waveform.astype(uint16)
            
    def get_waveform_catalogue(self):
        """Get list of the waveforms that are in use (not empty)
        Returns
        -------
        catalogue : list
            Strings with the names of the user functions that are not empty
        """
        catalogue = self.ask("DATA:CATalog?").split(",")
        catalogue = [wf[1:-1] for wf in catalogue]  # strip off extra quotes
        return catalogue
    
    def get_error(self) -> str:
        """Get the contents of the Error/Event queue on the device
        Returns
        -------
        str
            Error/event number, description of error/event
        """
        return self.ask("SYSTEM:ERROR:NEXT?")
    
    def getinfo(self):
        print(self.inst.query('*IDN?'))
    
    def ask(self,cmd):
        return self.inst.query(cmd)
    
    def write(self,cmd):
        self.inst.write(cmd)
    
    def read(self):
        return self.inst.read()
        
    def configure_pulse_measurement(self):
        self.write("SOURce1:BURST:MODE TRIGgered")
        self.write("SOURce1:BURST:NCYCles 1")
        self.write("SOURce1:BURST:STATE ON")
    
    def setSinglePulse(self,volts,pulseWidth): # seconds
        if pulseWidth > 5.0: # max width is is set to 5 seconds
            pulseWidth = 5.0
            print("Pulse width exceeded max limit, reset to 5 s.")
        elif pulseWidth < 1e-7: # min width is 100 ns -> machine limit
            pulseWidth = 1e-7
            print("Pulse width less than min limit, reset to 100 ns.")
        self.write('SOURce1:FREQuency:FIXed {}'.format((1/(pulseWidth*2))))
        if volts >= 0 and volts <= 10:
            self.write("SOURce1:FUNCtion:SHAPe USER5")
            self.write('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude {}'.format(volts/2))
            self.write('SOURce1:VOLTage:LEVel:IMMediate:OFFSet {}'.format(volts/4))
        elif volts < 0 and volts >= -10:
            self.write("SOURce1:FUNCtion:SHAPe USER6")
            self.write('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude {}'.format(-volts/2))
            self.write('SOURce1:VOLTage:LEVel:IMMediate:OFFSet {}'.format(volts/4))
        else:
            print("ERROR! Voltage out of range. Select within (-5V,5V) and magnitude greater than 1 mV")
            
    def setNPulses(self,v1,pw1,v2,pw2,n): # multiple pulses, pw is in seconds
        amplitude = abs(v1-v2)/2
        offset = (v1+v2)/4
        frequency = 1/(pw1+pw2)
        if pw1 == pw2:
            self.write("SOURce1:FUNCtion:SHAPe SQUARE")
        else:
            self.write("SOURce1:FUNCtion:SHAPe USER7")
        self.write('SOURce1:FREQuency:FIXed {}'.format(frequency))
        self.write('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude {}'.format(amplitude))
        self.write('SOURce1:VOLTage:LEVel:IMMediate:OFFSet {}'.format(offset))
        self.write("SOURce1:BURST:NCYCles {}".format(n))
    
    def configure_user7(self,x:int):
        waveform = zeros(8000)
        waveform[:x] = 1
        waveform[x:] = -1
        self._set_custom_waveform(waveform,memory_num=7)
        
    def trgNwait(self):
        sleep(0.1)
        pw = 1000/float(self.ask('source1:frequency:fixed?'))  # milliseconds
        sleep(0.1)
        nc = int(self.ask("SOURce1:BURST:NCYCles?"))
        sleep(0.1)
        self.trigger()
        if (pw*nc) < 10: # fix min wait time as 10 ms.
            pw = 10
            nc = 1
        loop = QEventLoop()
        QTimer.singleShot(int(pw*nc), loop.quit)
        loop.exec_()
    
    def trigger(self):
        self.write('*TRG')
        
    def close(self):
        self.inst.close()
        
    def output(self,state):
        self.write('OUTPut1:STATe {}'.format(state))