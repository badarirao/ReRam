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


"""
Keep Ch23 open always for 2 pole measurement.
Let CH1 to CH10 be for 10 different samples
Let CH11 to CH20 be for 10 different instruments
If CH1 is connected to sample 1.
CH11 is connected to sourcemeter
CH12 is connected to function generator

To apply pulse from function generator,
    open all -> close CH1 and CH12
    apply pulse
Next, to check resistance from sourcemeter,
    open CH12, close CH11
    check resistance
"""
import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())
from time import sleep, time
from pyvisa import ResourceManager
from pyvisa.errors import VisaIOError
from numpy import array,ndarray


def clist_validator(value, values):
    """ Provides a validator function that returns a valid clist string
    for channel commands of the Keithley 2700. Otherwise it raises a
    ValueError.

    :param value: A value to test
    :param values: A range of values (range, list, etc.)
    :raises: ValueError if the value is out of the range
    """
    # Convert value to list of strings
    if isinstance(value, str):
        clist = [value.strip(" @(),")]
    elif isinstance(value, (int, float)):
        clist = ["{:d}".format(value)]
    elif isinstance(value, (list, tuple, ndarray, range)):
        clist = ["{:d}".format(x) for x in value]
    else:
        raise ValueError("Type of value ({}) not valid".format(type(value)))

    # Pad numbers to length (if required)
    clist = [c.rjust(2, "0") for c in clist]
    clist = [c.rjust(3, "1") for c in clist]

    # Check channels against valid channels
    for c in clist:
        if int(c) not in values:
            raise ValueError(
                "Channel number {} not valid.".format(c)
            )

    # Convert list of strings to clist format
    clist = "(@{:s})".format(", ".join(clist))

    return clist


def text_length_validator(value, values):
    """ Provides a validator function that a valid string for the display
    commands of the Keithley. Raises a TypeError if value is not a string.
    If the string is too long, it is truncated to the correct length.

    :param value: A value to test
    :param values: The allowed length of the text
    """

    if not isinstance(value, str):
        raise TypeError("Value is not a string.")

    return value[:values]

