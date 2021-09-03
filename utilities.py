from datetime import datetime
from os.path import abspath,join,exists
from os import makedirs

def unique_filename(directory, prefix='DATA', suffix='', ext='csv',
                    dated_folder=False, index=True, datetimeformat="%Y-%m-%d"):
    """ Returns a unique filename based on the directory and prefix
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