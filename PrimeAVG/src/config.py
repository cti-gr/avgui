from os.path import expanduser
import PySide

global DBFILEPATH


def init_config(devmode):
    DBFILENAME = "avghistory.sqlite"
    global DBFILEPATH
    homedir = expanduser("~")
    if devmode:
        DBFILEPATH = DBFILENAME
    else:
        DBFILEPATH = homedir + "/.avgui/" + DBFILENAME
    