class Keithley2700:
    """ Represents the Keithely 2700 Multimeter/Switch System and provides a
    high-level interface for interacting with the instrument.

    .. code-block:: python

        keithley = Keithley2700("GPIB::1")

    """
    CLIST_VALUES = list(range(101, 121))
    
    def __init__(self, adapter, **kwargs):
        if isinstance(adapter,str):
            rm = ResourceManager()
            self.inst = rm.open_resource(adapter)
            self.address = adapter
            self.ID = 'K2700'
            self.inst.query('*IDN?')
            self.name = 'Keithley 2700 multiplexer'
        else:
            raise VisaIOError(-1073807346)
        #self.check_errors()
        #self.determine_valid_channels()
        
    def ask(self,cmd):
        return self.inst.query(cmd)
    
    def write(self,cmd):
        self.inst.write(cmd)
    
    def read(self):
        return self.inst.read()
    
    def close(self):
        self.inst.close()
        
    def get_state_of_channels(self, channels):
        """ Get the open or closed state of the specified channels

        :param channels: a list of channel numbers, or single channel number
        """
        clist = clist_validator(channels, self.CLIST_VALUES)
        print(clist)
        state = self.ask("ROUTe:MULTiple:STATe? %s" % clist)

        return state

    def open_all_channels(self):
        """ Open all channels of the Keithley 2700.
        """
        self.write(":ROUTe:OPEN:ALL")

    def determine_valid_channels(self):
        """ Determine what cards are installed into the Keithley 2700
        and from that determine what channels are valid.
        """
        self.CLIST_VALUES.clear()

        self.cards = {slot: card for slot, card in enumerate(self.options, 1)}

        for slot, card in self.cards.items():

            if card == "none":
                continue
            elif card == "7709":
                """The 7709 is a 6(rows) x 8(columns) matrix card, with two
                additional switches (49 & 50) that allow row 1 and 2 to be
                connected to the DMM backplane (input and sense respectively).
                """
                channels = range(1, 51)
            else:
                log.warning(
                    "Card type %s at slot %s is not yet implemented." % (card, slot)
                )

            channels = [100 * slot + ch for ch in channels]

            self.CLIST_VALUES.extend(channels)

    def close_rows_to_columns(self, rows, columns, slot=None):
        """ Closes (connects) the channels between column(s) and row(s)
        of the 7709 connection matrix.
        Only one of the parameters `rows' or 'columns' can be "all"

        :param rows: row number or list of numbers; can also be "all"
        :param columns: column number or list of numbers; can also be "all"
        :param slot: slot number (1 or 2) of the 7709 card to be used
        """

        channels = self.channels_from_rows_columns(rows, columns, slot)
        self.closed_channels = channels

    def open_rows_to_columns(self, rows, columns, slot=None):
        """ Opens (disconnects) the channels between column(s) and row(s)
        of the 7709 connection matrix.
        Only one of the parameters `rows' or 'columns' can be "all"

        :param rows: row number or list of numbers; can also be "all"
        :param columns: column number or list of numbers; can also be "all"
        :param slot: slot number (1 or 2) of the 7709 card to be used
        """

        channels = self.channels_from_rows_columns(rows, columns, slot)
        self.open_channels = channels

    def channels_from_rows_columns(self, rows, columns, slot=None):
        """ Determine the channel numbers between column(s) and row(s) of the
        7709 connection matrix. Returns a list of channel numbers.
        Only one of the parameters `rows' or 'columns' can be "all"

        :param rows: row number or list of numbers; can also be "all"
        :param columns: column number or list of numbers; can also be "all"
        :param slot: slot number (1 or 2) of the 7709 card to be used

        """

        if slot is not None and self.cards[slot] != "7709":
            raise ValueError("No 7709 card installed in slot %g" % slot)

        if isinstance(rows, str) and isinstance(columns, str):
            raise ValueError("Only one parameter can be 'all'")
        elif isinstance(rows, str) and rows == "all":
            rows = list(range(1, 7))
        elif isinstance(columns, str) and columns == "all":
            columns = list(range(1, 9))

        if isinstance(rows, (list, tuple, ndarray)) and \
                isinstance(columns, (list, tuple, ndarray)):

            if len(rows) != len(columns):
                raise ValueError("The length of the rows and columns do not match")

            # Flatten (were necessary) the arrays
            new_rows = []
            new_columns = []
            for row, column in zip(rows, columns):
                if isinstance(row, int) and isinstance(column, int):
                    new_rows.append(row)
                    new_columns.append(column)
                elif isinstance(row, (list, tuple, ndarray)) and isinstance(column, int):
                    new_columns.extend(len(row) * [column])
                    new_rows.extend(list(row))
                elif isinstance(column, (list, tuple, ndarray)) and isinstance(row, int):
                    new_columns.extend(list(column))
                    new_rows.extend(len(column) * [row])

            rows = new_rows
            columns = new_columns

        # Determine channel number from rows and columns number.
        rows = array(rows)
        columns = array(columns)

        channels = (rows - 1) * 8 + columns

        if slot is not None:
            channels += 100 * slot

        return channels

    # system, some taken from Keithley 2400
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
        sleep(duration)
        self.beep(base_frequency * 5.0 / 4.0, duration)
        sleep(duration)
        self.beep(base_frequency * 6.0 / 4.0, duration)

    @property
    def error(self):
        """ Returns a tuple of an error code and message from a
        single error. """
        err = self.values(":system:error?")
        if len(err) < 2:
            err = self.read()  # Try reading again
        code = err[0]
        message = err[1].replace('"', '')
        return (code, message)

    def check_errors(self):
        """ Logs any system errors reported by the instrument.
        """
        code, message = self.error
        while code != 0:
            t = time()
            log.info("Keithley 2700 reported error: %d, %s" % (code, message))
            print(code, message)
            code, message = self.error
            if (time() - t) > 10:
                log.warning("Timed out for Keithley 2700 error retrieval.")

    def reset(self):
        """ Resets the instrument and clears the queue.  """
        self.write("status:queue:clear;*RST;:stat:pres;:*CLS;")

    def display_closed_channels(self):
        """ Show the presently closed channels on the display of the Keithley
        2700.
        """

        return(self.ask("ROUTe:MULTiple:CLOSe?"))
    
    def close_Channels(self,channels):
        if channels:
            clist = clist_validator(channels,self.CLIST_VALUES)
            self.write("ROUTe:MULTiple:CLOSE {}".format(clist))
            print("Closed  {}".format(clist))
    
    def open_Channels(self,channels):
        if channels:
            clist = clist_validator(channels,self.CLIST_VALUES)
            self.write("ROUTe:MULTiple:OPEN {}".format(clist))
            print("Opened  {}".format(clist))
