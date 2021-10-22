#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2020 PyMeasure Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import logging
import time

import numpy as np
from pyvisa import ResourceManager
from pyvisa.errors import VisaIOError
from PyQt5.QtCore import QEventLoop, QTimer
# Setup logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class Keithley2450:
    """ Represents the Keithely 2450 SourceMeter and provides a
    high-level interface for interacting with the instrument.

    """

    def __init__(self,adapter,**kwargs):
        if isinstance(adapter,str):
            rm = ResourceManager()
            self.inst = rm.open_resource(adapter)
            self.address = adapter
        else:
            raise VisaIOError(-1073807346)
        self.name = "Keithley 2450 SMU"

    def ask(self,cmd):
        return self.inst.query(cmd)
    
    def write(self,cmd):
        self.inst.write(cmd)
    
    def read(self):
        return self.inst.read()
    
    def close(self):
        self.inst.close()
    
    def start_buffer(self):
        """ Starts the buffer. """
        self.write(":INIT")

    def reset_buffer(self):
        """ Resets the buffer. """
        self.write(":STAT:PRES;*CLS;:TRAC:CLEAR;:TRAC:FEED:CONT NEXT;")
        
    def enable_source(self):
        """ Enables the source of current or voltage depending on the
        configuration of the instrument. """
        self.write("OUTPUT ON")


    def disable_source(self):
        """ Disables the source of current or voltage depending on the
        configuration of the instrument. """
        self.write("OUTPUT OFF")


    def measure_resistance(self, nplc=1, resistance=2.1e5, auto_range=True):
        """ Configures the measurement of resistance.

        :param nplc: Number of power line cycles (NPLC) from 0.01 to 10
        :param resistance: Upper limit of resistance in Ohms, from -210 MOhms to 210 MOhms
        :param auto_range: Enables auto_range if True, else uses the set resistance
        """
        log.info("%s is measuring resistance.", self.name)
        self.write(":SENS:FUNC 'RES';"
                   ":SENS:RES:NPLC %f;" % nplc)
        if auto_range:
            self.write(":SENS:RES:RANG:AUTO 1;")
        else:
            self.resistance_range = resistance


    def measure_voltage(self, nplc=1, voltage=21.0, auto_range=True):
        """ Configures the measurement of voltage.

        :param nplc: Number of power line cycles (NPLC) from 0.01 to 10
        :param voltage: Upper limit of voltage in Volts, from -210 V to 210 V
        :param auto_range: Enables auto_range if True, else uses the set voltage
        """
        log.info("%s is measuring voltage.", self.name)
        self.write(":SENS:FUNC 'VOLT';"
                   ":SENS:VOLT:NPLC %f;" % nplc)
        if auto_range:
            self.write(":SENS:VOLT:RANG:AUTO 1;")
        else:
            self.voltage_range = voltage


    def measure_current(self, nplc=1, current=1.05e-4, auto_range=True):
        """ Configures the measurement of current.

        :param nplc: Number of power line cycles (NPLC) from 0.01 to 10
        :param current: Upper limit of current in Amps, from -1.05 A to 1.05 A
        :param auto_range: Enables auto_range if True, else uses the set current
        """
        log.info("%s is measuring current.", self.name)
        self.write(":SENS:FUNC 'CURR';"
                   ":SENS:CURR:NPLC %f;" % nplc)
        if auto_range:
            self.write(":SENS:CURR:RANG:AUTO 1;")
        else:
            self.current_range = current


    def auto_range_source(self):
        """ Configures the source to use an automatic range.
        """
        if self.source_mode == 'current':
            self.write(":SOUR:CURR:RANG:AUTO 1")
        else:
            self.write(":SOUR:VOLT:RANG:AUTO 1")

    def apply_current(self, current_range=None,
             compliance_voltage=0.1):
        """ Configures the instrument to apply a source current, and
        uses an auto range unless a current range is specified.
        The compliance voltage is also set.

        :param compliance_voltage: A float in the correct range for a
                                   :attr:`~.Keithley2450.compliance_voltage`
        :param current_range: A :attr:`~.Keithley2450.current_range` value or None
        """
        log.info("%s is sourcing current.", self.name)
        self.source_mode = 'current'
        if current_range is None:
            self.auto_range_source()
        else:
            self.source_current_range = current_range
        self.compliance_voltage = compliance_voltage


    def apply_voltage(self, voltage_range=None,
            compliance_current=0.1):
        """ Configures the instrument to apply a source voltage, and
        uses an auto range unless a voltage range is specified.
        The compliance current is also set.

        :param compliance_current: A float in the correct range for a
                                   :attr:`~.Keithley2450.compliance_current`
        :param voltage_range: A :attr:`~.Keithley2450.voltage_range` value or None
        """
        log.info("%s is sourcing voltage.", self.name)
        self.source_mode = 'voltage'
        if voltage_range is None:
            self.auto_range_source()
        else:
            self.source_voltage_range = voltage_range
        self.compliance_current = compliance_current

    def beep(self, frequency, duration):
        """ Sounds a system beep.

        :param frequency: A frequency in Hz between 65 Hz and 2 MHz
        :param duration: A time in seconds between 0 and 7.9 seconds
        """
        self.write(":SYST:BEEP %g, %g" % (frequency, duration))


    def triad(self, base_frequency, duration):
        """ Sounds a musical triad using the system beep.

        :param base_frequency: A frequency in Hz between 65 Hz and 1.3 MHz
        :param duration: A time in seconds between 0 and 7.9 seconds
        """
        self.beep(base_frequency, duration)
        time.sleep(duration)
        self.beep(base_frequency*5.0/4.0, duration)
        time.sleep(duration)
        self.beep(base_frequency*6.0/4.0, duration)


    @property
    def error(self):
        """ Returns a tuple of an error code and message from a
        single error. """
        err = self.values(":system:error?")
        if len(err) < 2:
            err = self.read() # Try reading again
        code = err[0]
        message = err[1].replace('"', '')
        return (code, message)


    def reset(self):
        """ Resets the instrument and clears the queue.  """
        self.write("*RST;:stat:pres;:*CLS;")

    def ramp_to_current(self, target_current, steps=30, pause=20e-3):
        """ Ramps to a target current from the set current value over
        a certain number of linear steps, each separated by a pause duration.

        :param target_current: A current in Amps
        :param steps: An integer number of steps
        :param pause: A pause duration in seconds to wait between steps
        """
        currents = np.linspace(
            self.source_current,
            target_current,
            steps
        )
        for current in currents:
            self.source_current = current
            time.sleep(pause)

    def ramp_to_voltage(self, target_voltage, steps=30, pause=20e-3):
        """ Ramps to a target voltage from the set voltage value over
        a certain number of linear steps, each separated by a pause duration.

        :param target_voltage: A voltage in Amps
        :param steps: An integer number of steps
        :param pause: A pause duration in seconds to wait between steps
        """
        voltages = np.linspace(
            self.source_voltage,
            target_voltage,
            steps
        )
        for voltage in voltages:
            self.source_voltage = voltage
            time.sleep(pause)

    def trigger(self):
        """ Executes a bus trigger.
        """
        return self.write("*TRG")

    @property
    def mean_voltage(self):
        """ Returns the mean voltage from the buffer """
        return self.means[0]

    @property
    def max_voltage(self):
        """ Returns the maximum voltage from the buffer """
        return self.maximums[0]

    @property
    def min_voltage(self):
        """ Returns the minimum voltage from the buffer """
        return self.minimums[0]

    @property
    def std_voltage(self):
        """ Returns the voltage standard deviation from the buffer """
        return self.standard_devs[0]

    @property
    def mean_current(self):
        """ Returns the mean current from the buffer """
        return self.means[1]

    @property
    def max_current(self):
        """ Returns the maximum current from the buffer """
        return self.maximums[1]

    @property
    def min_current(self):
        """ Returns the minimum current from the buffer """
        return self.minimums[1]

    @property
    def std_current(self):
        """ Returns the current standard deviation from the buffer """
        return self.standard_devs[1]

    @property
    def mean_resistance(self):
        """ Returns the mean resistance from the buffer """
        return self.means[2]

    @property
    def max_resistance(self):
        """ Returns the maximum resistance from the buffer """
        return self.maximums()[2]

    @property
    def min_resistance(self):
        """ Returns the minimum resistance from the buffer """
        return self.minimums[2]

    @property
    def std_resistance(self):
        """ Returns the resistance standard deviation from the buffer """
        return self.standard_devs[2]

    def use_rear_terminals(self):
        """ Enables the rear terminals for measurement, and
        disables the front terminals. """
        self.write(":ROUT:TERM REAR")

    def use_front_terminals(self):
        """ Enables the front terminals for measurement, and
        disables the rear terminals. """
        self.write(":ROUT:TERM FRON")

    def shutdown(self):
        """ Ensures that the current or voltage is turned to zero
        and disables the output. """
        log.info("Shutting down %s.", self.name)
        if self.source_mode == 'current':
            self.ramp_to_current(0.0)
        else:
            self.ramp_to_voltage(0.0)
        self.stop_buffer()
        self.disable_source()
    
    def wait_till_done(self, wait_time=10):
        """
        Wait until the measurement is completed.

            Infinite loop runs until the 'state' is not 'RUNNING'

        Returns
        -------
        int
            1: if the measurement has successfully finished
            0: if there is some error
        """
        loop = QEventLoop()
        while True:
            QTimer.singleShot(wait_time, loop.quit)
            loop.exec_()
            state = self.ask("Trigger:state?").split(';')[0]
            if state == 'IDLE':
                return 1
            elif state != 'RUNNING':
                return 0
            
    def apply_switch_pulse(self,voltage,pulse_width):
        """
        Apply the required switching pulse, and return the voltage & current.

        Parameters
        ----------
        voltage : float
        pulse_width : float
            Positive

        Returns
        -------
        list of voltage and current

        """
        self.write("SENSe:CURRent:NPLCycles 0.01")
        self.write("TRIG:LOAD 'SimpleLoop', 1, {0}".format(pulse_width))
        self.source_voltage = voltage
        self.start_buffer()
        self.wait_till_done(1)
        return map(float, self.ask("TRAC:data? 1, 1, 'defbuffer1', sour, read")[:-1].split(','))
    
    def readReRAM(self):
        self.start_buffer()
        self.wait_till_done()
        return float(self.ask("TRAC:stat:average?")[:-1])
