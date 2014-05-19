import mainWindowUI, updateDialogUI, scanDialogUI, historyDialogUI, scanSelectUI, scanSettingsUI, scanProgressUI, scanResultsUI, dbupdateResultsUI, checkPanelUI, countDownUI, updateProgressUI, problemSubmissionUI, updateSettingsUI, registrationUI, currentStatusUI, showScanResultsUI, avgavInfoUI, avguiInfoUI

import utilities
import os
from PySide import QtGui, QtCore
from datetime import date
from configparser import SafeConfigParser
import conf.language.lang as langmodule


class avguiInfo(QtGui.QDialog, avguiInfoUI.Ui_Dialog):
	def __init__(self, parent=None):
		super(avguiInfo, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), self.close)

class avgavInfo(QtGui.QDialog, avgavInfoUI.Ui_Dialog):
	def __init__(self, parent=None):
		super(avgavInfo, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), self.close)

class updateSettings(QtGui.QDialog, updateSettingsUI.Ui_dialogUpdateSettings):

	def __init__(self, parent=None):
		super(updateSettings, self).__init__(parent)
		self.setupUi(self)
		# setting input validators
		self.proxyValidator = QtGui.QIntValidator()
		self.proxyValidator.setRange(1, 10000)
		self.leditProxyPort.setValidator(self.proxyValidator)
		self.leditMinSpeed.setValidator(QtGui.QIntValidator())
		self.leditMaxTime.setValidator(QtGui.QIntValidator())
		self.cmbBoxProxyMode.insertItem(0, langmodule.noProxyTitle)	
		self.cmbBoxProxyMode.insertItem(1, langmodule.yesProxyTitle)	
		self.cmbBoxProxyMode.insertItem(2, langmodule.dependsProxyTitle)	
		self.cmbBoxProxyAuthType.insertItem(0, langmodule.autoProxyAuthTitle)	
		self.cmbBoxProxyAuthType.insertItem(1, langmodule.basicProxyAuthTitle)	
		self.cmbBoxProxyAuthType.insertItem(2, langmodule.ntlmProxyAuthTitle)	

class currentStatus(QtGui.QDialog, currentStatusUI.Ui_statusDialog):
	
	def __init__(self, parent=None):
		super(currentStatus, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), self.close)


class checkPanel(QtGui.QDialog, checkPanelUI.Ui_formCheck):
	
	def __init__(self, parent=None):
		super(checkPanel, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), self.close)

class registrationDialog(QtGui.QDialog, registrationUI.Ui_dialogRegistration):
	def __init__(self, parent=None):
		super(registrationDialog, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.btnCancel, QtCore.SIGNAL("clicked()"), self.close)

class countDown(QtGui.QDialog, countDownUI.Ui_formCountDown):
	
	sigCloseEvent = QtCore.Signal(str)
	
	def __init__(self, parent=None):
		super(countDown, self).__init__(parent)
		self.setupUi(self)
	
	def closeEvent(self, event):
		self.sigCloseEvent.emit("")

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
	

class updateProgress(QtGui.QDialog, updateProgressUI.Ui_dialogUpdateProg):
	
	sigCloseEvent = QtCore.Signal()

	def __init__(self, parent=None):
		super(updateProgress, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), self.close)

	def closeEvent(self, event):
		self.sigCloseEvent.emit()

class scanProgress(QtGui.QDialog, scanProgressUI.Ui_DiaScanProg):

	sigCloseEvent= QtCore.Signal()

	def __init__(self, parent=None):
		super(scanProgress, self).__init__(parent)
		self.setupUi(self)
		self.theShowScanResults = showScanResults(self)
		
	def closeEvent(self, event):
		self.sigCloseEvent.emit()

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
		self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), self.close)
		self.selectDialog = QtGui.QFileDialog(self)

	def clear(self):
		
		self.radioFolder.setAutoExclusive(False)
		self.radioFolder.setChecked(False)
		self.radioFolder.setAutoExclusive(True)
		self.radioFile.setAutoExclusive(False)
		self.radioFile.setChecked(False)
		self.radioFile.setAutoExclusive(True)
		
class scanDialog(QtGui.QDialog, scanDialogUI.Ui_scanDialog):
	
	sigCleanScanDialog = QtCore.Signal()
	
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
		self.fileToScanLabel.setText(langmodule.noFilesFoldersSelected)
		self.infoLabel.setText("")

	def closeEvent(self, event):
		self.sigCleanScanDialog.emit()
	
	

class historyDialog(QtGui.QDialog, historyDialogUI.Ui_historyDialog):
	def __init__(self, parent=None):
		super(historyDialog, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), self.close)
		
		self.theResults = scanResults(self)
		self.theHistdbResults = histdbResults(self)
				

class updateDialog(QtGui.QDialog, updateDialogUI.Ui_updateDialog):
	def __init__(self, parent=None):
		super(updateDialog, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), self.close)
		 
		self.theCountDown = countDown(self)
		self.theCheckPanel = checkPanel(self)
		self.theUpdateProgress = updateProgress(self)
		self.theUpdateSettings = updateSettings(self)

class showScanResults(QtGui.QDialog, showScanResultsUI.Ui_showScanResultsDialog):
	def __init__(self, parent=None):
		super(showScanResults, self).__init__(parent)
		self.setupUi(self)
		self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), self.close)
		
		
class mainWindow(QtGui.QMainWindow, mainWindowUI.Ui_MainWindow):
	
	sigMainSent = QtCore.Signal(str)
	
	def __init__(self, parent=None):
		super(mainWindow, self).__init__(parent)
		self.setupUi(self)
		
		# Opening Configuration File
		self.theUpdate = updateDialog(self)
		self.theScan = scanDialog(self)
		self.theCurrentStatus = currentStatus(self)
		self.theHistory = historyDialog(self)
		self.theavguiInfo = avguiInfo(self)
		self.theavgavInfo = avgavInfo(self)
		self.confileName = os.path.expanduser("~") + "/.avgui/config.ini"
		self.configparser = SafeConfigParser()
		self.configparser.read(self.confileName)
		lang = self.configparser.get('Language', 'lang')
		if lang == "EL":
			self.comLangsel.setCurrentIndex(0)
			self.theavguiInfo.lblCTI.setPixmap(QtGui.QPixmap(":/cti_logo_gr.png"))
		elif lang == "EN":
			self.comLangsel.setCurrentIndex(1)
			self.theavguiInfo.lblCTI.setPixmap(QtGui.QPixmap(":/cti_logo_en.png"))
		
		#self.theScanProgress = scanProgress()
		
		self.connect(self.btnExitMain, QtCore.SIGNAL("clicked()"), self.close)
		
	def closeEvent(self, event):
		utilities.finalizeApp()
		
