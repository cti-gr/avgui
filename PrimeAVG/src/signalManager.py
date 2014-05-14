#!/usr/lib/python3.3
from PySide.QtGui import QMessageBox, QFileDialog, QDialog, QPlainTextEdit, QGridLayout, QApplication, QCursor, QTableWidgetItem
from PySide.QtCore import QObject, QCoreApplication, QProcess, QThreadPool, QDate, QSize, QMutex, QMutexLocker, QTimer, Qt
from datetime import datetime, date, time
import utilities
from io import open
from os.path import expanduser
import subprocess, sys, time, weakref, tempfile
import setupGui
import gc, re
import getpass
import conf.language.lang as langmodule
from configparser import SafeConfigParser
import os, config
import hashlib
from uuid import getnode
########################################################################################################
# IMPORTANT NOTICE!!!! TO CHECK CLASS-LEVEL PARAMETERS!!!!
########################################################################################################


global scanPath
global scanParameters
global abnormalTermination
global homeDir
global scanReportFolder
global scanReportFile
global scanReportPath
global infectionsList
global infectedFiles
mutexTermination = QMutex()

class manager(QObject):

	_scanParams = []
	_scanRunning = 0
	# _storageEnabled = 0
	#_folderStorage = None
	#_fileStorage = None
	#_storagePath = None
	_resultsToPrint = []

	

	def __init__(self, theMainWindow, parent=None):
		global abnormalTermination
		global scanPath
		global homeDir
		global scanReportPath
		global scanReportFolder
		global infectionsList
		global infectedFiles
		super(manager, self).__init__(parent)
		
		# Opening Configuration File
		self.confileName = os.path.expanduser("~") + "/.avgui/config.ini"
		self.configparser = SafeConfigParser()
		self.configparser.read(self.confileName)
		self.mutexPrint = QMutex()
		
		self._theMainWindow = theMainWindow
		self.setupConnections(self._theMainWindow)
		self.theTimer = QTimer()
		abnormalTermination = 0
		self.scanReportStorageEnabled = 0
		scanReportPath = None
		scanReportFolder = None
		scanPath = None
		homeDir = expanduser("~")
				
	def setupConnections(self, theMainWindow):
		# Main Window
		self._theMainWindow.btnHistory.clicked.connect(self.emitHistory)
		self._theMainWindow.btnScan.clicked.connect(self.emitScan)
		self._theMainWindow.btnUpdate.clicked.connect(self.emitUpdate)
		self._theMainWindow.sigMainSent.connect(self.handleMainWindowEmits)
		self._theMainWindow.btnStatus.clicked.connect(self.showStatus)
		self._theMainWindow.comLangsel.currentIndexChanged.connect(self.setLanguage)
		
		# Scan Dialog
		self._theMainWindow.theScan.btnSelectF.clicked.connect(self.selectWhatToScan)
		self._theMainWindow.theScan.btnBeginScan.clicked.connect(self.beginScan)
		self._theMainWindow.theScan.btnScanSettings.clicked.connect(self.setScanSettings)
		self._theMainWindow.theScan.sigCleanScanDialog.connect(self.cleanUpScanSettings)
		
		# Scan Select Dialog
		# self._theMainWindow.theScan.theSelect.sigSelectType.connect(self.handleSelectScanTypeEmits)
		self._theMainWindow.theScan.theSelect.radioFile.clicked.connect(self.emitFileSelected)
		self._theMainWindow.theScan.theSelect.radioFolder.clicked.connect(self.emitFolderSelected)
		
		# Scan Settings Dialog
		self._theMainWindow.theScan.theScanSettings.btnOK.clicked.connect(self.getScanSettings)
		self._theMainWindow.theScan.theScanSettings.chkbFileStore.stateChanged.connect(self.enableStorage)
		self._theMainWindow.theScan.theScanSettings.btnSelectFolder.clicked.connect(self.selectScanReportFolder)
		
		# Scan Progress Dialog
		self._theMainWindow.theScan.theScanProgress.btnExitScan.clicked.connect(self.terminateScan)
		self._theMainWindow.theScan.theScanProgress.sigCloseEvent.connect(self.terminateScan)
		
		# Scan History Dialog
		self._theMainWindow.theHistory.btnExecute.clicked.connect(self.execSearch)
		self._theMainWindow.theHistory.btnHistoryDB.clicked.connect(self.retrieveDBHistory)
		self._theMainWindow.theHistory.theResults.btnExtractTxt.clicked.connect(self.extractToText)
		self._theMainWindow.theHistory.theResults.sigCloseEvent.connect(self.clearResults)

		# Update Dialog
		self._theMainWindow.theUpdate.btnUpdateCheck.clicked.connect(self.checkUpdates)
		self._theMainWindow.theUpdate.btnUpdate.clicked.connect(self.performUpdate)		   
		self._theMainWindow.theUpdate.btnUpdateSet.clicked.connect(self.setUpdateSettings)
		self._theMainWindow.theUpdate.theUpdateSettings.btnOK.clicked.connect(self.setUpdateSettings)
		self._theMainWindow.theUpdate.theUpdateSettings.btnCancel.clicked.connect(self.setUpdateSettings)
		
				
	def emitScan(self):
		self._theMainWindow.sigMainSent.emit("SCAN")
		
		
	def emitHistory(self):
		self._theMainWindow.sigMainSent.emit("HISTORY")

		
	def emitUpdate(self):
		self._theMainWindow.sigMainSent.emit("UPDATE")
		
		
	def handleMainWindowEmits(self, param):
		#print(param)
		if param == "SCAN":
			self._theMainWindow.theScan.clear()
			self._theMainWindow.theScan.theSelect.clear()
			self._theMainWindow.theScan.show()
		elif param == "UPDATE":
			self._theMainWindow.theUpdate.show()
		elif param == "HISTORY":
			self._theMainWindow.theHistory.show()
			# populating combo boxes
			availMal = utilities.populateMalware()
			modelMalware = utilities.malwareModel(availMal)
			self._theMainWindow.theHistory.comMalware.setModel(modelMalware)
			availDBs = utilities.populateVirusDBs()
			modelDBs = utilities.virusDBModel(availDBs)
			
			#populating date fields
			self.curDateList = date.today().isoformat().split('-')
			self.curQDate = QDate(int(self.curDateList[0]), int(self.curDateList[1]), int(self.curDateList[2]))
			self._theMainWindow.theHistory.comStartDate.setDate(self.curQDate )
			self._theMainWindow.theHistory.comEndDate.setDate(self.curQDate )
			
			self._theMainWindow.theHistory.comDatabase.setModel(modelDBs)
			
		else:
			QMessageBox.critical(None, langmodule.attention, langmodule.applicationError, 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
	
	def selectWhatToScan(self):
		self._theMainWindow.theScan.theSelect.clear()
		self._theMainWindow.theScan.theSelect.show()
		
	def emitFileSelected(self):
		global scanPath
		options = QFileDialog.DontResolveSymlinks 
		scanPath = QFileDialog.getOpenFileName(self._theMainWindow.theScan.theSelect, langmodule.chooseFileToScan, '/home', 'All files (*.*)', "",  options)[0]
		print("scan path is: " + scanPath)
		if scanPath == "":
			scanPath=None
			return
		else:
			self._theMainWindow.theScan.infoLabel.setText(langmodule.scanFileTitle)
			self._theMainWindow.theScan.fileToScanLabel.setText(str(scanPath))
		self._theMainWindow.theScan.theSelect.close()
		
	def emitFolderSelected(self):
		global scanPath
		options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
		scanPath = QFileDialog.getExistingDirectory(self._theMainWindow.theScan.theSelect, langmodule.chooseFolderToScan, '/home', options)
		print("scan path is: " + scanPath)
		if scanPath == "":
			scanPath=None
			return
		else:
			self._theMainWindow.theScan.infoLabel.setText(langmodule.scanFolderTitle)
			self._theMainWindow.theScan.fileToScanLabel.setText(str(scanPath))
		self._theMainWindow.theScan.theSelect.close()
		
############################################ Setting Language #############################################################

	def setLanguage(self):
		
		oldLang = self.configparser.get('Language', 'lang')
		print("oldLang: " + oldLang)
		newLang = self._theMainWindow.comLangsel.currentText()
		self.configparser.set('Language', 'lang', newLang)
		print("newLang: " + newLang)
		if oldLang != newLang:
			QMessageBox.information(None, langmodule.attention, langmodule.needRestartTitle, 
									QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			self.configparser.set('Language', 'lang', newLang)
			with open(self.confileName, 'r+') as confile:
				self.configparser.write(confile)


################################### Methods related to setting the Scan Settings ##########################################

	def setScanSettings(self):
		self._theMainWindow.theScan.theScanSettings.show()
		
	
	def getScanSettings(self):
		global scanParameters
		global scanReportFolder
		global scanReportFile
		global scanReportPath
		#global scanReportStorageEnabled
		
		closeWidget = True
		
		#print("Setting up scan settings...")
		scanParams = []
		# scan for specific file extensions
		if self._theMainWindow.theScan.theScanSettings.chkbIfType.isChecked():
			#print("Getting file extension")
			filesToScan = self._theMainWindow.theScan.theScanSettings.textIfType.toPlainText()
			print("files to scan BEFORE: " + str(filesToScan))
			if (utilities.checkIsExtension(filesToScan)):
				scanParams.append("--ext")
				scanParams.append(filesToScan)
				#print("files to scan AFTER: " + str(filesToScan))
				#print("Just after setting file extensions: " + str(scanParams))
		fileStorageOK = self.validateFileStorage()
		if (self.scanReportStorageEnabled == 1) & (fileStorageOK):
			scanParams.append("--report")
			scanParams.append(scanReportPath)
			#print(scanParams)
		if self._theMainWindow.theScan.theScanSettings.chkbBackUpFiles.isChecked():
			scanParams.append("--vv-backup")
		if self._theMainWindow.theScan.theScanSettings.chkbArchive.isChecked():
			scanParams.append("--arc")
		if self._theMainWindow.theScan.theScanSettings.chkbBootSec.isChecked():
			scanParams.append("--boot-sector")
		if self._theMainWindow.theScan.theScanSettings.chkbCookies.isChecked():
			scanParams.append("--coo")
		if self._theMainWindow.theScan.theScanSettings.chkbMultimedia.isChecked():
			scanParams.append("--media")
		# check which radio button is set 
			# and create parameter
		if self._theMainWindow.theScan.theScanSettings.radioDelete.isChecked():
			scanParams.append("--delete")
		elif self._theMainWindow.theScan.theScanSettings.radioHeal.isChecked():
			scanParams.append("--heal")
		elif self._theMainWindow.theScan.theScanSettings.radioVault.isChecked():
			scanParams.append("--vv-move")
		
		#print("Inside function the scanParams are: " + str(scanParams))
		scanParameters = scanParams
		#print("Just set manager._scanParams: " + str(manager._scanParams))
		#scanParameters = scanParams
		print("Just set scanParameters: " + str(scanParameters))
		
		#print("Clicked OK_1: " + "self.validateFileStorage: " + str(self.validateFileStorage()) + " scanReportStorageEnabled: " + str(self.scanReportStorageEnabled) )
		if self.scanReportStorageEnabled == 1:
			print("Level 1")
			if fileStorageOK:
				print("Level 2")
				self._theMainWindow.theScan.theScanSettings.close()
				print("just closed")
		elif self.scanReportStorageEnabled == 0:
			self._theMainWindow.theScan.theScanSettings.close()
		#print("Clicked OK_2: " + "self.validateFileStorage: " + str(self.validateFileStorage()) + " scanReportStorageEnabled: " + str(self.scanReportStorageEnabled) )
		#self._theMainWindow.theScan.theScanSettings.close()
		
	def selectScanReportFolder(self):
		global scanReportFolder
		#global scanReportStorageEnabled
		result = False
		#if self._theMainWindow.theScan.theScanSettings.chkbFileStore.isChecked():
		if self.scanReportStorageEnabled == 1:
			reportDir = ""
			while not result:
				self._theMainWindow.theScan.theScanSettings.theStoreFileDialog.ShowDirsOnly
				self._theMainWindow.theScan.theSelect.selectDialog.setFileMode(QFileDialog.Directory)
				reportDir = self._theMainWindow.theScan.theSelect.selectDialog.getExistingDirectory()
				if reportDir == "":
					return
				result = utilities.checkFolderPermissions(reportDir)
				if not result:
					QMessageBox.information(None, langmodule.attention, langmodule.noAccessRights, 
									QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
				else:					
					scanReportFolder = reportDir
					self._theMainWindow.theScan.theScanSettings.btnSelectFolder.setText(scanReportFolder)
			
	
	def validateFileStorage(self):
		global scanReportFolder
		global scanReportPath
		storagePathOK = True
		
		if (self._theMainWindow.theScan.theScanSettings.textStoreFile.toPlainText() == "") & (self.scanReportStorageEnabled == 1):
			print("here...")
			QMessageBox.information(None, langmodule.attention, langmodule.noFileNameProvided, 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			#self._theMainWindow.theScan.theScanSettings.chkbFileStore.stateChanged.disconnect()
			#self._theMainWindow.theScan.theScanSettings.chkbFileStore.setChecked(False)
			#self._theMainWindow.theScan.theScanSettings.chkbFileStore.stateChanged.connect(self.enableStorage)
			storagePathOK = False
		elif (self._theMainWindow.theScan.theScanSettings.textStoreFile.toPlainText() != "") & (self.scanReportStorageEnabled == 1):
			print("scanReportFolder is: " + str(scanReportFolder))
			scanReportFile = self._theMainWindow.theScan.theScanSettings.textStoreFile.toPlainText()
			if scanReportFolder != None:
				scanReportPath = scanReportFolder + "/" + scanReportFile
			else:
				scanReportPath = scanReportFile
			storagePathOK = True
		return storagePathOK
		#print("scanReportPath is: " + str(scanReportPath))
		
		return storagePathOK
			 
	def enableStorage(self):
		#global scanReportStorageEnabled
			   
		if self.scanReportStorageEnabled == 0:
			self._theMainWindow.theScan.theScanSettings.btnSelectFolder.setEnabled(True)
			self._theMainWindow.theScan.theScanSettings.textStoreFile.setEnabled(True)
			#print("setting to 1")
			#print("sender: " + str(self.sender().objectName()))
			self.scanReportStorageEnabled = 1
		else:
			self._theMainWindow.theScan.theScanSettings.btnSelectFolder.setDisabled(True)
			self._theMainWindow.theScan.theScanSettings.textStoreFile.setDisabled(True)
			#print("Setting to 0")
			#print("sender: " + str(self.sender().objectName()))
			self.scanReportStorageEnabled = 0

##################################################################################################
		
################################### DB Updates History ##########################################  

	def retrieveDBHistory(self):
		self.thedbHistoryWorker = utilities.dbHistoryWorker()
		#self.thedbHistoryWorker.finished.connect(self.showdbHistoryResults)
		self.thedbHistoryWorker.sigHistoryRetrieved.connect(self.showdbHistoryResults)
		self.thedbHistoryWorker.start()
		
	def showdbHistoryResults(self, theResults):
		print("theResults = " + str(theResults))
		modelHisDBRes = utilities.dbHistoryTableModel(theResults)
		self._theMainWindow.theHistory.theHistdbResults.tblViewHistoryDB.setModel(modelHisDBRes)
		self._theMainWindow.theHistory.theHistdbResults.tblViewHistoryDB.resizeColumnsToContents()
		self._theMainWindow.theHistory.theHistdbResults.show()
		self.thedbHistoryWorker.exit()
		
##################################################################################################
	
########################################## SCAN ##################################################
	def beginScan(self):
		global infectionsList
		global infectedFiles
		global infectionsList
		self._theMainWindow.theScan.theScanProgress.theShowScanResults.tableWidget.clear()
		self.isCleanScan = False
		global scanPath
		global abnormalTermination
		global scanParameters
		self.getScanSettings()
		infectedFiles = []
		infectionsList = []
		abnormalTermination = 0
		self._theMainWindow.theScan.theScanProgress.btnExitScan.setText(langmodule.terminateScan)
		#print("Scan path is: " + str(scanPath))
		if scanPath == None:
			QMessageBox.information(None, langmodule.attention, langmodule.noFilesChosen, 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			return -1
		
		# preparing to start scan in a new thread
		self.theScanWorker = utilities.scanWorker(scanPath, scanParameters)
		#self.theScanWorker.finished.connect(self.onScanFinish)
		self.theScanWorker.sigWriteScan.connect(self.printToWidget)
		self.theScanWorker.sigScanTerminated.connect(self.onScanFinish)
		
		self._theMainWindow.theScan.theScanProgress.textScanProg.clear()
		self._theMainWindow.theScan.theScanProgress.show()
		self.theScanWorker.start()
			
		#preparing to store scan event in a new thread
		self.theSQLITEWorker = utilities.sqliteWorker()
		self.theSQLITEWorker.finished.connect(self.onSQLiteFinish)

	def onSQLiteFinish(self):
		pass
		#print("Data Insertion Completed!!!!")

	def printToWidget(self, linetoappend):
		self.mutexPrint.lock()
		global infectionsList
		global infectedFiles
		lineList = (linetoappend.split())
		if ("Trojan" in lineList):
			position = lineList.index('Trojan')
			infectedFiles.append(lineList[position - 1])
			infectionsList.append(lineList[position +2])
		if ("Virus" in lineList):
			if ("identified" in lineList):
				position = lineList.index('Virus')
				infectedFiles.append(lineList[position - 1])
				infectionsList.append(lineList[position +2])
		if ("Could" in lineList):
			position = lineList.index('Could')
			infectedFiles.append(lineList[position - 1])
			infectionsList.append(lineList[position +3])
		print("Infected Files: " + str(infectedFiles))
		print("List of Infections: " + str(infectionsList))
		for i,j in langmodule.translationDict.items(): 
			linetoappend = linetoappend.replace(i,j)
		# curDateTime = datetime.now().isoformat(' ')[:19]
		self._theMainWindow.theScan.theScanProgress.textScanProg.appendPlainText(linetoappend)
		self.mutexPrint.unlock()

	def terminateScan(self):
		global infectionsList
		
		infectionsList = []
		
		if not self.isCleanScan:
			global abnormalTermination
			print("Entering terminateScan from signalManager")
			if hasattr(self, 'theScanWorker'):
				if (self.theScanWorker.getScanState() == QProcess.ProcessState.Running) | (self.theScanWorker.getScanState() == QProcess.ProcessState.Starting):
					print("Seems it was running, calling killScan method")
					self.theScanWorker.killScan()
			self.isCleanScan = True
			self._theMainWindow.theScan.theScanProgress.hide()
			manager._scanParams = []
		

	def onScanFinish(self, normalTermination):
		global infectionsList
		self.theScanWorker.sigWriteScan.disconnect()
		# infectionsList = []
		
		print("Entering onScanFinish, from signalManager, normalTermination = " + str(normalTermination))
		if hasattr(self, 'theScanWorker'):
			self.theScanWorker.exit()
			while not self.theScanWorker.wait():
				print("Waiting for scan worker to finish")
		self._theMainWindow.theScan.theScanProgress.btnExitScan.setText(langmodule.btnExitUpdateProgTitle)
		
		if hasattr(self, 'theScanWorker'):
			del self.theScanWorker
			print("The Scan Worker is being Deleted")
		else:
			print("The Scan Worker Was Already Deleted")
		try:
			lockerFinish = QMutexLocker(mutexTermination)		   
			if normalTermination=="True":
				if infectionsList:
					header1 = QTableWidgetItem("Threats")
					header2 = QTableWidgetItem(("Files"))
					self._theMainWindow.theScan.theScanProgress.theShowScanResults.tableWidget.setColumnCount(2)
					self._theMainWindow.theScan.theScanProgress.theShowScanResults.tableWidget.setRowCount(len(infectionsList))
					self._theMainWindow.theScan.theScanProgress.theShowScanResults.tableWidget.setHorizontalHeaderItem(0, header1)
					self._theMainWindow.theScan.theScanProgress.theShowScanResults.tableWidget.setHorizontalHeaderItem(1, header2)
					self._theMainWindow.theScan.theScanProgress.theShowScanResults.tableWidget.horizontalHeader().setStretchLastSection(True)
					for i in range(1, len(infectionsList) + 1):
							newItem0 = QTableWidgetItem(infectionsList[i-1])
							newItem1 = QTableWidgetItem(infectedFiles[i-1])
							print("line " + str(i) + ": " + newItem0.text())
							print("line " + str(i) + ": " + newItem1.text())
							self._theMainWindow.theScan.theScanProgress.theShowScanResults.tableWidget.setItem(i-1, 0, newItem0)
							self._theMainWindow.theScan.theScanProgress.theShowScanResults.tableWidget.setItem(i-1, 1, newItem1)
							self._theMainWindow.theScan.theScanProgress.theShowScanResults.tableWidget.resizeColumnsToContents()
					self._theMainWindow.theScan.theScanProgress.theShowScanResults.show()
				self.theSQLITEWorker.start() 
		except Exception as errmut2:
			print(str(errmut2))
			exit(-1)

		gc.collect()
	

	def cleanUpScanSettings(self):
		global scanPath
		print("Running cleanup")
		scanPath = None
		manager._scanParams = []
		
######################################################## END OF SCAN ###############################################
	
	def execSearch(self):
		flag = 0
		
		if (self._theMainWindow.theHistory.comStartDate.date() > self._theMainWindow.theHistory.comEndDate.date()):
			QMessageBox.information(None, langmodule.wrongDates1, langmodule.wrongDates2, 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			return
		
		dateFrom = self._theMainWindow.theHistory.comStartDate.date().toString('yyyy-MM-dd')
		dateTo = self._theMainWindow.theHistory.comEndDate.date().toString('yyyy-MM-dd')
		#dateFrom = self._theMainWindow.theHistory.comStartDate.date().toString('yyyy-MM-dd') + ' 23:59:59'
		#dateTo = self._theMainWindow.theHistory.comEndDate.date().toString('yyyy-MM-dd') + ' 23:59:59'
		if dateFrom == dateTo:
			dateFrom = dateFrom + ' 00:00:00'
		dateTo = dateTo + ' 23:59:59'
		
		malware = self._theMainWindow.theHistory.comMalware.currentText()
		virusDB = self._theMainWindow.theHistory.comDatabase.currentText()
		results = utilities.scanSearchQuery(dateFrom, dateTo, malware, virusDB)
		if not results:
			QMessageBox.information(None, langmodule.noResults, langmodule.noResultsCriteria, 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
		else:
			
			if (malware == '') & (virusDB == ''):
				flag = 0
			elif (malware =='') & (virusDB != ''):
				flag = 1
			elif (malware != '') & (virusDB == ''):
				flag = 2
			else:
				flag = 3
		
			nestedResults = []
			for item in results:
				tempList = []
				for i in item:
					tempList.append(str(i))
				nestedResults.append(tempList)
			manager._resultsToPrint = nestedResults
			modelResults = utilities.scanResultsTableModel(nestedResults, flag)
			# print("Nested Results: " + str(nestedResults))
			self._theMainWindow.theHistory.theResults.tblVscanResults.setModel(modelResults)
			#self._theMainWindow.theHistory.theResults.tblVscanResults.resizeColumnsToContents()
			if flag == 0:
				for i in range(3):
					self._theMainWindow.theHistory.theResults.tblVscanResults.setColumnWidth(i, 300)
			if flag == 2:
				self._theMainWindow.theHistory.theResults.tblVscanResults.setColumnWidth(0, 170)
				self._theMainWindow.theHistory.theResults.tblVscanResults.setColumnWidth(1, 180)
				self._theMainWindow.theHistory.theResults.tblVscanResults.setColumnWidth(2, 200)
									  
			if flag == 3:
				self._theMainWindow.theHistory.theResults.tblVscanResults.setColumnWidth(0, 150)
				self._theMainWindow.theHistory.theResults.tblVscanResults.setColumnWidth(1, 170)
				self._theMainWindow.theHistory.theResults.tblVscanResults.setColumnWidth(2, 190)
				self._theMainWindow.theHistory.theResults.tblVscanResults.setColumnWidth(3, 170)
			#print("flag = " + str(flag))
			#qsize = QSize(2000, 2000)
			#self._theMainWindow.theHistory.theResults.tblVscanResults.resize(qsize)
			self._theMainWindow.theHistory.theResults.show()

	def extractToText(self):
		try:
			now = datetime.now().isoformat().split('T')
			filename='scanLog_' + now[0][0:10] + '_' + now[1][0:8] + '.txt'
			flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
			folder = QFileDialog.getExistingDirectory(self._theMainWindow.theHistory.theResults, langmodule.chooseFolderToStoreText, homeDir, flags)
			print(filename)
			print(manager._resultsToPrint)
			path = folder + '/' + filename
			with open(path, 'w') as file:
				file.write(langmodule.userTitle + '\t\t\t' + langmodule.noOfResultsTitle  + '\t\t' + langmodule.scanDateTimeTitle + '\n') # linux specific newline - not portable!
				file.write("----------------------------------------------------------------------------------" + '\n') # linux specific newline - not portable!
				for inlist in manager._resultsToPrint:
					file.write(inlist[0] + '\t\t\t')
					file.write(inlist[1] + '\t\t\t\t\t')
					file.write(inlist[2] + '\n') # linux specific newline - not portable!
				file.close()	
		except IOError as error:
			print(str(error)[0:13])
			if "Permission denied" in str(error):
				QMessageBox.critical(None, langmodule.attention, langmodule.noAccessRightsInFolder, 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
		except Exception:
			QMessageBox.critical(None, langmodule.attention, langmodule.errorStoringFile, 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
	def clearResults(self):
		manager._resultsToPrint = []
		#print("Test")
	
			
################################################## UPDATES ###########################################################

################################################## Check Updates #####################################################

	def checkUpdates(self):
		self.abnormalTermination = False
		self.isCleanCheck = False
		self._theMainWindow.theUpdate.theCheckPanel.txtCheck.clear()
		self._theMainWindow.theUpdate.theCountDown.countDownLCD.display(30)
		self.theChecker = utilities.chkUpdateWorker()
		self.theChecker.sigFailed.connect(self.handleCheckTermination)
		self.theChecker.sigCheckFinished.connect(self.handleCheckTermination)
		self.theChecker.started.connect(self.beginDaemonChecker)
		self._theMainWindow.theUpdate.theCountDown.sigCloseEvent.connect(self.closeCounterWidget)
		self.theDaemonChecker = utilities.checkDaemonD()
		self.theDaemonChecker.sigDstarted.connect(self.startTimer)
		self._theMainWindow.theUpdate.theCountDown.show()
		self.theChecker.start()
		while not self.theChecker.isRunning():
			print("Waiting for checker to start")


	def beginDaemonChecker(self):
		#print("beginning daemon checker")
		self.theDaemonChecker.start()
		while not self.theDaemonChecker.isRunning():
			print("Waiting for daemon checker to start")

		
	def startTimer(self, result):
		try:
			self.theTimer.timeout.disconnect()
		except Exception as err:
			print("Error disconnecting timeout signal from timer")
		if result == 1: # process failed to start
			QMessageBox.critical(None, langmodule.attention, langmodule.restartUpdate, 
				QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			self._theMainWindow.theUpdate.theCountDown.close()
		if result == 2:
			self._theMainWindow.theUpdate.theCountDown.close()
			return # user cancelled the operation
		else: # normal process initiation
			#print("starting timer...")
			self.theTimer.timeout.connect(self.decrementLCD)
			self.theTimer.start(1000)

	def decrementLCD(self):
		currentValue = self._theMainWindow.theUpdate.theCountDown.countDownLCD.intValue()
		#print("decrementing: current value is: " + str(currentValue))
		self._theMainWindow.theUpdate.theCountDown.countDownLCD.display(currentValue - 1)
		
	def closeCounterWidget(self):
		if not self.isCleanCheck:
			print("In Close Counter Widget")
			if hasattr(self, 'theChecker'):
				print("it has!")
				self.theChecker.cleanUp()
			self.isCleanCheck = True
		else:
			pass
	
	def handleCheckTermination(self, abnormalTermination, theOutput):
		self.abnormalTermination = abnormalTermination
		if self._theMainWindow.theUpdate.theCountDown.isVisible():
			print("was visible")
			self._theMainWindow.theUpdate.theCountDown.close()
		print("inside with abnormalTermination: " + str(self.abnormalTermination))
		self.theTimer.stop()
		if hasattr(self, 'theChecker'):
			if self.theChecker.isRunning():
				self.theChecker.exit()
		if hasattr(self, 'theDaemonChecker'):
			if self.theDaemonChecker.isRunning():
				self.theDaemonChecker.exit()
			while not self.theDaemonChecker.wait():
				print("Waiting for daemon checker to exit")
		if hasattr(self, 'theDaemonChecker'):
			del self.theDaemonChecker
		if hasattr(self, 'theChecker'):
			#self.theChecker.exit()
			print("Trying to delete the checker")
			del self.theChecker
		gc.collect()
		#if hasattr(self, 'theChecker'):
		#	 print("Failed to delete the checker")
		#self._theMainWindow.theUpdate.theCountDown.close()
		if not self.abnormalTermination:
			self._theMainWindow.theUpdate.theCheckPanel.txtCheck.appendPlainText(theOutput)
			self._theMainWindow.theUpdate.theCheckPanel.show()
		gc.collect()

############################################### Run Update #######################################################

	def performUpdate(self):
		self.isClean = False
		self._theMainWindow.theUpdate.theUpdateProgress.sigCloseEvent.connect(self.closeUpdateProgress)
		self.theUpdater = utilities.updateWorker()
		self.theUpdater.sigWriteUpdate.connect(self.printToUpdateWidget)
		self.theUpdater.sigUpdateTerminated.connect(self.onUpdateFinish)
		self.theUpdater.started.connect(self.startChecker)
		self.theUpdateChecker = utilities.checkDaemonD()
		self.theUpdateChecker.sigDstarted.connect(self.showProgress)
		self.theUpdater.start()
	
	def closeUpdateProgress(self):
		print("is clean: " + str(self.isClean))
		if self.isClean:
			pass
		else:
			if hasattr(self, "theUpdater"):
				self.theUpdater.cleanUp()
			self.isClean = True

	def startChecker(self):
		self.theUpdateChecker.start()
		while not self.theUpdateChecker.isRunning():
			print("Waiting for checker to start")		 

	def showProgress(self, result):
		print("result is: " + str(result))
		self._theMainWindow.theUpdate.theUpdateProgress.textUpdateProg.clear()
		if result == 0:
			self._theMainWindow.theUpdate.theUpdateProgress.show()
			self._theMainWindow.theUpdate.theUpdateProgress.btnExit.setEnabled(False)
		else:
			pass
	
	def printToUpdateWidget(self, theInput):
		 self._theMainWindow.theUpdate.theUpdateProgress.textUpdateProg.appendPlainText(theInput)

	def onUpdateFinish(self, exitCode):
		print("EXIT CODE IS: " + str(exitCode))
		if exitCode == 1: # process did not start
			QMessageBox.critical(None, langmodule.attention, langmodule.restartUpdate, 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			if hasattr(self, 'theUpdateChecker'):
				self.theUpdateChecker.exit()
			if hasattr(self, 'theUpdater'):
				self.theUpdater.exit()
		elif exitCode == 0 | exitCode == 255: # nornal process termination
			# print(str(self.theUpdater.isRunning()))
			# signals need to be disconnected in both cases
			self.theUpdater.started.disconnect()
			self.theUpdater.sigUpdateTerminated.disconnect()
			self.theUpdater.sigWriteUpdate.disconnect()
			self.theUpdateChecker.sigDstarted.disconnect()
		if exitCode == 0:
			self._theMainWindow.theUpdate.theUpdateProgress.btnExit.setEnabled(True)
		if exitCode == 299: # abnormalTermination
			if self._theMainWindow.theUpdate.theUpdateProgress.isVisible():
				self._theMainWindow.theUpdate.theUpdateProgress.hide

		###	 cleanup code, always runs	###
		if hasattr(self, 'theUpdateChecker'):
			print("here 1")
			self.theUpdateChecker.exit()
			while self.theUpdateChecker.isRunning():
				print("here 2")
				self.theUpdateChecker.exit()
				QApplication.processEvents()
		if hasattr(self, 'theUpdateChecker'):
			del self.theUpdateChecker
		if hasattr(self, 'theUpdater'):
			while self.theUpdater.isRunning():
				print("now waiting updater...")
				self.theUpdater.exit()
				QApplication.processEvents()
		if hasattr(self, 'theUpdater'):
			print("trying to delete the updater")
			del self.theUpdater
			#if self._theMainWindow.theUpdate.theUpdateProgress.isVisible():
			#print("set it")
		gc.collect()

###################################################### Update Settings ##############################################
	
	#@QtCore.Slot()
	def setUpdateSettings(self):
		self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyMode.currentIndexChanged.connect(self.updateProxyModeSettings)			
		self._theMainWindow.theUpdate.theUpdateSettings.chkUseLogin.stateChanged.connect(self.updateProxyModeSettings)			
		self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyAuthType.currentIndexChanged.connect(self.updateProxyModeSettings)
		if self.sender().objectName() == "btnUpdateSet":
			self.getSettings()
			print("getting settings")
			if self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyMode.currentIndex() == 0:
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyName.setEnabled(False)
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyPort.setEnabled(False)
				if (self._theMainWindow.theUpdate.theUpdateSettings.chkUseLogin.isEnabled()):
					self._theMainWindow.theUpdate.theUpdateSettings.chkUseLogin.setEnabled(False)
				self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyAuthType.setEnabled(False)
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyUsername.setEnabled(False)
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyPass.setEnabled(False)
			self._theMainWindow.theUpdate.theUpdateSettings.show()
		elif self.sender().objectName() == "btnOK":
			try:
				print("test")
				self.setSettings()
				self._theMainWindow.theUpdate.theUpdateSettings.close()
			except Exception as err:
				raise err
		elif self.sender().objectName() == "btnCancel":
			self._theMainWindow.theUpdate.theUpdateSettings.close()

	def updateProxyModeSettings(self):
		if (str(self.sender().objectName())) == "cmbBoxProxyMode":
			print("sender was cmbBoxProxyMode")
			if self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyMode.currentIndex() == 0:
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyName.setEnabled(False)
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyPort.setEnabled(False)
				if (self._theMainWindow.theUpdate.theUpdateSettings.chkUseLogin.isEnabled()):
					self._theMainWindow.theUpdate.theUpdateSettings.chkUseLogin.setEnabled(False)
				self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyAuthType.setEnabled(False)
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyUsername.setEnabled(False)
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyPass.setEnabled(False)
			else:
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyName.setEnabled(True)
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyPort.setEnabled(True)
				self._theMainWindow.theUpdate.theUpdateSettings.chkUseLogin.setEnabled(True)
				if	self._theMainWindow.theUpdate.theUpdateSettings.chkUseLogin.isChecked():
					self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyAuthType.setEnabled(True)
					self._theMainWindow.theUpdate.theUpdateSettings.leditProxyUsername.setEnabled(True)
					self._theMainWindow.theUpdate.theUpdateSettings.leditProxyPass.setEnabled(True)
		elif (str(self.sender().objectName())) == "chkUseLogin":
			if self._theMainWindow.theUpdate.theUpdateSettings.chkUseLogin.isChecked():
				self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyAuthType.setEnabled(True)
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyUsername.setEnabled(True)
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyPass.setEnabled(True)
			else:
				self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyAuthType.setEnabled(False)
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyUsername.setEnabled(False)
				self._theMainWindow.theUpdate.theUpdateSettings.leditProxyPass.setEnabled(False)

	def showStatus(self):
		# !!!! NOT PORTABLE !!!! #
		statusList = subprocess.check_output(["avgctl", "--stat-all"]).decode("utf").split('\n')
		avgVersion = statusList[5].split()[-1]
		self._theMainWindow.theCurrentStatus.lblAVGtitle.setStyleSheet("QLabel { font-weight : bold; }");
		self._theMainWindow.theCurrentStatus.lblAVGvalue.setText(avgVersion)
		
		lastUpdate = statusList[8].split()[4] + "/" + statusList[8].split()[5] + "/" + statusList[8].split()[6] + ", " + statusList[8].split()[7]
		self._theMainWindow.theCurrentStatus.lblLastUpdateTitle.setStyleSheet("QLabel { font-weight : bold; }");
		self._theMainWindow.theCurrentStatus.lblLastUpdateValue.setText(lastUpdate)
		
		licence = statusList[11].split()[-1]
		licenceNo = statusList[12].split()[-1]
		self._theMainWindow.theCurrentStatus.lblLicenceTitle.setStyleSheet("QLabel { font-weight : bold; }");
		self._theMainWindow.theCurrentStatus.lblLicenceValue.setText(licence + " / " + licenceNo)
		
		aviVersion = statusList[45].split()[-1]
		self._theMainWindow.theCurrentStatus.lblDatabaseTitle.setStyleSheet("QLabel { font-weight : bold; }");
		self._theMainWindow.theCurrentStatus.lblDatabaseValue.setText(aviVersion)
		
		aviDate = statusList[46].split()[6] + "/" + statusList[46].split()[7] + "/" + statusList[46].split()[8] + ", " + statusList[46].split()[9]
		self._theMainWindow.theCurrentStatus.lblDBDateTitle.setStyleSheet("QLabel { font-weight : bold; }");
		self._theMainWindow.theCurrentStatus.lblDBDateValue.setText(aviDate)
		
		oadStatus1 = statusList[21].split('\t')[2]
		self._theMainWindow.theCurrentStatus.lblOADTitle.setStyleSheet("QLabel { font-weight : bold; }");
		if oadStatus1 == "running":
			self._theMainWindow.theCurrentStatus.lblOADValue.setStyleSheet("QLabel { color : green; }");
			oadStatus = langmodule.genericON
			# perhaps add background color
		else:
			self._theMainWindow.theCurrentStatus.lblOADValue.setStyleSheet("QLabel { color : red; }");
			oadStatus = langmodule.genericOFF
		self._theMainWindow.theCurrentStatus.lblOADValue.setText(oadStatus)
		
		schedStatus1 = statusList[22].split('\t')[2]
		self._theMainWindow.theCurrentStatus.lblSchedTitle.setStyleSheet("QLabel { font-weight : bold; }");
		if schedStatus1 == "running":
			self._theMainWindow.theCurrentStatus.lblSchedValue.setStyleSheet("QLabel { color : green; }");
			schedStatus = langmodule.genericON
			# perhaps add background color
		else:
			self._theMainWindow.theCurrentStatus.lblSchedValue.setStyleSheet("QLabel { color : red; }");
			schedStatus = langmodule.genericOFF
		self._theMainWindow.theCurrentStatus.lblSchedValue.setText(schedStatus)

		lastVirUpdate = statusList[29].split()[3] + "/" + statusList[29].split()[4] + "/" + statusList[29].split()[5] + ", " + statusList[29].split()[6]
		self._theMainWindow.theCurrentStatus.lblNextVUpdateTitle.setStyleSheet("QLabel { font-weight : bold; }");
		self._theMainWindow.theCurrentStatus.lblNextVUpdateValue.setText(lastVirUpdate)
		
		lastProgUpdate = statusList[30].split()[3] + "/" + statusList[30].split()[4] + "/" + statusList[30].split()[5] + ", " + statusList[30].split()[6]
		self._theMainWindow.theCurrentStatus.lblNextPUpdateTitle.setStyleSheet("QLabel { font-weight : bold; }");
		self._theMainWindow.theCurrentStatus.lblNextPUpdateValue.setText(lastProgUpdate)
		
		self._theMainWindow.theCurrentStatus.show()
	'''
# Check Registration
	def checkRegistration(self):
		subprocess.call(["sudo", "-k"])
		self.checkThread = utilities.checkRegistrationThread()
		self.checkThread.sigIsRegistered.connect(self.decideNext)
		try:
			self.checkThread.start()
		except Exception as genericError:
			QMessageBox.critical(None, "Προσοχή", "Πρόβλημα με την υποβολή προβλήματος: " + str(genericError.returncode), 
			 					 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)

	def decideNext(self, isRegistered):
		if isRegistered == True:
			print("Is registered, will just submit issue")
			# get and display username
			self.username = config.username
			self._theMainWindow.theProblemSubmission.lblUserValue.setText(self.username)
			# get and display Ubuntu version
			self.ubuntu_version = config.ubuntu_version
			self._theMainWindow.theProblemSubmission.lblUbuntuValue.setText(self.ubuntu_version)
			# get and display kernel version
			self.kernel_version = config.kernel_version
			self._theMainWindow.theProblemSubmission.lblKernelValue.setText(self.kernel_version)
			# get and display avgui version
			self.avgui_version = config.avgui_version
			self._theMainWindow.theProblemSubmission.lblAvguiValue.setText(self.avgui_version)
			# get avg version
			self.avg_version = config.avg_version
			self._theMainWindow.theProblemSubmission.lblAvgValue.setText(self.avgui_version) # intented BUG !!!
			self._theMainWindow.theProblemSubmission.show()
		elif isRegistered == False:
			print("Is not registered, will initiate registration process")
			self._theMainWindow.theRegistration.show()
		
			
	def submitIssue(self):
		print("Submitting issue...")
		mac_address = getnode()
		# get globalUUID for validating post
		confileName = os.getcwd() + "/conf/config.ini"
		conf = SafeConfigParser()
		conf.read(confileName)
		avguuid = conf.get('uuid', 'avguuid')
		global_uuid = hashlib.sha512()
		global_uuid.update(str(mac_address).encode("utf"))
		global_uuid.update(str(avguuid).encode("utf"))
		globalUUID = global_uuid.hexdigest()
		
		
		# get user mail and password from the form
		user_email = self._theMainWindow.theProblemSubmission.txtEmail.text()
		if user_email == "":
			QMessageBox.information(None, langmodule.attention, "Δεν έχετε εισάγει το email σας.", 
									QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			return
		user_password = self._theMainWindow.theProblemSubmission.txtPassword.text()
		if user_password == "":
			QMessageBox.information(None, langmodule.attention, langmodule.noPasswordInserted, 
									QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			return
		# hash the password
		hashed_user_password = hashlib.sha512(user_password.encode("utf"))
		# get problem description from the form
		problem_description = self._theMainWindow.theProblemSubmission.txtProbDesc.toPlainText()
		# create a temporary file from the problem description
		with tempfile.NamedTemporaryFile(prefix="txt", delete=False) as pd:
			pd.write(bytearray(problem_description.encode("utf")))
			# pd.seek(0)
			pd.close()
		self.theProblemSubmissionThread = utilities.submitIssueThread(self.username, self.ubuntu_version, self.kernel_version, self.avgui_version, self.avg_version, user_email, hashed_user_password, pd)

		self.theProblemSubmissionThread.start()
	
	def postRegistration(self):
		email_pattern = r'[^@]+@[^@]+\.[^@]+'
		email_address = self._theMainWindow.theRegistration.txtEmail.text()
		password1 = self._theMainWindow.theRegistration.txtPassword.text()
		password2 = self._theMainWindow.theRegistration.txtPassword2.text()
		if not re.match(email_pattern, email_address):
			QMessageBox.information(None, langmodule.attention, langmodule.noCorrectMailAddress, 
									QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			return
		if password1 != password2:
			QMessageBox.information(None, langmodule.attention, langmodule.passwordsDoNotMatch, 
									QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			return
		if password1 == "" or password2 == "" or email_address == "":
			QMessageBox.information(None, langmodule.attention, langmodule.mustFillInAllFields, 
									QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			return
		hashedpass = hashlib.sha512(self._theMainWindow.theRegistration.txtPassword2.text().encode("utf"))
		passdigest = hashedpass.hexdigest()
		self.theRegistrationThread = utilities.registrationThread(email_address, passdigest)
		self.theRegistrationThread.start()
	'''
	def getSettings(self):
		# Automatic Program Update
		self.autoProgUpdateOut = subprocess.check_output(["avgcfgctl", "UpdateProgram.sched.Task.Disabled"])
		self.tmp_autoProgUpdate = self.autoProgUpdateOut.decode("utf").rstrip().split("=",1)[-1].capitalize()
		if self.tmp_autoProgUpdate == "False":
			self.autoProgUpdate = True
		else:
			self.autoProgUpdate = False
		self._theMainWindow.theUpdate.theUpdateSettings.chkAutoUpdateProg.setChecked(self.autoProgUpdate)
		# Automatic Virus Database Update
		self.autoVirUpdateOut = subprocess.check_output(["avgcfgctl", "UpdateVir.sched.Task.Disabled"])
		self.tmp_autoVirUpdate = self.autoVirUpdateOut.decode("utf").rstrip().split("=",1)[-1].capitalize()
		if self.tmp_autoVirUpdate == "False":
			self.autoVirUpdate = True
		else:
			self.autoVirUpdate = False
		self._theMainWindow.theUpdate.theUpdateSettings.chkAutoUpdateVir.setChecked(self.autoVirUpdate)
		# Minimum Speed 
		self.minSpeedOut = subprocess.check_output(["avgcfgctl", "Default.update.Inet.disconnect_speed_limit"])
		self.minSpeed = int(str(self.minSpeedOut.decode("utf")).split("=",1)[-1])
		self._theMainWindow.theUpdate.theUpdateSettings.leditMinSpeed.setText(str(self.minSpeed))
		# Maximum Time
		self.maxTimeOut = subprocess.check_output(["avgcfgctl", "Default.update.Inet.disconnect_time_limit"])
		self.maxTime = int(str(self.maxTimeOut.decode("utf")).split("=",1)[-1])
		self._theMainWindow.theUpdate.theUpdateSettings.leditMaxTime.setText(str(self.maxTime))
		# Proxy Name
		self.proxyNameOut = subprocess.check_output(["avgcfgctl", "Default.update.Options.Proxy.Server"])
		self.proxyName = str(self.proxyNameOut.decode("utf")).split("=",1)[-1]
		self._theMainWindow.theUpdate.theUpdateSettings.leditProxyName.setText(str(self.proxyName))
		# Proxy Username
		self.proxyUsernameOut = subprocess.check_output(["avgcfgctl", "Default.update.Options.Proxy.Login"])
		self.proxyUsername = str(self.proxyUsernameOut.decode("utf")).split("=",1)[-1]
		self._theMainWindow.theUpdate.theUpdateSettings.leditProxyUsername.setText(str(self.proxyUsername))
		# Proxy Password
		self.proxyPassOut = subprocess.check_output(["avgcfgctl", "Default.update.Options.Proxy.Password"])
		self.proxyPass = str(self.proxyPassOut.decode("utf")).split("=",1)[-1]
		self._theMainWindow.theUpdate.theUpdateSettings.leditProxyPass.setText(str(self.proxyPass))
		# Proxy Port
		self.proxyPortOut = subprocess.check_output(["avgcfgctl", "Default.update.Options.Proxy.Port"])
		self.proxyPort = int(str(self.proxyPortOut.decode("utf")).split("=",1)[-1])
		self._theMainWindow.theUpdate.theUpdateSettings.leditProxyPort.setText(str(self.proxyPort))
		# Proxy Set up
		self.proxyModeOut = subprocess.check_output(["avgcfgctl", "Default.update.Options.Proxy.Mode"])
		self.proxyMode = int(str(self.proxyModeOut.decode("utf")).split("=",1)[-1])
		self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyMode.setCurrentIndex(self.proxyMode)
		# Proxy Auth Type
		self.proxyAuthTypeOut = subprocess.check_output(["avgcfgctl", "Default.update.Options.Proxy.AuthenticationType"])
		self.proxyAuthType = int(str(self.proxyModeOut.decode("utf")).split("=",1)[-1])
		self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyAuthType.setCurrentIndex(self.proxyAuthType)
		# Proxy Log In Required
		self.proxyLoginRequiredOut = subprocess.check_output(["avgcfgctl", "Default.update.Options.Proxy.UseLogin"])
		self.tmp_proxyLoginRequired = self.proxyLoginRequiredOut.decode("utf").rstrip().split("=",1)[-1].capitalize()
		if self.tmp_proxyLoginRequired == 'False':
			self.proxyLoginRequired = False
		else:
			self.proxyLoginRequired = True
		self._theMainWindow.theUpdate.theUpdateSettings.chkUseLogin.setChecked(self.proxyLoginRequired)

	def setSettings(self):
		self.command = ""
		# Automatic Program Update
		self.newAutoProgUpdate = self._theMainWindow.theUpdate.theUpdateSettings.chkAutoUpdateProg.isChecked()
		if (self.newAutoProgUpdate != self.autoProgUpdate):
			self.command = self.command + " UpdateProgram.sched.Task.Disabled=" + str(not self.newAutoProgUpdate)
		# Automatic Virus Database Update
		self.newAutoVirUpdate = self._theMainWindow.theUpdate.theUpdateSettings.chkAutoUpdateVir.isChecked()
		if (self.newAutoVirUpdate != self.autoVirUpdate):
			self.command = self.command + " UpdateVir.sched.Task.Disabled=" + str(not self.newAutoVirUpdate)		
		# Minimum Speed
		self.newMinSpeed = int(self._theMainWindow.theUpdate.theUpdateSettings.leditMinSpeed.text())
		if (self.newMinSpeed != self.minSpeed):
			self.command = self.command + "Default.update.Inet.disconnect_speed_limit=" + str(self.newMinSpeed)
		# Maximum Time
		self.newMaxTime = int(self._theMainWindow.theUpdate.theUpdateSettings.leditMaxTime.text())
		if (self.newMaxTime != self.maxTime):
			self.command = self.command + " Default.update.Inet.disconnect_time_limit=" + str(self.newMaxTime)
		# Proxy Name
		self.newProxyName = self._theMainWindow.theUpdate.theUpdateSettings.leditProxyName.text()
		if (self.newProxyName != self.proxyName):
			self.command = self.command + " Default.update.Options.Proxy.Server="+self.newProxyName.replace(" ", "")
		# Proxy Username
		self.newProxyUsername = self._theMainWindow.theUpdate.theUpdateSettings.leditProxyUsername.text()
		if (self.newProxyUsername != self.proxyUsername):
			self.command = self.command + " Default.update.Options.Proxy.Login=" + self.newProxyUsername
		# Proxy Password
		self.newProxyPass = self._theMainWindow.theUpdate.theUpdateSettings.leditProxyPass.text()
		if (self.newProxyPass != self.proxyPass):
			self.command = self.command + " Default.update.Options.Proxy.Password=" + self.newProxyPass
		# Proxy Port
		self.newProxyPort = int(self._theMainWindow.theUpdate.theUpdateSettings.leditProxyPort.text())
		if (self.newProxyPort != self.proxyPort):
			self.command = self.command + " Default.update.Options.Proxy.Port=" + str(self.newProxyPort)
		# Proxy Set up
		self.newProxyMode = int(self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyMode.currentIndex())
		if (self.newProxyMode != self.proxyMode):
			self.command = self.command + " Default.update.Options.Proxy.Mode=" + str(self.newProxyMode)
		# Proxy Auth Type
		self.newProxyAuthType = int(self._theMainWindow.theUpdate.theUpdateSettings.cmbBoxProxyAuthType.currentIndex())
		if (self.newProxyAuthType != self.proxyAuthType):
			self.command = self.command + " Default.update.Options.Proxy.AuthenticationType=" + str(self.newProxyAuthType)
		# Proxy Log in Required
		self.newProxyLoginRequired = self._theMainWindow.theUpdate.theUpdateSettings.chkUseLogin.isChecked()
		print(self.newProxyLoginRequired)
		print(self.proxyLoginRequired)
		if (self.newProxyLoginRequired != self.proxyLoginRequired):
			self.command = self.command + " Default.update.Options.Proxy.UseLogin=" + str(self.newProxyLoginRequired)
		
		print("command is: " + self.command)
		self.command = " ".join(self.command.split()) 
		print("new command is: " + self.command)
		if self.command != "":
			try:
				subprocess.call(["gksu", "avgcfgctl -w " + self.command])
			except Exception as err:
				print("Error setting new update settings")
				raise err
