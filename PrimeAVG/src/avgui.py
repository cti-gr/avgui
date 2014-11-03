#!/usr/bin/python3.4
import gc
from PySide.QtGui import QApplication, QMessageBox
import sys
import setupGui
import signalManager
import utilities
import config
import os
import signal
import subprocess
import logging
import conf.language.lang as langmodule


#import avg_icons_rc

# Should incorporate code to include AVG installation check

def avgstopped_handler(signum, frame):
	QMessageBox.critical(None, langmodule.attention, langmodule.avgStopped, 
				QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
	app.exit(1)

class theApplication(object):

	def __init__(self):
		self.theWindow = setupGui.mainWindow()
		self.theInitializer =  signalManager.manager(self.theWindow)   
		    

if __name__=="__main__":
	
	app = QApplication(sys.argv)

	if len(sys.argv) > 2:
		print("Too many arguments - Exiting")
		sys.exit(1)
	elif len(sys.argv) == 2:
		if sys.argv[1] != "--debug":
			print("Unknown argument - Exiting")
			sys.exit(1)
		else:
			config.init_config(True)
	else:
		config.init_config()

	langmodule.setuplang()

	if not utilities.isAVGDRunning():
		QMessageBox.critical(None, langmodule.attention, langmodule.avgnotrunning, 
				QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
		#print(langmodule.avgnotrunning)
		exit(1)

	signal.signal(signal.SIGALRM, avgstopped_handler)
	mainpid = os.getpid()

	theApp = theApplication()
	theApp.theWindow.show()
	gc.enable()
	
	try:
		subprocess.call([config.daemonMonitor, "--start", str(mainpid)])
	except Exception as exc:
		QMessageBox.critical(None, langmodule.attention, langmodule.failedToStartDaemon, 
				QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)

	app.exec_()
# to add finalization operation, e.g. closing the cursor






