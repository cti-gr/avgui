from os.path import expanduser

import PySide
from PySide import QtCore
import sys, subprocess

global avgmonitor
global DBFILEPATH
global daemonMonitor

global PYSIDE_VERSION
global QT_VERSION
global PYTHON_VERSION

def init_config(devmode):
	global daemonMonitor
	global avgmonitor
	global DBFILEPATH
	global PYSIDE_VERSION
	global QT_VERSION
	global PYTHON_VERSION
	
	
	
	PYTHON_VERSION=sys.version
	PYSIDE_VERSION=PySide.__version__
	QT_VERSION=PySide.QtCore.__version__
	DBFILENAME = "avghistory.sqlite"
	homedir = expanduser("~")
	if devmode:
		DBFILEPATH = DBFILENAME
	else:
		DBFILEPATH = homedir + "/.avgui/" + DBFILENAME
		
	
	daemonMonitor = subprocess.check_output(["pwd"]).decode("utf").rstrip() + "/" + "avgmonitor.py"
	#avgmonitor = daemonPath + "/" + avgmonitor
