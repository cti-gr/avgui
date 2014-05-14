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
	langmodule.setuplang()
	if not utilities.isAVGDRunning():
		#QMessageBox.critical(None, "Προσοχή", "To AVG δεν εκτελείται - Η εφαρμογή θα τερματίσει", 
		#		QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
		print(langmodule.avgnotrunning)
		exit(1)
	
	app = QApplication(sys.argv)

	if utilities.parseParams(sys.argv)[0] == 0:
		config.init_config()
	elif utilities.parseParams(sys.argv)[0] == 1:
		config.init_config(True)
		print("Using database: " + str(config.dbfilepath))
		# print(str(os.getpid()))
		print("Executing with Python: " + config.python_version)
		print("Using PySide: " + config.pyside_version)
		print("Qt Framework used is: " + config.qt_version)
	else:
		QMessageBox.critical(None, langmodule.attention, "Λάθος στις Παραμέτρους Εκκίνησης", 
				QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
		sys.exit(1)

	signal.signal(signal.SIGALRM, avgstopped_handler)
	mainpid = os.getpid()

	theApp = theApplication()
	theApp.theWindow.show()
	gc.enable()
	
	try:
		if config.debug:
			subprocess.call([config.daemonMonitor, "--start", str(mainpid)])
		else:
			subprocess.call(["/usr/share/avgui/src/avgmonitor.py", "--start", str(mainpid)])
	except Exception as exc:
		QMessageBox.critical(None, langmodule.attention, langmodule.failedToStartDaemon, 
				QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)

	app.exec_()
# to add finalization operation, e.g. closing the cursor






