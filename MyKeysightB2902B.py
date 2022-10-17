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

# kB2920B = KeysightB2902B("USB0::0x2A8D::0x9201::MY61390641::INSTR")
class KeysightB2902B:
    """ Represents the Keysight B2902B SourceMeter and provides a
    high-level interface for interacting with the instrument.

    """

    def __init__(self,adapter,channel = 1, **kwargs):
        if isinstance(adapter,str):
            rm = ResourceManager()
            self.inst = rm.open_resource(adapter)
            self.name = 'Keysight B2902B SMU'
            self.address = adapter
            self.ID = 'B2902B'
            self._source_voltage = 0
            self.nplc = 1
            self.source_mode = 'voltage'
            self.sense_mode = 'current'
            self.ch = channel # channel number
            self.overVoltage_protection(False)
            self.wire_config = 2
            self.avg = 1 # number of readings to take and average
            self.write(f"TRAC{self.ch}:FEED SENS")
            self.write(f":OUTP{self.ch}:LOW flo") # float LOW TERMINAL
            self.pulse_delay = 2e-5  # set a default 20 µs pulse delay
        else:
            raise VisaIOError(-1073807346)
        self.name = "Keysight B2902B SMU"

    @property 
    def source_voltage(self):
        self._source_voltage = float(self.ask(f":SOUR{self.ch}:VOLT?"))
        return self._source_voltage
        
    @source_voltage.setter 
    def source_voltage(self,value):
        # output voltage when output is on
        # ensure source mode is voltage (apply_voltage())
        self._source_voltage = value
        self.write(f":SOUR{self.ch}:VOLT {value}")
    
    @property 
    def source_current(self):
        self._source_current = float(self.ask(f":SOUR{self.ch}:CURR?"))
        return self._source_current
        
    @source_current.setter 
    def source_current(self,value):
        # output current when output is on
        # ensure source mode is current (apply_current())
        self._source_current = value
        self.write(f":SOUR{self.ch}:CURR {value}")

    def ask(self,cmd):
        ans = self.inst.query(cmd)
        #if self.error[1] != 'No error':
        #    print(f"Problem with {cmd}")
        return ans

    def write(self,cmd):
        self.inst.write(cmd)
        error_message = self.error
        if error_message[1] != 'No error':
            print(f"Problem with {cmd}")
            print(error_message)
    
    def read(self):
        return self.inst.read()
    
    def close(self):
        self.inst.close()
    
    def start_buffer(self):
        """ Starts the buffer. """
        self.write(f":INIT (@{self.ch})")

    def reset_buffer(self):
        """ Resets the buffer. """
        self.write(":STAT:PRES;*CLS;:TRAC:CLEAR;:TRAC:FEED:CONT NEXT;")
        
    def enable_source(self):
        """ Enables the source of current or voltage depending on the
        configuration of the instrument. """
        self.write(f"OUTPUT{self.ch} ON")


    def disable_source(self):
        """ Disables the source of current or voltage depending on the
        configuration of the instrument. """
        self.write(f"OUTPUT{self.ch} OFF")


    def measure_resistance(self, resistance=2.1e5, auto_range=True):
        """ Configures the measurement of resistance.

        :param nplc: Number of power line cycles (NPLC) from 0.01 to 10
        :param resistance: Upper limit of resistance in Ohms, from -210 MOhms to 210 MOhms
        :param auto_range: Enables auto_range if True, else uses the set resistance
        """
        self.sense_mode = 'resistance'
        log.info("%s is measuring resistance.", self.name)
        self.write(f":SENS{self.ch}:FUNC 'RES'")
        self.write(f":SENS{self.ch}:RES:NPLC {self.nplc};")
        if auto_range:
            self.write(f":SENS{self.ch}:RES:RANG:AUTO 1")
        else:
            self.write(f":SENS{self.ch}:RES:RANG:AUTO 0")
            self.resistance_range = resistance


    def measure_voltage(self, voltage=21.0, auto_range=True):
        """ Configures the measurement of voltage.

        :param nplc: Number of power line cycles (NPLC) from 0.01 to 10
        :param voltage: Upper limit of voltage in Volts, from -210 V to 210 V
        :param auto_range: Enables auto_range if True, else uses the set voltage
        """
        self.sense_mode = 'voltage'
        log.info("%s is measuring voltage.", self.name)
        self.write(f":SENS{self.ch}:FUNC 'VOLT'")
        self.write(f":SENS{self.ch}:VOLT:NPLC {self.nplc};")
        if auto_range:
            self.write(f":SENS{self.ch}:VOLT:RANG:AUTO 1")
        else:
            self.write(f":SENS{self.ch}:VOLT:RANG:AUTO 0")
            self.voltage_range = voltage

    def measure_current(self, current=1.05e-4, auto_range=True):
        """ Configures the measurement of current.

        :param nplc: Number of power line cycles (NPLC) from 0.01 to 10
        :param current: Upper limit of current in Amps, from -1.05 A to 1.05 A
        :param auto_range: Enables auto_range if True, else uses the set current
        """
        self.sense_mode = 'current'
        log.info("%s is measuring current.", self.name)
        self.write(f":SENS{self.ch}:FUNC 'CURR'")
        self.setNPLC()
        if auto_range:
            self.write(f":SENS{self.ch}:CURR:RANG:AUTO 1")
        else:
            self.current_range = current


    def auto_range_source(self):
        """ Configures the source to use an automatic range.
        """
        if self.source_mode == 'current':
            self.write(f":SOUR{self.ch}:CURR:RANG:AUTO 1")
        else:
            self.write(f":SOUR{self.ch}:VOLT:RANG:AUTO 1")

    def auto_range_sense(self):
        """ Configures the sense to use an automatic range.
        """
        if self.source_mode == 'current':
            self.write(f"SENS{self.ch}:CURR:RANG:AUTO ON")
        else:
            self.write(f"SENS{self.ch}:VOLT:RANG:AUTO ON")
    
    def set_wire_configuration(self, config = 2):
        config = int(float(config))
        if config == 2:
            self.write(f"SENS{self.ch}:REM OFF") # Two wire configuration
        elif config == 4:
            self.write(f"SENS{self.ch}:REM ON") # Four wire configuration
        else:
            print("Wrong configuration command sent. Choose either 2 or 4 only.")
    
    def setNPLC(self, nplc = 'default'):
        # nplc can also be 'auto' for automatic selection depending on range
        if nplc == 'default':
            self.write(f"SENS{self.ch}:CURR:NPLC {self.nplc}")
        else:
            self.write(f"SENS{self.ch}:CURR:NPLC {nplc}")
    
    def apply_current(self, current_range=None,compliance_voltage=0.1):
        """ Configures the instrument to apply a source current, and
        uses an auto range unless a current range is specified.
        The compliance voltage is also set.

        :param compliance_voltage: A float in the correct range for a
                                   :attr:`~.Keithley2450.compliance_voltage`
        :param current_range: A :attr:`~.Keithley2450.current_range` value or None
        """
        log.info("%s is sourcing current.", self.name)
        self.source_mode = 'current'
        self.write(f"SOUR{self.ch}:FUNC:MODE CURR")
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
        self.write(f"SOUR{self.ch}:FUNC:MODE VOLT")
        if voltage_range is None:
            self.auto_range_source()
        else:
            self.source_voltage_range = voltage_range
        self.set_compliance(compliance_current)
        self.setNPLC()

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
        err = self.ask(":system:error?").strip().split(',')
        if len(err) != 2:
            err = self.read() # Try reading again
        code = err[0]
        message = err[1].replace('"', '')
        return (code, message)


    def reset(self):
        """ Resets the instrument and clears the queue.  """
        self.write("*RST;:stat:pres;*CLS;")

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
        pass

    def use_front_terminals(self):
        """ Enables the front terminals for measurement, and
        disables the rear terminals. """
        pass

    def correct_zero_at_beginning_only(self):
        pass
    
    def set_zero_correct_on(self):
        pass

    def set_source_compliance(self, limit):
        if self.source_mode == 'voltage':
            self.write(f"source:voltage:ilimit {limit}")
        elif self.source_mode == 'current':
            self.write(f"source:current:vlimit {limit}")
    
    def set_compliance(self, limit):
        if self.sense_mode == 'voltage':
            self.write(f"sense:voltage:prot {limit}")
        elif self.sense_mode == 'current':
            self.write(f"sense:current:prot {limit}")
    
    def set_positive_compliance(self, limit):
        if self.sense_mode == 'voltage':
            self.write(f"sense:voltage:prot:pos {limit}")
        elif self.sense_mode == 'current':
            self.write(f"sense:current:prot:pos {limit}")
    
    def set_negative_compliance(self, limit):
        if self.sense_mode == 'voltage':
            self.write(f"sense:voltage:prot:neg {limit}")
        elif self.sense_mode == 'current':
            self.write(f"sense:current:prot:neg {limit}")
    
    def set_read_back_on(self):
        # This SMU always returns actual voltage applied, so this command does not make sense.
        # If you want to know applied voltage, then you need to get it from your command.
        pass
            
    def format_sense_data(self): # set to get specified data when asked
        # get applied voltage, measured current, and state
        # I think state will give 1 if output was ON, and 0 if output was OFF
        self.write(":FORM:ELEM:SENS SOUR,CURR,STAT")
    
    def display_light(self, state='ON', percent = 25):
        # cannot set percent in this SMU. It has been kept to keep it similar to K2450
        self.write(f":DISPlay:enable {state}")
    
    def set_source_mode(self, mode):
        """
        Mode can be:
            FIX : fixed
            List: user defined custom list sweep
            Sweep: sweep

        Parameters
        ----------
        mode : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if mode.lower() == 'swe':
            mode = 'sweep'
        elif mode.lower() == 'fix':
            mode = 'fixed'
        assert mode.lower() in ('sweep', 'list', 'fixed')
        self.write(f':SOUR{self.ch}:{self.source_mode}:MODE {mode}')

    def set_voltage_points(self, points):
        points = points.replace(" ","")
        self.write(f"SOUR{self.ch}:LIST:VOLT {points}")
    
    def append_voltage_points(self, points):
        points = points.replace(" ","")
        self.write(f"SOUR{self.ch}:LIST:VOLT:APP {points}")
    
    def configure_sweep(self, delay = 0):
        """
        Set start Index of list, delay, sweep counts, and failAbort
        failAbort : OFF implies, if limiting current is reached, it will not stop.

        Parameters
        ----------
        delay : TYPE, optional
            DESCRIPTION. The default is 0.

        Returns
        -------
        None.

        """
        self.write(f"SOUR{self.ch}:FUNC:SHAP DC")
        self.source_sweep_mode('list')
        self.write(":trig:sour AINT") # auto decide trigger method (TODO: how about using TIM instead of aint? Currently delay doesn't work with tim)
        self.write(f"TRIG{self.ch}:TRAN:DEL 0")      # should it be zero or some finite value? (for aint, I guess some internal delay is added)
        self.write(f"TRIG{self.ch}:ACQ:DEL {delay}")
        nPoints = int(float(self.ask(f"SOUR{self.ch}:LIST:VOLT:POINts?").strip()))
        self.write(f"trig{self.ch}:coun {nPoints}")
        self.write(":FORM:ELEM:SENS VOLT,CURR")
        self.clear_buffer(nPoints)
        #self.write(f"TRAC{self.ch}:TST:FORM ABS") # set timestamp to absolute

    def clear_buffer(self,nPoints):
        self.write(f"TRAC{self.ch}:FEED:CONT NEV")
        self.write(f"TRAC{self.ch}:CLEar")
        self.write(f"TRAC{self.ch}:POIN {nPoints}") #maybe not needed
        self.write(f"TRAC{self.ch}:FEED:CONT NEXT")
        # TODO: check if the following 2 lines can be set only at the beginning
        #self.write(f"TRAC{self.ch}:TST:FORM ABS")

    def set_simple_loop(self, count=1, delayTime = 0):
        pass

        """if delayTime <= 0:
            self.write(f"SOUR{self.ch}:WAIT:AUTO ON")
            self.write(f"SOUR{self.ch}:WAIT OFF")
        else:
            self.write(f"SOUR{self.ch}:WAIT ON")
            self.write(f"SOUR{self.ch}:WAIT:AUTO OFF")
            self.write(f"SOUR{self.ch}:WAIT:OFFS {delayTime}")
        self.write(f"TRIG:LOAD 'SimpleLoop', {count}, {delayTime}")"""
    
    def is_compliance_tripped(self):
        if self.sense_mode == 'voltage':
            return int(float(self.ask(f"SENS{self.ch}:VOLT:PROT:TRIP?").strip()))
        elif self.sense_mode == 'current':
            return int(float(self.ask(f"SENS{self.ch}:CURR:PROT:TRIP?").strip()))
        else:
            print("Some error occurred in 'Keysight 2902B -  is_compliance_tripped' command")
            return True
    
    def get_start_point(self):
        # you can set trace:data to measure from current data position directly
        return 'CURR'
    
    def set_measurement_count(self, count=1):
        pass # need to ignore this for forming program; using measure? command instead for 1 point.
        #self.write(f"TRACe{self.ch}:POINts {count}")
    
    def get_end_point(self):
        # You can specify size of data to be received in trace:data. If not specified, all available is returned
        pass
        return 1
    
    def set_return_data_format(self): # set to return source voltage, and measured current
        self.write(":FORM:ELEM:SENS VOLT,CURR")

    def get_trace_data(self, offset='CURR', size=1):
        # get the whole data in buffer
        return self.ask(f"TRACe{self.ch}:data?").strip()

    def get_one_shot(self):
        return self.ask(f":meas?").strip().split(',')

    def get_trace_data_recent(self, offset='CURR', size=1):
        return self.ask(f"TRAC{self.ch}:data? {offset}")
    
    def get_average_trace_data(self):
        self.write(f"TRACe{self.ch}:STAT:FORM MEAN")
        return float(self.ask(f"TRAC{self.ch}:stat:data?").strip())
    
    def get_all_buffer_data(self):
        return self.ask("Measure?").strip().split(',')
        
    def get_trigger_state(self):
        state = self.ask(":STAT:OPER:COND?").strip()
        if state == '1170':
            return 'IDLE'
        elif state == '1152' or state == '1154':
            # 1152 means source trigger is running
            # 1154 means acquire trigger is running
            return 'RUNNING'
        else:
            return 'Error'

    def abort(self):
        self.write(f"Abort (@{self.ch})")
    
    def shutdown(self):
        """ Ensures that the current or voltage is turned to zero
        and disables the output. """
        log.info("Shutting down %s.", self.name)
        if self.source_mode == 'current':
            self.ramp_to_current(0.0)
        else:
            self.ramp_to_voltage(0.0)
        #self.stop_buffer()
        self.reset_buffer()
        self.disable_source()
    
# User designed functions follows

    def wait_till_done(self, wait_time=10):
        """
        Wait until the measurement is completed.

            waits indefinitely until measurement is completed

        Returns
        -------
        int
            1: if the measurement has successfully finished
            0: if there is some error
        """
        original_timeout = self.inst.timeout
        self.inst.timeout = None
        ans = self.ask(f":IDLE{self.ch}:ACQ?")
        self.inst.timeout = original_timeout
        return ans
            
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
        self.setNPLC(0.01)
        self.set_simple_loop(1,pulse_width)
        self.source_voltage = voltage
        self.start_buffer()
        self.wait_till_done(1)
        return map(float, self.get_trace_data())
    
    def readReRAM(self):
        self.start_buffer()
        self.wait_till_done()
        return float(self.get_average_trace_data())
    
    def read_resistance_states(self,voltagePulses): #list of (voltage,pulse_width) tuples
        # Assuming function generator is connected and SMU is disconnected
        Currents = []
        for vp in voltagePulses:
            if vp[0] != 0:
                self.apply_switch_pulse(*vp)
                self.setNPLC()
                self.set_simple_loop(self.avg,0)
                self.source_voltage = self.readV
                self.start_buffer()
                self.wait_till_done()
                c = self.get_average_trace_data()
                if c == 0:
                    c = 1e-12
            else:
                c = 1e-12
            Currents.append(c)
        return Currents

#  misc commands
    def set_power_line_frequency(self,freq):
        # set the power line frequency to 50 or 60 Hz
        assert freq in (50,60)
        self.write(f":SYST:LFR {freq}")

    def enable_beep(self, status = 'ON'):
        if status == True:
            status = 'ON'
        elif status == False:
            status = 'OFF'
        assert status.upper() in (True,False)
        self.write(f":SYST:BEEP:STAT {status}")

    def set_date_time(self, date):
        # get date and time in datetime format
        setDate = date.strftime("%Y,%m,%d")
        setTime = date.strftime("%H,%M,%S")
        self.write(f":SYST:DATE {setDate}")
        self.write(f":SYST:TIME {setTime}")

    def perform_self_test(self):
        result = self.ask("*TST?")
        if result == 0:
            return "PASS"
        else:
            return "FAIL"

    def perform_self_calibration(self):
        result = self.ask("*CAL?")
        if result == 0:
            return "PASS"
        else:
            return "FAIL"

    def set_startup_task(self,program_name):
        self.write(f":PROG:PON:COPY '{program_name}'")
        self.write(f":PROG:PON:RUN ON")

    def clear_error_buffer(self):
        errors = self.ask(":SYST:ERR:ALL?")

    def get_timestamp(self):
        timestamp = self.ask(":SYST:TIME:TIM:COUN?")
        return timestamp

    def clear_timestamp(self):
        self.write(":SYST:TIME:TIM:COUN:RES")

    def autoClear_timestamp(self, status = 'ON'):
        # automatic clear of timestamp when initiate action occurs
        if status == True:
            status = 'ON'
        elif status == False:
            status = 'OFF'
        assert status.upper() in ('ON', 'OFF')
        self.write(f":SYST:TIME:TIM:COUN:RES:AUTO {status}")

    def enable_remote_display(self, status = 'ON'):
        if status == True:
            status = 'ON'
        elif status == False:
            status = 'OFF'
        assert status.upper() in ('ON','OFF')
        self.write(f":DISP:ENAB {status}")

    def set_continuous_trigger(self, status):
        if status == True:
            status = 'ON'
        elif status == False:
            status = 'OFF'
        assert status.upper() in ('ON','OFF')
        self.write(f"SOUR{self.ch}:FUNC:TRIG:CONT {status}")

    def source_sweep_mode(self, mode):
        # set voltage to sweep mode, list mode or fixed mode upon triggered.
        if mode.lower() == 'swe':
            mode = 'sweep'
        elif mode.lower() == 'fix':
            mode = 'fixed'
        assert mode.lower() in ('sweep', 'list', 'fixed')
        self.write(f':SOUR{self.ch}:{self.source_mode}:MODE {mode}')

    def set_output_level(self,output):
        # set current or voltage output level.
        # Can be either a floating point or 'MIN', 'MAX' or 'DEFault'
        # default is 0
        if isinstance(output,str):
            output = output.lower()
            if output == 'minimum':
                output = 'min'
            elif output == 'maximum':
                output = 'max'
            elif output == 'default':
                output = 'def'
        else:
            assert isinstance(output, (int,float)), 'invalid type'
            if self.source_mode == 'Voltage':
                assert -200 > output > 200, 'Voltage out of range'
            elif self.sense_mode == 'Current':
                assert -1 > output > 1, 'Current out of range'
        self.write(f"SOUR{self.ch}:{self.source_mode}:TRIG {output}")

    def configure_pulse(self, delay_time=2e-5, baseV=0,pw1 = 0.1, pw2 = 0.2):
        self.write(f"SOUR{self.ch}:FUNC:SHAP PULS")
        self.write(f"SOUR{self.ch}:VOLT:MODE FIX")
        self.write(f"SOUR{self.ch}:PULS:DEL {delay_time}")
        self.write(f"SOUR{self.ch}:VOLT {baseV}")

        pulse_delay = self.pulse_delay  # set a default 20 µs pulse delay
        self.write(f"SOUR{self.ch}:PULS:DEL {pulse_delay}")
        self.write(f"TRIG{self.ch}:TRAN:DEL 0")
        if pw1 + pulse_delay < 0.02: # acquire period should be more than 1/line frequency
            self.acq_trigger_period1 = 0.02 + pulse_delay
        else:
            self.acq_trigger_period1 = pw1 + pulse_delay
        if pw2 + pulse_delay < 0.02:
            self.acq_trigger_period2 = 0.02 + pulse_delay
        else:
            self.acq_trigger_period2 = pw2 + pulse_delay
        self.source_trigger_period1 = (self.avg + 1) * self.acq_trigger_period1
        self.source_trigger_period2 = (self.avg + 1) * self.acq_trigger_period2
        # TODO: check if the following settings will be preserved when buffer is cleared
        self.write(f":trig{self.ch}:sour tim")
        self.write(":trig:tran:coun 1")
        self.write(f":trig{self.ch}:acq:coun {self.avg + 1}")  # 1 set for write current, avg sets for read current
        self.write(":FORM:ELEM:SENS VOLT,CURR,TIME,SOUR")

    def set_pulse1(self, pulse_width, amplitude):
        pulse_delay = self.pulse_delay  # set a default 20 µs pulse delay
        self.clear_buffer(2)
        self.write(f"SOUR{self.ch}:VOLT:TRIG {amplitude}")
        self.write(f"SOUR{self.ch}:PULS:WIDT {pulse_width}")
        self.write(f"TRIG{self.ch}:ACQ:DEL {pulse_delay + 0.5 * pulse_width}")
        self.write(f":trig{self.ch}:tran:tim {self.source_trigger_period1}")
        self.write(f":trig{self.ch}:acq:tim {self.acq_trigger_period1}")

    def set_pulse2(self, pulse_width, amplitude):
        pulse_delay = self.pulse_delay
        self.clear_buffer(2)
        self.write(f"SOUR{self.ch}:VOLT:TRIG {amplitude}")
        self.write(f"SOUR{self.ch}:PULS:WIDT {pulse_width}")
        self.write(f"TRIG{self.ch}:ACQ:DEL {pulse_delay + 0.5 * pulse_width}")
        self.write(f":trig{self.ch}:tran:tim {self.source_trigger_period2}")
        self.write(f":trig{self.ch}:acq:tim {self.acq_trigger_period2}")

    def configure_DC_sweep(self, delay_time, minV, maxV, direction, npoints, ncycles):
        pass

    def configure_pulse_sweep(self, voltages, baseV, pulse_width):
        #TODO: if resistance variation is high enough, then acqusition period can be shorter than 1/line frequency
        #TODO: currently, the value returned by actual voltage applied has some fraction from read voltage as well.
        #TODO: so find out if the actual pulse voltage can be back calculated if you know the fraction.
        pulse_delay = self.pulse_delay
        if pulse_width < 0.02:  # acqusition period should be greater than 1/(line frequency)
            acq_trigger_period = 0.02 + pulse_delay
        else:
            acq_trigger_period = pulse_width + pulse_delay
        source_trigger_period = (self.avg + 1) * acq_trigger_period
        self.write(f"SOUR{self.ch}:FUNC:SHAP PULS")
        self.write(f"SOUR{self.ch}:VOLT:MODE LIST")
        self.write(f"SOUR{self.ch}:LIST:VOLT {voltages}")
        self.write(f"SOUR{self.ch}:VOLT {baseV}")
        pulse_delay = 2e-5 # set a default 20 µs pulse delay
        self.write(f"SOUR{self.ch}:PULS:DEL {pulse_delay}")
        self.write(f"SOUR{self.ch}:PULS:WIDT {pulse_width}")
        self.write(f"TRIG{self.ch}:TRAN:DEL 0")
        self.write(f"TRIG{self.ch}:ACQ:DEL {pulse_delay+2e-5}")
        #self.write(f"TRIG{self.ch}:ACQ:DEL {pulse_delay + 0.5 * pulse_width}")
        nPoints = int(float(self.ask(f":SOUR{self.ch}:LIST:{self.source_mode}:POIN?").strip()))
        self.write(f":trig{self.ch}:sour tim")
        # set source trigger conditions
        self.write(f":trig{self.ch}:tran:tim {source_trigger_period}")
        self.write(f":trig:tran:coun {nPoints}")
        # set acquire trigger conditions
        self.write(f":trig{self.ch}:acq:tim {acq_trigger_period}")
        self.write(f":trig{self.ch}:acq:coun {(self.avg+1) * nPoints}")  # 1 set for write current, avg sets for read current
        measurement_time = self.get_measurement_time() #+ 2e-5  # assume 20 µs overhead, need to adjust appropriately
        self.write(":FORM:ELEM:SENS VOLT,CURR,TIME,SOUR")

    def configure_pulse_trigger_sweep(self, voltages, npulses, pulse_width, baseV = 0):
        pulse_delay = 0  # set a default 0 s pulse delay
        # disable acquire trigger
        self.write(f"trig{self.ch}:acq:tout: 0")
        # set
        self.write(f"SOUR{self.ch}:FUNC:SHAP PULS")
        self.write(f"SOUR{self.ch}:VOLT:MODE LIST")
        self.write(f"SOUR{self.ch}:LIST:VOLT {voltages}")
        self.write(f"SOUR{self.ch}:VOLT {baseV}")
        self.write(f"SOUR{self.ch}:PULS:DEL {pulse_delay}")
        self.write(f"SOUR{self.ch}:PULS:WIDT {pulse_width}")
        self.write(f"TRIG{self.ch}:TRAN:DEL 0")
        nPoints = int(float(self.ask(f":SOUR{self.ch}:LIST:{self.source_mode}:POIN?").strip()))
        self.write(f":trig{self.ch}:sour tim")
        # set source trigger conditions
        self.write(f":trig{self.ch}:tran:tim {source_trigger_period}")
        self.write(f":trig:tran:coun {nPoints}")

    def configure_pulse_trigger_high_res_acquire_sweep(self, voltages, npulses, pulse_width, baseV = 0):
        pulse_delay = 2e-5
        source_trigger_period = pulse_width + pulse_delay
        npoints = len(voltages)
        if source_trigger_period*npoints > 2: # max only 2 seconds
            if pulse_width*npoints <= 2: # check if total time is less than 2 seconds if pulse_delay is set to zero
                source_trigger_period = pulse_width
                pulse_delay = 0
                print("Setting pulse delay to 0")
            else: # else decrease number of points
                npoints = int(2/source_trigger_period)
                voltages = voltages[:npoints]
                print("Trimming number of voltage points")
        acq_trigger_period = 2e-5
        acq_points = ceil(npoints*source_trigger_period/acq_trigger_period)
        self.write(f"SOUR{self.ch}:FUNC:SHAP PULS")
        self.write(f"SOUR{self.ch}:VOLT:MODE LIST")
        self.write(f"SOUR{self.ch}:LIST:VOLT {voltages}")
        self.write(f"SOUR{self.ch}:VOLT {baseV}")
        self.write(f"SOUR{self.ch}:PULS:DEL {pulse_delay}")
        self.write(f"SOUR{self.ch}:PULS:WIDT {pulse_width}")
        self.write(f"TRIG{self.ch}:TRAN:DEL 0")
        self.write(f"TRIG{self.ch}:ACQ:DEL 0")
        nPoints = int(float(self.ask(f":SOUR{self.ch}:LIST:{self.source_mode}:POIN?").strip()))
        self.write(f":trig{self.ch}:sour tim")
        # set source trigger conditions
        self.write(f":trig{self.ch}:tran:tim {source_trigger_period}")
        self.write(f":trig:tran:coun {nPoints}")
        # set acquire trigger conditions
        self.write(f":trig{self.ch}:acq:tim {acq_trigger_period}")
        self.write(
            f":trig{self.ch}:acq:coun {acq_points}")  # 1 set for write current, avg sets for read current
        measurement_time = self.get_measurement_time()  # + 2e-5  # assume 20 µs overhead, need to adjust appropriately
        self.write(":FORM:ELEM:SENS VOLT,CURR,TIME,SOUR")

    def set_low_terminal_state(self, state):
        if state.lower() == 'float':
            state = 'flo'
        elif state.llwer() == 'ground':
            state = 'gro'
        assert state.lower() in ('flo','gro'), "low terminal state can only be 'float' or 'ground'"


#  misc commands
    def set_power_line_frequency(self,freq):
        # set the power line frequency to 50 or 60 Hz
        assert freq in (50,60)
        self.write(f":SYST:LFR {freq}")

    def enable_beep(self, status = 'ON'):
        if status == True:
            status = 'ON'
        elif status == False:
            status = 'OFF'
        assert status.upper() in (True,False)
        self.write(f":SYST:BEEP:STAT {status}")

    def set_date_time(self, date):
        # get date and time in datetime format
        setDate = date.strftime("%Y,%m,%d")
        setTime = date.strftime("%H,%M,%S")
        self.write(f":SYST:DATE {setDate}")
        self.write(f":SYST:TIME {setTime}")

    def perform_self_test(self):
        result = self.ask("*TST?")
        if result == 0:
            return "PASS"
        else:
            return "FAIL"

    def perform_self_calibration(self):
        result = self.ask("*CAL?")
        if result == 0:
            return "PASS"
        else:
            return "FAIL"

    def set_startup_task(self,program_name):
        self.write(f":PROG:PON:COPY '{program_name}'")
        self.write(":PROG:PON:RUN ON")

    def clear_error_buffer(self):
        errors = self.ask(":SYST:ERR:ALL?")
        return errors

    def get_timestamp(self):
        timestamp = self.ask(":SYST:TIME:TIM:COUN?")
        return timestamp

    def clear_timestamp(self):
        self.write(":SYST:TIME:TIM:COUN:RES")

    def autoClear_timestamp(self, status = 'ON'):
        # automatic clear of timestamp when initiate action occurs
        if status == True:
            status = 'ON'
        elif status == False:
            status = 'OFF'
        assert status.upper() in ('ON', 'OFF')
        self.write(f":SYST:TIME:TIM:COUN:RES:AUTO {status}")

    def enable_remote_display(self, status = 'ON'):
        if status == True:
            status = 'ON'
        elif status == False:
            status = 'OFF'
        assert status.upper() in ('ON','OFF')
        self.write(f":DISP:ENAB {status}")

    def set_continuous_trigger(self, status):
        if status == True:
            status = 'ON'
        elif status == False:
            status = 'OFF'
        assert status.upper() in ('ON','OFF')
        self.write(f"SOUR{self.ch}:FUNC:TRIG:CONT {status}")

    def set_output_level(self,output):
        # set current or voltage output level.
        # Can be either a floating point or 'MIN', 'MAX' or 'DEFault'
        # default is 0
        if isinstance(output,str):
            output = output.lower()
            if output == 'minimum':
                output = 'min'
            elif output == 'maximum':
                output = 'max'
            elif output == 'default':
                output = 'def'
        else:
            assert isinstance(output, (int,float)), 'invalid type'
            if self.source_mode == 'Voltage':
                assert -200 > output > 200, 'Voltage out of range'
            elif self.sense_mode == 'Current':
                assert -1 > output > 1, 'Current out of range'
        self.write(f"SOUR{self.ch}:{self.source_mode}:TRIG {output}")

    def trigger_pulse(self):
        self.enable_source()  # start outputting pulse base value
        self.trigger() # perform the specified pulse output and measurement

    def configure_DC_sweep(self, delay_time, minV, maxV, direction, npoints, ncycles):
        pass

    def set_low_terminal_state(self, state):
        if state.lower() == 'float':
            state = 'flo'
        elif state.llwer() == 'ground':
            state = 'gro'
        assert state.lower() in ('flo','gro'), "low terminal state can only be 'float' or 'ground'"

    def overVoltage_protection(self, status = False):
        if status == True:
            status = 'on'
        elif status == False:
            status = 'off'
        assert status.lower() in ('on','off',1,0), "incorrect status command sent for over voltage protection"
        self.write(f":OUTP{self.ch}:PROT {status}")

    def set_transient_speed(self, speed = 'normal'):
        # normal - gives clean output
        # fast - sets the fast mode to obtain high slew rate of output
        if speed.lower() == 'norm':
            speed = 'normal'
        assert status.lower() in ('normal','fast'), "incorrect parameter sent to set_transient_speed"
        self.write(f"sour{self.ch}:{self.source_mode}:tran:spe {speed}")

    def get_measurement_time(self):
        t = self.ask(f":SENS{self.ch}:{self.source_mode}:DC:APER?").strip()
        return float(t)

    def set_measurement_time(self,t):
        if isinstance(t,float) or isinstance(t,int):
            assert 8e-6 <= t <= 2, "measurement time should lie between 8 µs and 2 s"
            self.write(f"SENS{self.ch}:{self.source_mode}:")