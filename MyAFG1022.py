# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:47:30 2021
USER5 is pospulse
USER6 is negpulse
@author: Badari
"""
# USB::0x0699::0x0353::1643763::INSTR
from pyvisa import ResourceManager
from pyvisa.errors import VisaIOError
from PyQt5.QtCore import QEventLoop, QTimer

class AFG1022:
    def __init__(self,adapter,**kwargs):
        if isinstance(adapter,str):
            rm = ResourceManager()
            self.inst = rm.open_resource(adapter)
        
    def getinfo(self):
        print(self.inst.query('*IDN?'))
    
    def ask(self,cmd):
        return self.inst.query(cmd)
    
    def write(self,cmd):
        self.inst.write(cmd)
    
    def read(self):
        self.inst.read()
        
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
        if volts >= 0.001 and volts <= 10:
            self.write("SOURce1:FUNCtion:SHAPe USER5")
            self.write('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude {}'.format(volts/2))
            self.write('SOURce1:VOLTage:LEVel:IMMediate:OFFSet {}'.format(volts/4))
        elif volts < -0.001 and volts >= -10:
            self.write("SOURce1:FUNCtion:SHAPe USER6")
            self.write('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude {}'.format(-volts/2))
            self.write('SOURce1:VOLTage:LEVel:IMMediate:OFFSet {}'.format(volts/4))
        else:
            print("ERROR! Voltage out of range. Select within (-5V,5V) and magnitude greater than 1 mV")
            
    def setPulses(self,v,pw,n): # multiple pulses
        pass
    
    def apply_pulse(self,volts,pulse_width):
        pass
    
    def trgNwait(self):
        pw = float(self.ask('source1:frequency:fixed?'))
        nc = int(self.ask("SOURce1:BURST:NCYCles?"))
        self.trigger()
        if ((1/pw)*nc) > 0.001: # if pulse width is more thatn
            loop = QEventLoop()
            QTimer.singleShot(1/pw, loop.quit)
            loop.exec_()
    
    def trigger(self):
        self.write('*TRG')
        
    def close(self):
        self.inst.close()
        
    def output(self,state):
        self.write('OUTPut1:STATe {}'.format(state))
        