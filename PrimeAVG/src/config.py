from os.path import expanduser
import PySide, sys

global DBFILEPATH
global QT_VERSION
global PYSIDE_VERSION
global PYTHON_VERSION

def init_config(devmode):
    global QT_VERSION
    global PYSIDE_VERSION
    global PYTHON_VERSION

    DBFILENAME = "avghistory.sqlite"
    PYSIDE_VERSION = str(PySide.__version__)
    QT_VERSION = str(PySide.QtCore.__version__)
    PYTHON_VERSION = str(sys.version)
    global DBFILEPATH
    homedir = expanduser("~")
    if devmode:
        DBFILEPATH = DBFILENAME
        print("Python version: " + PYTHON_VERSION)
        print("PySide version: " + PYSIDE_VERSION)
        print("Qt Version: " + QT_VERSION)
    else:
        DBFILEPATH = homedir + "/.avgui/" + DBFILENAME
       
