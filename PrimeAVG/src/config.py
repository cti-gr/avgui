#!/usr/bin/python3.4

from os.path import expanduser

import PySide
from PySide import QtCore
import sys, subprocess, getpass
from os.path import expanduser
import os



global homedir
global avgmonitor
global dbfilepath
global daemonMonitor
global avgdir
global pyside_version
global qt_version
global python_version
global username
global server_url
global ubuntu_version
global kernel_version
global avgui_version
global avg_version
global debug



def init_config(debugMode=False):
	global homedir	
	global daemonMonitor
	global avgmonitor
	global dbfilepath
	global pyside_version
	global qt_version
	global python_version
	global username
	global server_url
	global ubuntu_version
	global kernel_version
	global avgui_version
	global avg_version
	global debug

	
	debug = debugMode
	avg_version = subprocess.check_output(["dpkg", "-s", "avg2013flx"]).split()[21].decode("utf")
	avgui_version = subprocess.check_output(["dpkg", "-s", "avg2013flx"]).split()[21].decode("utf")
	kernel_version = subprocess.check_output(["uname", "-r"]).decode("utf").split()[0]
	ubuntu_version = subprocess.check_output(["lsb_release", "-a"]).split()[5].decode("utf")
	#server_url = 'http://httpbin.org/post'
	username = getpass.getuser()
	python_version=sys.version
	pyside_version=PySide.__version__
	qt_version=PySide.QtCore.__version__
	dbfilename = "avghistory.sqlite"
	homedir = expanduser("~")
	avgdir = homedir + "/" + ".avgui"
	if debugMode:
		dbfilepath = dbfilename
		daemonMonitor  = os.getcwd() + "/avgmonitor.py"
	else:
		dbfilepath = homedir + "/.avgui/" + dbfilename
		daemonMonitor = "/usr/share/avgui/src/avgmonitor.py"
	#daemonMonitor = subprocess.check_output(["pwd"]).decode("utf").rstrip() + "/" + "avgmonitor.py"
	print("Daemon Monitor is: " + daemonMonitor)
	print("Using database: " + str(dbfilepath))
	print("Executing with Python: " + python_version)
	print("Using PySide: " + pyside_version)
	print("Qt Framework used is: " + qt_version)
	#avgmonitor = daemonPath + "/" + avgmonitor
