import mainWindowUI, updateDialogUI, scanDialogUI, historyDialogUI, scanSelectUI, scanSettingsUI, scanProgressUI, scanResultsUI, dbupdateResultsUI
from PySide import QtGui, QtCore
from datetime import date

class histdbResults(QtGui.QDialog, dbupdateResultsUI.Ui_dialogDBResults):
    def __init__(self, parent=None):
        super(histdbResults, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), self.close)
        
        
class scanResults(QtGui.QDialog, scanResultsUI.Ui_dialogScanResults):
    
    sigCloseEvent= QtCore.Signal()
    
    def __init__(self, parent=None):
        super(scanResults, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), self.close)
    
    def closeEvent(self, event):
       self.sigCloseEvent.emit()
    

class scanProgress(QtGui.QDialog, scanProgressUI.Ui_DiaScanProg):
    
    def __init__(self, parent=None):
        super(scanProgress, self).__init__(parent)
        self.setupUi(self)
   
       
class scanSettings(QtGui.QDialog, scanSettingsUI.Ui_scanSettingsDialog):
       
    def __init__(self, parent=None):
        super(scanSettings, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), self.close)
        self.theStoreFileDialog = QtGui.QFileDialog()
        
        
    def clear(self):
        print("Clearing the dialog")
        self.chkbBackUpFiles.setChecked(False)
        self.chkbBootSec.setChecked(False)
        self.chkbCookies.setChecked(False)
        self.chkbFileStore.setChecked(False)
        self.chkbIfType.setChecked(False)
        self.chkbMultimedia.setChecked(False)
        self.textIfType.clear()
        self.textStoreFile.clear()
        
        
        self.radioDelete.setAutoExclusive(False)
        self.radioDelete.setChecked(False)
        self.radioDelete.setAutoExclusive(True)
        
        self.radioHeal.setAutoExclusive(False)
        self.radioHeal.setChecked(False)
        self.radioHeal.setAutoExclusive(True)
        
        self.radioVault.setAutoExclusive(False)
        self.radioVault.setChecked(False)
        self.radioVault.setAutoExclusive(True)
    
class scanSelect(QtGui.QDialog, scanSelectUI.Ui_scanSelectDialog):
    sigSelectType = QtCore.Signal(str)
    sigScanType = QtCore.Signal(str, str)
    
    def __init__(self, parent=None):
        super(scanSelect, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.exitButton, QtCore.SIGNAL("clicked()"), self.close)
        self.selectDialog = QtGui.QFileDialog(self)
   
    def clear(self):
        
        self.radioFolder.setAutoExclusive(False)
        self.radioFolder.setChecked(False)
        self.radioFolder.setAutoExclusive(True)
        self.radioFile.setAutoExclusive(False)
        self.radioFile.setChecked(False)
        self.radioFile.setAutoExclusive(True)
        
class scanDialog(QtGui.QDialog, scanDialogUI.Ui_scanDialog):
    
    
    def __init__(self, parent=None):
        super(scanDialog, self).__init__(parent)
        
        
        #children windows
        self.setupUi(self)
        self.theSelect = scanSelect(self)
        self.theScanSettings = scanSettings(self)
        self.theScanProgress = scanProgress(self)
                       
        self.selectDialog = QtGui.QFileDialog(self)
        self.connect(self.exitButton, QtCore.SIGNAL("clicked()"), self.close)
   
    def clear(self):
        self.fileToScanLabel.setText("Δεν έχουν επιλεγεί αρχεία / φάκελοι")
        self.infoLabel.setText("")        
   
         

class historyDialog(QtGui.QDialog, historyDialogUI.Ui_historyDialog):
    def __init__(self, parent=None):
        super(historyDialog, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.exitButton, QtCore.SIGNAL("clicked()"), self.close)
        
        self.theResults = scanResults(self)
        self.theHistdbResults = histdbResults(self)
                

class updateDialog(QtGui.QDialog, updateDialogUI.Ui_updateDialog):
    def __init__(self, parent=None):
        super(updateDialog, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.exitButton, QtCore.SIGNAL("clicked()"), self.close)
        

class mainWindow(QtGui.QMainWindow, mainWindowUI.Ui_MainWindow):
    
    sigMainSent = QtCore.Signal(str)
    
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        
        
        self.theUpdate = updateDialog(self)
        self.theScan = scanDialog(self)
        self.theHistory = historyDialog(self)
        self.theScanProgress = scanProgress()