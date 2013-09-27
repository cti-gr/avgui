#!/usr/bin/python3.3
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
#theDebugger = utilities.debugger()
#theDebugger.start()
theApp = theApplication()
theApp.theWindow.show()
gc.enable()
#gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_SAVEALL)
app.exec_()
# to add finalization operation, e.g. closing the cursor






