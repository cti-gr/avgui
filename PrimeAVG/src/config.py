#!/usr/bin/python3.4

from os.path import expanduser

import PySide
from PySide import QtCore
from PySide import QtGui
import sys, subprocess, getpass
from os.path import expanduser
import os
from configparser import SafeConfigParser

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

	# need to get language outside the standard procedure (i.e. through
	# conf.lang etc to customize error message regarding problem with 
	# avg2013flx installation
	if debug:
		confile = os.getcwd() + "/conf/config.ini"
	else:		
		confile = os.path.expanduser("~") + "/.avgui/config.ini"
	configparser = SafeConfigParser()
	f = open(confile, 'r')
	configparser.read(confile)
	lang = configparser.get("Language", 'lang')
		
	if lang == "EL":
		errorShort = "Προσοχή!"
		errorLong = "Υπάρχει κάποιο πρόβλημα με την εγκατάσταση του AVG Free for Linux - Ελέγξτε αν το πρόγραμμα έχει εγκατασταθεί σωστά"
	elif lang == "EN":
		errorShort = "Attention!"
		errorLong = "There seems to be a problem with AVG Free for Linux installation - Please check whether the program has been correctly installed!"

	try:
		avg_version = subprocess.check_output(["dpkg", "-s", "avg2013flx"]).split()[21].decode("utf")
	except Exception:
		QtGui.QMessageBox.critical(None, errorShort, errorLong, 
				QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default, QtGui.QMessageBox.NoButton)
		exit(1)
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
