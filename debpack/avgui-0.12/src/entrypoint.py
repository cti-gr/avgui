#!/usr/bin/python3.2
import gc
from PySide.QtGui import QApplication, QMessageBox
import sys
import setupGui
import signalManager
import utilities
import config


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
if (len(sys.argv) > 1):
    config.init_config(True)
else:
    config.init_config(False)
print(config.DBFILEPATH)
theApp = theApplication()
theApp.theWindow.show()

app.exec_()
# to add finalization operation, e.g. closing the cursor






