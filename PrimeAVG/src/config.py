from os.path import expanduser

import PySide
from PySide import QtCore
import sys

global avgmonitor
global DBFILEPATH


global PYSIDE_VERSION
global QT_VERSION
global PYTHON_VERSION

def init_config(devmode):

	global avgmonitor
	global DBFILEPATH
	global PYSIDE_VERSION
	global QT_VERSION
	global PYTHON_VERSION

	avgmonitor = "avgmonitor.py"
	PYTHON_VERSION=sys.version
	PYSIDE_VERSION=PySide.__version__
	QT_VERSION=PySide.QtCore.__version__
	DBFILENAME = "avghistory.sqlite"
	homedir = expanduser("~")
	if devmode:
		DBFILEPATH = DBFILENAME
	else:
		DBFILEPATH = homedir + "/.avgui/" + DBFILENAME

