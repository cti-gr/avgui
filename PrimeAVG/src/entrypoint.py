#!/usr/bin/python3.3
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


#import avg_icons_rc

# Should incorporate code to include AVG installation check

class theApplication(object):

	def __init__(self):
		self.theWindow = setupGui.mainWindow()
		self.theInitializer =  signalManager.manager(self.theWindow)       

app = QApplication(sys.argv)
if not utilities.isAVGDRunning():
	QMessageBox.critical(None, "Προσοχή", "To AVG δεν εκτελείται - Η εφαρμογή θα τερματίσει", 
				QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
	exit(1)
if (len(sys.argv) > 2):
	print("Error in numner of arguments - exiting")
	exit(1)
elif (len(sys.argv) == 2): 
	if sys.argv[1]=="True":
		config.init_config(True)
	else:
		print("Unknown parameter - exiting")
		exit(1)
else:
	config.init_config(False)
print(config.DBFILEPATH)

print(str(os.getpid()))
print("Executing with Python: " + config.PYTHON_VERSION)
print("Using PySide: " + config.PYSIDE_VERSION)
print("Qt Framework used is: " + config.QT_VERSION)

def avgstopped_handler(signum, frame):
	print("fooooooooooooooooooo")
	QMessageBox.critical(None, "Προσοχή", "TΟ AVG ΣΤΑΜΑΤΗΣΕ ΝΑ ΕΚΤΕΛΕΙΤΑΙ - Η εφαρμογή θα τερματίσει", 
				QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
	app.exit(1)

signal.signal(signal.SIGALRM, avgstopped_handler)
mainpid = os.getpid()

theApp = theApplication()
theApp.theWindow.show()
gc.enable()

daemon = (subprocess.check_output(["pwd"]).decode("utf").rstrip() + "/" + config.avgmonitor)
subprocess.call([daemon, "--start", str(mainpid)])

app.exec_()
# to add finalization operation, e.g. closing the cursor






