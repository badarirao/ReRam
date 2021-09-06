from datetime import datetime
from os.path import abspath,join,exists
from os import makedirs
from copy import copy

class FakeAdapter():
    """Provides a fake adapter for debugging purposes,
    which bounces back the command so that arbitrary values 
    testing is possible.
    
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
        """ Returns the last commands given after the
        last read call.
        """
        result = copy(self._buffer)
        # Reset the buffer
        self._buffer = ""
        return result

    def write(self, command):
        """ Writes the command to a buffer, so that it can
        be read back.
        """
        self._buffer += command

    def __repr__(self):
        return "<FakeAdapter>"
    
    def reset(self):
        pass

def unique_filename(directory, prefix='DATA', suffix='', ext='csv',
                    dated_folder=False, index=True, datetimeformat="%Y-%m-%d"):
    """ Returns a unique filename based on the directory and prefix
        Note: adopted from Pymeasure Package
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
        basename = "%s%s%s.%s" % (prefix, now.strftime(datetimeformat), suffix, ext)
        filename = join(directory, basename)
    return filename