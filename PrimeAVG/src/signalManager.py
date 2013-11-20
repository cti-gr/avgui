#!/usr/lib/python3.3
from PySide.QtGui import QMessageBox, QFileDialog, QDialog, QPlainTextEdit, QGridLayout, QApplication
from PySide.QtCore import QObject, QCoreApplication, QProcess, QThreadPool, QDate, QSize, QMutex, QMutexLocker, QTimer
from datetime import datetime, date, time
import utilities
from io import open
from os.path import expanduser
import subprocess, sys, time, weakref
import setupGui
import gc, re
import getpass


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
global scanReportStorageEnabled
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
		global scanReportStorageEnabled
		global scanReportPath
		global scanReportFolder
		
		super(manager, self).__init__(parent)
		self._theMainWindow = theMainWindow
		self.setupConnections(self._theMainWindow)
		self.theTimer = QTimer()
		abnormalTermination = 0
		scanReportStorageEnabled = 0
		scanReportPath = None
		scanReportFolder = None
		scanPath = None
		homeDir = expanduser("~")	 
		
	def setupConnections(self, theMainWindow):
		#Main Window
		self._theMainWindow.logBtn.clicked.connect(self.emitHistory)
		self._theMainWindow.scanBtn.clicked.connect(self.emitScan)
		self._theMainWindow.updateBtn.clicked.connect(self.emitUpdate)
		self._theMainWindow.sigMainSent.connect(self.handleMainWindowEmits)
		
		#Scan Dialog
		self._theMainWindow.theScan.btnSelectF.clicked.connect(self.selectWhatToScan)
		self._theMainWindow.theScan.btnBeginScan.clicked.connect(self.beginScan)
		self._theMainWindow.theScan.btnScanSettings.clicked.connect(self.setScanSettings)
		
		#Scan Select Dialog
		#self._theMainWindow.theScan.theSelect.sigSelectType.connect(self.handleSelectScanTypeEmits)
		self._theMainWindow.theScan.theSelect.radioFile.clicked.connect(self.emitFileSelected)
		self._theMainWindow.theScan.theSelect.radioFolder.clicked.connect(self.emitFolderSelected)
		
		#Scan Settings Dialog
		self._theMainWindow.theScan.theScanSettings.btnOK.clicked.connect(self.getScanSettings)
		self._theMainWindow.theScan.theScanSettings.chkbFileStore.stateChanged.connect(self.enableStorage)
		self._theMainWindow.theScan.theScanSettings.btnSelectFolder.clicked.connect(self.selectScanReportFolder)
		
		#Scan Progress Dialog
		self._theMainWindow.theScan.theScanProgress.btnExitScan.clicked.connect(self.terminateScan)
		
		#Scan History Dialog
		self._theMainWindow.theHistory.btnExecute.clicked.connect(self.execSearch)
		self._theMainWindow.theHistory.btnHistoryDB.clicked.connect(self.retrieveDBHistory)
		self._theMainWindow.theHistory.theResults.btnExtractTxt.clicked.connect(self.extractToText)
		self._theMainWindow.theHistory.theResults.sigCloseEvent.connect(self.clearResults)

		#Update Dialog
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
			QMessageBox.critical(None, "Προσοχή", "Η εφαρμογή παρουσίασε σφάλμα", 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
	
	def selectWhatToScan(self):
		self._theMainWindow.theScan.theSelect.clear()
		self._theMainWindow.theScan.theSelect.show()
		
	def emitFileSelected(self):
		global scanPath
		options = QFileDialog.DontResolveSymlinks 
		scanPath = QFileDialog.getOpenFileName(self._theMainWindow.theScan.theSelect, 'Επιλογή Αρχείου προς Σάρωση', '/home', 'All files (*.*)', "",  options)[0]
		print(scanPath)
		# manager._scanType = 0
		self._theMainWindow.theScan.infoLabel.setText("Η αναζήτηση θα γίνει στο ακόλουθο αρχείο")
		self._theMainWindow.theScan.fileToScanLabel.setText(str(scanPath))
		self._theMainWindow.theScan.theSelect.close()
		
	def emitFolderSelected(self):
		global scanPath
		options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
		scanPath = QFileDialog.getExistingDirectory(self._theMainWindow.theScan.theSelect, 'Επιλογή Φακέλου προς Σάρωση', '/home', options)
		print(scanPath)
		# manager._scanType = 1
		self._theMainWindow.theScan.infoLabel.setText("Η αναζήτηση θα γίνει στον ακόλουθο φάκελο")
		#self._theMainWindow.theScan.theSelect.sigSelectType.emit("FOLDER")
		self._theMainWindow.theScan.fileToScanLabel.setText(str(scanPath))
		self._theMainWindow.theScan.theSelect.close()

################################### Methods related to setting the Scan Settings ##########################################

	def setScanSettings(self):
		self._theMainWindow.theScan.theScanSettings.show()
		
	
	def getScanSettings(self):
		global scanParameters
		global scanReportFolder
		global scanReportFile
		global scanReportPath
		global scanReportStorageEnabled
		
		closeWidget = True
		
		print("Setting up scan settings...")
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
		if (scanReportStorageEnabled == 1) & (self.validateFileStorage()):
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
		
		print("Inside function the scanParams are: " + str(scanParams))
		scanParameters = scanParams
		#print("Just set manager._scanParams: " + str(manager._scanParams))
		#scanParameters = scanParams
		print("Just set scanParameters: " + str(scanParameters))
		
		if self.validateFileStorage() & (scanReportStorageEnabled == 1):
			self._theMainWindow.theScan.theScanSettings.close()
		
	def selectScanReportFolder(self):
		global scanReportFolder
		global scanReportStorageEnabled
		result = False
		#if self._theMainWindow.theScan.theScanSettings.chkbFileStore.isChecked():
		if scanReportStorageEnabled == 1:
			reportDir = ""
			while not result:
				self._theMainWindow.theScan.theScanSettings.theStoreFileDialog.ShowDirsOnly
				self._theMainWindow.theScan.theSelect.selectDialog.setFileMode(QFileDialog.Directory)
				reportDir = self._theMainWindow.theScan.theSelect.selectDialog.getExistingDirectory()
				if reportDir == "":
					return
				result = utilities.checkFolderPermissions(reportDir)
				if not result:
					QMessageBox.information(None, "Προσοχή", "Δεν έχετε τα κατάλληλα δικαιώματα για το συγκεκριμένο directory - Παρακαλώ επιλέξτε άλλο directory", 
									QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
				else:					
					scanReportFolder = reportDir
					self._theMainWindow.theScan.theScanSettings.btnSelectFolder.setText(scanReportFolder)
			
	
	def validateFileStorage(self):
		global scanReportFolder
		global scanReportPath
		storagePathOK = False
		
		if (self._theMainWindow.theScan.theScanSettings.textStoreFile.toPlainText() == "") & (scanReportStorageEnabled == 1):
			QMessageBox.information(None, "Προσοχή", "Δεν δώσατε όνομα αρχείου αποθήκευσης αποτελεσμάτων σάρωσης", 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			self._theMainWindow.theScan.theScanSettings.chkbFileStore.setChecked(False)
		if scanReportStorageEnabled == 1:
			print("scanReportFolder is: " + str(scanReportFolder))
			scanReportFile = self._theMainWindow.theScan.theScanSettings.textStoreFile.toPlainText()
			if scanReportFolder != None:
				scanReportPath = scanReportFolder + "/" + scanReportFile
				
			else:
				scanReportPath = scanReportFile
			storagePathOK = True
		print("scanReportPath is: " + str(scanReportPath))
		
		return storagePathOK
			 
	def enableStorage(self):
		global scanReportStorageEnabled
			   
		if scanReportStorageEnabled == 0:
			self._theMainWindow.theScan.theScanSettings.btnSelectFolder.setEnabled(True)
			self._theMainWindow.theScan.theScanSettings.textStoreFile.setEnabled(True)
			scanReportStorageEnabled = 1
		else:
			self._theMainWindow.theScan.theScanSettings.btnSelectFolder.setDisabled(True)
			self._theMainWindow.theScan.theScanSettings.textStoreFile.setDisabled(True)
			scanReportStorageEnabled = 0

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
		global scanPath
		global abnormalTermination
		global scanParameters
		self.getScanSettings()
		print("global scanpath: " + str(scanPath))
		
		abnormalTermination = 0
		self._theMainWindow.theScan.theScanProgress.btnExitScan.setText("Τερματισμός Ελέγχου")
		# can only have one scan process running
		if manager._scanRunning == 0:
			manager._scanRunning = 1
			# checking if scan path is set
			if scanPath == None:
				QMessageBox.information(None, "Προσοχή", "Δεν έχουν επιλεγεί αρχεία / φάκελοι προς σάρωση", 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
				manager._scanRunning = 0
				return -1
			# preparing to start scan in a new thread
			self._theMainWindow.theScan.theScanProgress.textScanProg.clear()
			self._theMainWindow.theScan.theScanProgress.show()
			self.theScanWorker = utilities.scanWorker(scanPath, scanParameters)
			self.theScanWorker.finished.connect(self.onScanFinish)
			self.theScanWorker.sigWriteScan.connect(self.printToWidget)
			
			#preparing to store scan event in a new thread
			self.theSQLITEWorker = utilities.sqliteWorker()
			self.theSQLITEWorker.finished.connect(self.onSQLiteFinish)
			
			self.theScanWorker.sigScanTerminated.connect(self.onScanFinish)
			self.theScanWorker.start()
			
			
		else:
			QMessageBox.information(None, "Προσοχή", "Εκτελείται ήδη διαδικασία αναζήτησης κακόβουλου λογισμικού", 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
			#return -1
		
	def onSQLiteFinish(self):
		pass
		#print("Data Insertion Completed!!!!")

	def printToWidget(self, linetoappend):
		#print("Signal Received!!!!!")
		curDateTime = datetime.now().isoformat(' ')[:19]
		self._theMainWindow.theScan.theScanProgress.textScanProg.appendPlainText(linetoappend)
				
	
	def terminateScan(self):
		global abnormalTermination
		if self.theScanWorker.isRunning():
			self.theScanWorker.killScan()
			#self.theScanWorker.exit()
			manager._scanRunning = 0
			abnormalTermination = 1
		self._theMainWindow.theScan.theScanProgress.hide()
		if self.theScanWorker.isRunning():
			self.theScanWorker.exit()
		manager._scanParams = []
	
			 
	def onScanFinish(self):
		global scanReportFolder
		global scanReportFile
		global scanReportPath
		
		global abnormalTermination
		#self._theMainWindow.theHistory.theResults.tblVscanResults
		manager._scanRunning = 0
		print("Thread finished normally")
		
		self._theMainWindow.theScan.theScanProgress.btnExitScan.setText("Κλείσιμο Παραθύρου")
		if abnormalTermination == 0:
			self.theSQLITEWorker.start()
		manager._scanParams = []
		
		#scanReportFolder = None
		#scanReporPath = None
		#scanReportFile = None
		
		gc.collect()

	
	def execSearch(self):
		flag = 0
		
		if (self._theMainWindow.theHistory.comStartDate.date() > self._theMainWindow.theHistory.comEndDate.date()):
			QMessageBox.information(None, "Λάθος Ημερομηνίες", "Έχετε χρησιμοποιήσει λάθος διάταξη στις ημερομηνίες", 
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
			QMessageBox.information(None, "Κανένα Αποτέλεσμα", "Δεν βρέθηκαν αποτελέσματα με τα συγκεκριμένα κριτήρια αναζήτησης", 
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
			folder = QFileDialog.getExistingDirectory(self._theMainWindow.theHistory.theResults, "Επιλογή Φακέλου για Αποθήκευση text Αρχείου", homeDir, flags)
			print(filename)
			print(manager._resultsToPrint)
			path = folder + '/' + filename
			with open(path, 'w') as file:
				file.write("Χρήστης" + '\t\t\t' + "Αριθμός Ευρημάτων"  + '\t\t' + "Ημερομηνία και ώρα αναζήτησης" + '\n') # linux specific newline - not portable!
				file.write("----------------------------------------------------------------------------------" + '\n') # linux specific newline - not portable!
				for inlist in manager._resultsToPrint:
					file.write(inlist[0] + '\t\t\t')
					file.write(inlist[1] + '\t\t\t\t\t')
					file.write(inlist[2] + '\n') # linux specific newline - not portable!
				file.close()	
		except IOError as error:
			print(str(error)[0:13])
			if "Permission denied" in str(error):
				QMessageBox.critical(None, "Προσοχή", "Δεν έχετε δικαιώματα αποθήκευσης αρχείων στο συγκεκριμένο φάκελο", 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
		except Exception:
			QMessageBox.critical(None, "Προσοχή", "Παρουσιάστηκε σφάλμα κατά την αποθήκευση του αρχείου", 
								 QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
	def clearResults(self):
		manager._resultsToPrint = []
		#print("Test")
	
			
################################################## UPDATES ###########################################################

################################################## Check Updates #####################################################

	def checkUpdates(self):
		self.abnormalTermination = False
		self.isClean = False
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

	def closeCounterWidget(self):
		if not self.isClean:
			print("In Close Counter Widget")
			if hasattr(self, 'theChecker'):
				print("it has!")
				self.theChecker.cleanUp()
			self.isClean = True
		else:
			pass
 
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
			QMessageBox.critical(None, "Προσοχή", "Η εφαρμογή παρουσίασε σφάλμα - Παρακαλώ επανεκκινήστε την διαδικασία ελέγχου ενημερώσεων", 
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
			QMessageBox.critical(None, "Προσοχή", "Αποτυχία εκκίνησης διαδικασίας ενημέρωσης - Επανεκκινήστε την διαδικασία", 
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

		###  cleanup code, always runs	###
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
				if  self._theMainWindow.theUpdate.theUpdateSettings.chkUseLogin.isChecked():
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
