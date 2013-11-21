from PySide import QtGui
from PySide import QtCore
from datetime import datetime, date, time
import subprocess, re, gc
import setupGui
import sqlite3
import getpass
import config
import os, stat, gc

# To add utility that periodically checks for size of the database !!!

malwareFound = []
infectedFiles =[]
dbVersion = None
dbRelDate = None
user = None
numFilesHealed = 0
mutexResults = QtCore.QMutex()
foo = 0
procChecker = None
mutexStartCheck = QtCore.QMutex()
mutexStartUpdate = QtCore.QMutex()
abnormalTermination = False
abnormalCheckUpdatesTermination = False
abnormalUpdateTermination = False

# TO ADD function to check database existence and integrity

class checkDaemonD(QtCore.QThread):
	
	global abnormalCheckUpdatesTermination	
	
	sigDstarted = QtCore.Signal(int)
	
	def __init__(self, dName="avgupdate", parent=None):
		super(checkDaemonD, self).__init__(parent)
		self.hasStarted = False
		self.gksuHasStarted = False
		self.dName = dName
		self.retriesCnt = 0

	def run(self):
		#print("EFFECTIVE UID in Thread: " + str(os.geteuid()))
		self.retriesCnt = 0
		#print("within daemon checker")
		while True:
			self.out1 = subprocess.Popen(['ps','-C', self.dName], stdout=subprocess.PIPE)
			self.out2 = subprocess.Popen(["wc", "-l"], stdin=self.out1.stdout, stdout=subprocess.PIPE)
			self.out1IN, self.out1ERR = self.out1.communicate()
			#print("out1IN is: " + str(self.out1IN))
			#print("out1ERR is: " + str(self.out1ERR))
			self.linecount1 = self.out2.communicate()[0]
			self.outA = subprocess.Popen(['ps','-C', 'gksu'], stdout=subprocess.PIPE)
			self.outB = subprocess.Popen(["wc", "-l"], stdin=self.outA.stdout, stdout=subprocess.PIPE)
			self.linecount2 = self.outB.communicate()[0]
			if (int(self.linecount2) > 1):
				self.gksuHasStarted = True
			#self.out1.stdout.close()
			if (int(self.linecount1) > 1):
				if not self.hasStarted:
					#print("linecount is: " + str(int(self.linecount1)))
					#print("Emitting signal")
					self.sigDstarted.emit(0)
					self.hasStarted = True
					return					
			elif self.hasStarted:
				#print("EXITING!")
				#out1.kill()
				#out2.kill()
				break
			else:
				print("Retries: " + str(self.retriesCnt))
				self.retriesCnt += 1
				if self.retriesCnt > 20:
					if self.gksuHasStarted & (int(self.linecount2) > 1):
						#print("gksu has started, user has not given password yet")
						self.retriesCnt = 0
					elif self.gksuHasStarted & (int(self.linecount2) == 1):
						#print("User cancelled the operation")
						abnormalCheckUpdatesTermination = True
						self.sigDstarted.emit(2)
						return
					else:
						print("Process failed to start")
						abnormalCheckUpdatesTermination = True
						self.sigDstarted.emit(1)
						self.exit()
						return					
				#print("linecount is: " + str(int(linecount)))
				#print("linecount is: " + str(int(linecount)))
				#print("hasStarted is: " + str(self.hasStarted))
				#print("passing " + str(self.retriesCnt) + " -- effective user id: " + str(os.geteuid()))
		#print("calling exit for daemon checker")
		self.exec_()
		self.exit()
								
################################ Check Updates ###############################################################

class chkUpdateWorker(QtCore.QThread):
	global mutexStartCheck
	global abnormalChekUpdatesTermination 
	
	sigFailed = QtCore.Signal(bool, str)
	sigCheckFinished = QtCore.Signal(bool, str)

	#def getProcState(self):
	#	if hasattr(self, 'avgchkProc'):
	#		print("Proc State from Within: " + str(self.avgchkProc.state()))
	#		return str(self.avgchkProc.state())

	def __init__(self, parent=None):
		super(chkUpdateWorker, self).__init__(parent)
		abnormalCheckUpdatesTermination = False
	
	def emitProcStarted(self):
		print("------------- PROCESS STARTED!!! ------------------ " + str(self.avgchkupProc.state()))	
		
	def run(self):
		self.theOutput = ""
		result = None
		#self.avgchkupProc = QtCore.QProcess()
		self.avgchkupProc = QtCore.QProcess()
		self.avgchkupProc.started.connect(self.emitProcStarted)
		self.avgchkupProc.setStandardErrorFile("errfile.txt")
		self.avgchkupProc.open(QtCore.QIODevice.Unbuffered)
		self.avgchkupProc.destroyed.connect(self.procDestroyed)
		self.avgchkupProc.readyRead.connect(self.parseOutput)
		self.avgchkupProc.finished.connect(self.onAVGprocFinish)
		self.finished.connect(self.onThreadTermination)
		#self.avgchkupProc.set
		try:
			startLocker = QtCore.QMutexLocker(mutexStartCheck)
			#print("starting AVGUPDATE process with EUID: " + str(os.geteuid()))
			#print("Now EUID is: " + str(os.geteuid()))
			QtGui.QApplication.processEvents()
			self.avgchkupProc.start("gksu", ["avgupdate -c"])
			#print("started UPDATE PROCESS with state: " + str(self.avgchkupProc.state()))
			if not self.avgchkupProc.waitForStarted(msecs=3000):
				print("SOS: " + str(self.avgchkupProc.state()))
				self.sigFailed.emit(True, "")
				self.exit()
				return
			self.exec_()
			QtGui.QApplication.processEvents()
		except Exception as err:
			print("Failed to initialize QProcess: " + str(err))
			return

	def cleanUp(self):
		global abnormalCheckUpdatesTermination
		#abnormalTermination = True
		if hasattr(self, 'avgchkupProc'):
			if (self.avgchkupProc.state() == QtCore.QProcess.ProcessState.Running) | (self.avgchkupProc.state() == QtCore.QProcess.ProcessState.Starting):
				print("now killing")
				self.avgchkupProc.terminate()
				#self.avgchkupProc.close()
			abnormalCheckUpdatesTermination = True
			if hasattr(self, 'avgchupProc'):	
				while not self.avgchkupProc.waitForFinished():
					print("Waiting for proc to finish")
					self.avgchkupProc.finished.emit(255)
			else:
				pass
			#print(str(self.avgchkupProc.state()))
	
	def procDestroyed(self):
		print("AVG UPDATE CHECK DESTROYED!!!")
		
	def parseOutput(self):
		if (self.avgchkupProc.state() == QtCore.QProcess.ProcessState.Running):
			getLines = self.avgchkupProc.read(self.avgchkupProc.bytesAvailable())
			self.theOutput += str(getLines)
		for i,j in config.translationDict.items():
			self.theOutput = self.theOutput.replace(i,j)
		#print(str(self.theOutput))
	
	def __exit__(self):
		if hasattr(self, 'avgchkupProc'):
			if (self.avgchkupProc.state() == QtCore.QProcess.ProcessState.Running) | (self.avgchkupProc.state() == QtCore.QProcess.ProcessState.Starting):
				self.avgchkupProc.kill()
				del self.avgchkupProc
				
	def onThreadTermination(self):
		print("Thread finished")
				
	#def __del__(self):
	#	if hasattr(self, 'avgchkupProc'):
	#		del self.avgchkupProc
	#	gc.collect()
	
	def onAVGprocFinish(self):
		global abnormalCheckUpdatesTermination

		print(" --- QProcess Terminated --- ")	
		if hasattr(self, 'avgchkupProc'):
			#self.avgchkupProc.close()
			if (self.avgchkupProc.state() == QtCore.QProcess.ProcessState.Running) | (self.avgchkupProc.state() == QtCore.QProcess.ProcessState.Starting):
				print("have to kill again!")	
				self.avgchkupProc.kill()
		#if hasattr(self, 'avgchkupProc'):
		#	del self.avgchkupProc
		print("checking...")	
		if hasattr(self, 'avgchkupProc'):
			print("EXIT CODE: " + str(self.avgchkupProc.exitCode()))
			if (self.avgchkupProc.exitCode() == 1) | (self.avgchkupProc.exitCode() == 2) :
				abnormalCheckUpdatesTermination = False
			else:
				abnormalCheckUpdatesTermination = True
			self.sigCheckFinished.emit(abnormalCheckUpdatesTermination, self.theOutput)
		else:
			self.abnormalCheckUpdatesTermination = True
			self.sigCheckFinished.emit(abnormalCheckUpdatesTermination, self.theOutput)
		print("emitted with: " + str(abnormalCheckUpdatesTermination))
		#print("EXIT CODE: " + str(self.avgUpdateProc.exitCode()))
		if hasattr(self, 'avgchkupProc'):
			del self.avgchkupProc		
		gc.collect()
		#self.exit()

################################################# Update Process ####################################################

class updateWorker(QtCore.QThread):
	global abnormalUpdateTermination 

	sigWriteUpdate = QtCore.Signal(str)
	sigUpdateTerminated = QtCore.Signal(int)
	
	def __init__(self, parent=None):
		self.exitCode = 0
		super(updateWorker, self).__init__(parent)

	def onThreadTermination(self):
		print("- - - Update Thread Terminated - - -")

	def run(self):
		self.finished.connect(self.onThreadTermination)
		self.avgUpdateProc = QtCore.QProcess()
		self.avgUpdateProc.open(QtCore.QIODevice.Unbuffered)
		self.avgUpdateProc.destroyed.connect(self.avgProcDestroyed)
		self.avgUpdateProc.readyRead.connect(self.printOut)
		self.avgUpdateProc.finished.connect(self.onAVGProcFinish)
		self.avgUpdateProc.start("gksu", ["avgupdate"])
		try:
			startLocker = QtCore.QMutexLocker(mutexStartCheck)
			while not self.avgUpdateProc.waitForStarted(msecs=2000):
				print(" - avgupdate failed to start - ")
				#self.avgUpdateProc.readyRead.disconnect()
				#self.avgUpdateProc.kill()
				#self.avgUpdateProc.close()
				self.exitCode = 1 
				self.avgUpdateProc.finished.emit(self.exitCode)
				#self.avgUpdateProc.start("gksu", ["avgupdate"])
				self.exit()
				return
		except Exception as err:
			print("Failed to initialize Update Process" + str(err))
			return
		self.exec_()
	
	def cleanUp(self):
		#abnormalTermination = True
		if hasattr(self, 'avgUpdateProc'):
			if (self.avgUpdateProc.state() == QtCore.QProcess.ProcessState.Running) | (self.avgUpdateProc.state() == QtCore.QProcess.ProcessState.Starting):
				print("OK GOT IT")
				self.exitCode = 299
				self.avgUpdateProc.finished.emit(self.exitCode)
			if hasattr(self, 'avgUpdateProc'):	
				while not self.avgUpdateProc.waitForFinished():
					print("Waiting for update process to finish")
			else:
				pass
	
	def avgProcDestroyed(self):
		print(" - Update Process Destroyed - ")
	
	def printOut(self):
		try:
			self.theLine = str(self.avgUpdateProc.read(self.avgUpdateProc.bytesAvailable()))			
			self.sigWriteUpdate.emit(self.theLine)
		except UnicodeDecodeError as uderr:
			print("A Unicode Decode Error occurred: " + str(uderr))
		except Exception as genericError:
			print("A generic error occurred: " + str(genericError))


	def onAVGProcFinish(self):
		print(" - | - | - Update Process Terminated - | - | - ")
		if hasattr(self, 'avgUpdateProc'):
			print("exit code is: " + str(self.avgUpdateProc.exitCode()))
			#if self.avgUpdateProc.receivers(SIGNAL('readyRead()')) > 0:
			self.avgUpdateProc.readyRead.disconnect()
			print("status is: " + str(self.avgUpdateProc.state()))
			#if (self.avgUpdateProc.state() == QtCore.QProcess.ProcessState.Running) | (self.avgUpdateProc.state() == QtCore.QProcess.ProcessState.Starting):
				# trying to kill
			#	self.avgUpdateProc.kill()
			# trying to close
			#self.avgUpdateProc.close()
			print("trying to delete avgUpdateProc")
			del self.avgUpdateProc
				#while self.isRunning():
		#	self.exit()
		#	print("thread still running")
		#gc.collect()

		self.sigUpdateTerminated.emit(self.exitCode)			
		
	def __exit__(self):
		print("in custom exit")
		if hasattr(self, 'avgUpdateProc'):
			print(" -- trying to delete avgUpdateProc -- ")
			del self.avgUpdateProc

##########################################################################################################################

def checkFolderPermissions(filepath=""):
	# function that checks if user executing has write permissions to the directory filepath
	# either as owner, group or otheir
	
	if filepath == "":
		QtGui.QMessageBox.critical(None, "Προσοχή", "Δεν ήταν δυνατόν ο έλεγχος δικαιωμάτων του συγκεκριμένου directory", 
								 QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default, QtGui.QMessageBox.NoButton)
		return False
	else:
		try:
			st = os.stat(filepath)
			if os.getuid() == st.st_uid:
				if bool(st.st_mode & stat.S_IWUSR):
					return True
			if os.getgid() == st.st_gid:
				if bool(st.st_mode & stat.S_IWGPR):
					return True
			else:
				return bool(st.st_mode & stat.S_IWOTH)	
		except Exception as error:
			QtGui.QMessageBox.critical(None, "Προσοχή", "Δεν ήταν δυνατόν ο έλεγχος δικαιωμάτων του συγκεκριμένου directory" + str(error), 
								 QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default, QtGui.QMessageBox.NoButton)
			raise(error)
	
def isAVGDRunning():
# check if avgd is up and running	 
	returnCode = False
	
	try:
		out1 = subprocess.Popen(['ps','-C','avgd'], stdout=subprocess.PIPE)
		out2 = subprocess.Popen(["wc", "-l"], stdin=out1.stdout, stdout=subprocess.PIPE)
		out1.stdout.close()
		linecount = out2.communicate()[0]
	   
		try:
			lines = int(linecount)
			if lines == 2:
				returnCode = True
		except:
			print("An error - LEVEL 1 - has occured")		
	except:
		print("An error - LEVEL 2 - has occured") 
		
	return returnCode

def checkIsExtension(fileTypes):
# in scan settings, check if file extensions are actually passed by user, i.e. .pdf .m3u etc
	isOK = True
	prog = re.compile('^\.[a-zA-Z0-9]*$')
	fexts = fileTypes.split()
	for f in fexts:
		result = prog.match(f)
		if result == None:
			isOK = False
	#print(isOK)
	if isOK:
		return fexts
	else:
		return False

class debugger(QtCore.QThread):
	def __init__(self, parent=None):
		super(debugger, self).__init__(parent)
		
	def run(self):
		while True:
			for o in gc.get_objects():
				if(("PySide.QtCore.QProces" in str(type(o))) | ("QThread" in str(type(o)))):	
					print(str(o) + "ID: " + str(id(o)))
			self.sleep(5)
			
################################ SCAN WORKER ######################################################

class scanWorker(QtCore.QThread):
	sigWriteScan = QtCore.Signal(str)
	sigScanTerminated = QtCore.Signal(str)
	
	def __init__(self, scanPath, scanParams, parent=None):
		super(scanWorker, self).__init__(parent)
		self.scanPath = scanPath
		self.scanParams = scanParams
		self.setTerminationEnabled(True)  
		global malwareFound
		global infectedFiles
		global dbVersion
		global dbRelDate
		global user
		global numFilesHealed
		malwareFound = []
		infectedFiles = []
		dbVersion = None
		dbRelDate = None
		user = None
		numFilesHealed = 0
		self.normalTermination = "True"
	
	def __del__(self):
		if hasattr(self, 'avgscanProc'):
			del self.avgscanProc
		gc.collect()

	def run(self): 
		#print("CURRENT THREAD WHEN STARTING: " +  str(self.currentThreadId()))
		#print("Starting scan with scanPath: " + str(self.scanPath) + " and with scanParams: " + str(self.scanParams))
		#self.finished.connect(self.onThreadFinish)
		self.avgscanProc = QtCore.QProcess()
		self.avgscanProc.open(QtCore.QIODevice.Unbuffered)
		self.avgscanProc.destroyed.connect(self.procDestroyed)
		self.avgscanProc.readyRead.connect(self.printOut)
		self.avgscanProc.finished.connect(self.onAVGProcessFinish)
		if (self.avgscanProc.state() != QtCore.QProcess.ProcessState.Running) & (self.avgscanProc.state() != QtCore.QProcess.ProcessState.Starting) :
			
			print("---- STARTING AVG SCAN ----")
			if self.scanParams:
				try:
					print("Within try1 " + str(self.scanParams))
					self.avgscanProc.start("avgscan", [self.scanPath] + self.scanParams)
					self.exec_()
					#while not self.avgscanProc.waitForStarted():
					#print("Waiting avgscanProc to start") 
				except Exception as errinit1:
						print("Σφάλμα κατά την εκκίνηση της σάρωσης: " + str(errinit2))
			else:
				try:
					print("Within try2")
					self.avgscanProc.start("avgscan", [self.scanPath])
					self.exec_()
					#while not self.avgscanProc.waitForStarted():
					#	 print("Waiting avgscanProc to start") 
				except Exception as errinit2:
					print("Σφάλμα κατά την εκκίνηση της σάρωσης: " + str(errinit2))

	def procDestroyed(self):
		print("!!!!!! PROCESS DESTROYED !!!!!!") 
	
	@QtCore.Slot()	  
	def printOut(self):
		global malwareFound
		global infectedFiles
		global dbVersion
		global dbRelDate
		global user
		global numFilesHealed
		global mutexResults
	
		try:
			if (self.avgscanProc.state() == QtCore.QProcess.ProcessState.Running) | (self.avgscanProc.state() == QtCore.QProcess.ProcessState.Starting):
				#print(str(self.avgscanProc))
				#print("Before reading: " + str(id(self.avgscanProc)))
				self.theLine = self.avgscanProc.read(self.avgscanProc.bytesAvailable())
				#self.theLine = self.avgscanProc.readAllStandardOutput()
				#print("--------------")
				#print(str(self.avgscanProc))
				self.sigWriteScan.emit(str(self.theLine))
			else:
				print("DID NOT MANAGE TO RETRIEVE LINE")
				print("In printOut, Thread id: " + str(id(self)))
				print("In printOut, PROCESS id: " + str(id(self.avgscanProc)))
				#print(vars(self.avgscanProc))
				self.avgscanProc.closeWriteChannel()
				self.avgscanProc.closeReadChannel(QProcess.StandardOutput)
				print(str(self.avgscanProc.readChannel()))
				#self.avgscanProc.finished.emit(0)
				#gc.collect()
				return
		except UnicodeDecodeError as uerr:
			print ("A Unicode error occurred: " + str(uerr))
			return
		except Exception as genericerror:
			print("A generic error occurred: " + str(genericerror)) 
			return
		
		
		textin = str(self.theLine).splitlines()
		#print("textin, within processScanOutput: " + str(textin))
		
		try:
			locker = QtCore.QMutexLocker(mutexResults)
			for i in textin:
				if str(i).find("Virus database version") != -1:
					#print("i: " + str(i))
					dbVersion = i[24:] 
				if str(i).find("Virus database release date") != -1:
					#print("i: " + str(i))
					dbRelDate = i[29:] 
				if str(i).find("Virus identified") != -1:
					#print("i: " + str(i))
					infectedFiles.append(i.split()[0])
					malwareFound.append(i.split()[3])
				if str(i).find("Virus found") != -1:
					#print("i: " + str(i))
					infectedFiles.append(i.split()[0])
					malwareFound.append(i.split()[3])
				if str(i).find("Files healed") != -1:
					numFilesHealed = i.split()[3]
		except Exception as err:
			print(str(err))
		
		
	def killScan(self):
		if (self.avgscanProc.state() == QtCore.QProcess.ProcessState.Running) | (self.avgscanProc.state() == QtCore.QProcess.ProcessState.Starting):
			print("killing scan - in scanWorker class")
			self.normalTermination="False"
			self.avgscanProc.finished.emit(0)
		else:
			pass
		#self.avgscanProc.finished.emit()
		
		
		#if hasattr(self, 'avgscanProc'):
		#while not self.avgscanProc.waitForFinished():
		#print("Waiting....")
		#self.sigScanTerminated.emit()
	
	def getScanState(self):
		if hasattr(self, 'avgscanProc'):
			return self.avgscanProc.state()
		else:
			pass

	def onAVGProcessFinish(self):
		print("--------- QProcess Terminated ----------")
		if hasattr(self, 'avgscanProc'):
			print("Exit Code: " + str(self.avgscanProc.exitCode()))
		#try:
		#	self.avgscanProc.readyRead.disconnect
		#except Exception as disconect_error:
		#	print("Error Disconnectint readyRead signal")
		if hasattr(self, 'avgscanProc'):
			if (self.avgscanProc.state() == QtCore.QProcess.ProcessState.Running) | (self.avgscanProc.state() == QtCore.QProcess.ProcessState.Starting):
				print("It was still running - trying to kill it again")
				self.avgscanProc.kill()
			#self.avgscanProc.close()
		if hasattr(self, 'avgscanProc'):
			del self.avgscanProc
		gc.collect()
		if hasattr(self, 'avgscanProc'):
			while not self.avgscanProc.waitForFinished():
				print("Waiting before emitting...")
		self.sigScanTerminated.emit(self.normalTermination)
		self.exit()
		
	def onThreadFinish(self):
		self.exit()

##################################### END OF CLASS SCAN WORKER #############################

class sqliteWorker(QtCore.QThread):
	
	def __init__(self, parent=None):
		super(sqliteWorker, self).__init__(parent)
			
	def run(self):
		global malwareFound
		global infectedFiles
		global dbVersion
		global dbRelDate
		global user
		global numFilesHealed
		global mutexResults
		scaneventID = None # to be used when entering into tblInfections
		sqlocker = QtCore.QMutexLocker(mutexResults)
	
		try:
			#print("Opening connection")	  
			# open db connection and create cursor
			# to replace the path in the connect statement
			conn = sqlite3.connect(config.DBFILEPATH)
			#print("Creating Cursor")	 
			cur = conn.cursor()
			
			
			#########################
			# check Virus DB and Date
			# if it does not exist
			#	add it in tblVirusDB
			########################
			#print("Executing tblVirusDBs insertion")	 
			getVirusDBs = cur.execute("""select * from tblVirusDBs""")
			virusDBslist = getVirusDBs.fetchall()
			#print("virusDBslist :" + str(virusDBslist))
			if not virusDBslist: # if no virus db entry yet
				toInsert = (dbVersion, dbRelDate)
				#print("toInsert in VirusDB: " + str(toInsert))
				#print("inserting ONE...!!!!!")
				cur.execute('insert into tblVirusDBs (DBVersion, DBrDate) values (?, ?)', toInsert)
				#conn.commit()
			else:
				cnt = 0
				while cnt < len(virusDBslist):
					#print("here")
					if (dbVersion in virusDBslist[cnt][1]):
						#print(cnt)
						break
					cnt = cnt + 1
				if cnt >= len(virusDBslist):
					toInsert = (dbVersion, dbRelDate)
					#print(str(toInsert))
					#print("cnt: " + str(cnt))
					cur.execute('insert into tblVirusDBs (DBVersion, DBrDate) values (?, ?)', toInsert)
					#conn.commit()
									 
			
			#################################
			# for all malware identified
			#	 if name does not exist
			#		 add it in the tblMalware
			#################################
			#print("Checking if malware found") 
			
			if malwareFound:
				
				cur.execute("""select Name from tblMalware""")
				getMalware = cur.fetchall()
				if not getMalware: # if no malware has yet been inserted in tblMalware
					for mal in malwareFound:
						t = (mal,)
						#print("Malware insertion") 
						cur.execute('insert into tblMalware (Name) values (?)', t) 
						#conn.commit()
				else: 
					for mal in malwareFound:
							t = (mal,)
							if t in getMalware:
								pass
							else:
								#print("Malware insertion v2") 
								cur.execute('insert into tblMalware (Name) values (?)', t)	
								#conn.commit()
						   
			#########################################
			# create Scan Event entry in tblScanEvent
			#########################################
			curDateTime = datetime.now().isoformat(' ')[:19]
			user = getpass.getuser()
			numInfections = len(infectedFiles)
			#scanWorker.numFilesHealed
			
			# getting dbID from the tblVirusDBs
			#print("dbVersion is: " + dbVersion)
			dbVerTuple = (dbVersion, )
			#print("dbVerTuple: " + str(dbVerTuple))
			dbs = cur.execute('select ID from tblVirusDBs where DBVersion = ?', dbVerTuple)
			dblist = dbs.fetchall()
			#print("dblist: " + str(dblist))
			if len(dblist) > 1:
				print("Σφάλμα κατά την εξαγωγή του dbID")
				conn.close()
				raise Exception("Error getting dbID")
				exit(-1)
			else:
				#print("foufoutos")
				#exit(1)
				dbID = dblist[0][0]
		   
					 
			
			tupleToInsert = (user, numInfections, numFilesHealed, curDateTime, dbID)
			
			
			# inserting Scan Event
			cur.execute('insert into tblScanEvent (User, NoOfInfections, NoOfHealings, DateTime, VirusDBID) values (?,?,?,?,?)', tupleToInsert)
			#conn.commit()
			
			################################
			# for each file infected 
			#	  add entry in tblInfections
			################################
			
			# get Scan Event ID just entered
			y = conn.execute('select * from tblScanEvent order by ID desc limit 1')
			z = 0
			for rowSEID in y:
				scaneventID = rowSEID[0]
				#print("scan event ID: " + str(scaneventID))
				z = z + 1
			if z != 1:
				print("Σφάλμα κατά την εξαγωγή του Scan Event ID " + str(scaneventID))
				raise Exception("Error getting Scan Event ID")
				conn.close()
				exit(-1)
			
			# for each infected file of the specific Scan Event, i.e. in infectedFiles
			#	  get the malware ID from tblMalware
			#	  get the file name/path
			
			i = 0
			
			for inFile in infectedFiles:
				okGo = True; # if inode exists, will not proceed with insertion
				# we will need the inode of that particular file
				
				try:
					checkls = subprocess.check_output(["ls", "-i", str(inFile)])
					inode = int(checkls.decode("utf").split()[0])
					#print("inode " + str(inode))
					inodesexisting = conn.execute("select Inode from tblInfections").fetchall()
					#print("Existing inodes: " + str(inodesexisting))
					if (inode,) in inodesexisting:
						print("PROBLEM")
						okGo = False
				except Exception:
					raise Exception("Error while getting file's iNode number")
				
				if True:
					mal = (malwareFound[i], )				 
					f = conn.execute('select ID from tblMalware where name = ?', mal)
					malist = f.fetchall()
					if len(malist) != 1:
						raise Exception("Σφάλμα και την εξαγωγή malware ID από το tblMalware")
						conn.close()
						exit(-1)
					malID = malist[0][0]	
					i = i + 1
					infToInsert = (inFile, inode, scaneventID, malID)
					# insert into tblInfections 
					cur.execute('insert into tblInfections (FilePath, Inode, ScanEventID, MalwareID) values (?,?,?,?)', infToInsert)
					#conn.commit()
			
			
			conn.commit()
			conn.close()
			malwareFound = []
			infectedFiles = []
			dbVersion = None
			dbRelDate = None
			user = None
			numFilesHealed = 0
			print("--- Terminating SQLITEworker ---")
			self.exit()
				 
			
		except Exception as err:
			 print("Σφάλμα κατά την εισαγωγή στοιχείων στη βάση: "	 + str(err))
			 conn.close()
			 raise Exception(str(err))

# --- Models and Data needed to populate Combo Boxes of search dialog --- #

def populateVirusDBs():
	availableDBs = []
	try:
		conn = sqlite3.connect(config.DBFILEPATH)
		cur = conn.execute('select DBVersion from tblVirusDBs')
		tmpList = cur.fetchall()
		if len(tmpList) > 0:
			count = len(tmpList)
			for i in range(count):
				availableDBs.append(tmpList[i][0])
	except Exception as errinit:
		 QtGui.QMessageBox.critical(None, "Προσοχή", "Σφάλμα κατά την αρχικοποίηση Virus DB Combo Box: " + str(errinit), 
								 QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default, QtGui.QMessageBox.NoButton)
	return availableDBs
					

def populateMalware():
	availableMalware = []
	try:
		conn = sqlite3.connect(config.DBFILEPATH)
		cur = conn.execute('select Name from tblMalware')
		tmpList = cur.fetchall()
		if len(tmpList) > 0:
			count = len(tmpList)
			for i in range(count):
				availableMalware.append(tmpList[i][0])
	except Exception as errinit:
		 QtGui.QMessageBox.critical(None, "Προσοχή", "Σφάλμα κατά την αρχικοποίηση Malware Combo Box: " + str(errinit), 
								 QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default, QtGui.QMessageBox.NoButton)
	return availableMalware
		 

class virusDBModel(QtCore.QAbstractListModel):
	def __init__(self, availableDBs, parent=None):
		super(virusDBModel, self).__init__(parent)
		self.__availableDBs = availableDBs
		if self.__availableDBs:
			self.__availableDBs.insert(0, "")
		
		
	def data(self, index, role):
		
		if role == QtCore.Qt.DisplayRole:
			row = index.row()
			value = self.__availableDBs[row]
			
			#print(type(value))
			return value
	 
	def rowCount(self, parent):
		
		return len(self.__availableDBs)


class malwareModel(QtCore.QAbstractListModel):
	def __init__(self, availableMalware, parent=None):
		super(malwareModel, self).__init__(parent)
		self.__availableMalware = availableMalware
		if self.__availableMalware:
			self.__availableMalware.insert(0, "")
		
	def data(self, index, role):
		
		if role == QtCore.Qt.DisplayRole:
			row = index.row()
			value = self.__availableMalware[row]
			
			#print(type(value))
			return value
	 
	def rowCount(self, parent):
		
		return len(self.__availableMalware)
		
# --- Models and Data needed to support the Table View of Scan Results --- #

def scanSearchQuery(startDate ='', endDate ='', malwareFound ='', databaseUsed =''):
	
	try:
		conn = sqlite3.connect(config.DBFILEPATH)
		cur = conn.cursor()
		querySelect = 'SELECT DISTINCT tblScanEvent.User, tblScanEvent.NoOfInfections '
		queryFrom = 'FROM tblScanEvent '
		queryWhere = ''
		whereCondition = False
		if malwareFound != '':
			querySelect = querySelect + ', tblMalware.Name '
			queryFrom = queryFrom + ',tblMalware, tblInfections '
			queryWhere = 'tblScanEvent.ID = tblInfections.ScanEventID AND tblMalware.Name =' + "'" + malwareFound + "' "
			whereCondition = True
		if databaseUsed != '':
			querySelect = querySelect + ', tblVirusDBs.DBVersion '
			queryFrom = queryFrom + ',tblVirusDBs '
			if whereCondition:
				queryWhere = queryWhere + "AND "
			queryWhere = queryWhere + 'tblVirusDBs.DBVersion=' + "'" + databaseUsed + "' " + 'AND tblScanEvent.VirusDBID = tblVirusDBs.ID ' 
			whereCondition = True
		if startDate != '':
			if whereCondition:
				queryWhere = queryWhere + "AND "
			queryWhere = queryWhere + """tblScanEvent.DateTime >= datetime('""" + startDate	 + """') """
			whereCondition = True
		if endDate != '':
			if whereCondition:
				queryWhere = queryWhere + "AND "
			queryWhere = queryWhere + """tblScanEvent.DateTime <= datetime('""" + endDate  + """') """
			whereCondition = True
		querySelect = querySelect + ', tblScanEvent.DateTime '
		if whereCondition:
			queryString = querySelect + queryFrom + "WHERE " + queryWhere
		else:
			queryString = querySelect + queryFrom
		queryString = queryString + 'ORDER BY tblScanEvent.DateTime'
		#print(queryString)
		results = cur.execute(queryString)
		resultsList = results.fetchall()
		#print("resultsList: " + str(resultsList))
	
	except Exception as errcon:
		QtGui.QMessageBox.critical(None, "Προσοχή", "Σφάλμα κατά την αναζήτηση περιεχομένου στη βάση: " + str(errcon), 
								 QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default, QtGui.QMessageBox.NoButton)
	return resultsList
	 
			
class scanResultsTableModel(QtCore.QAbstractTableModel):
	
	def __init__(self, results = [[]], flag = 0, parent=None):
		super(scanResultsTableModel, self).__init__(parent)
		self.__results = results
		#self.__headers = headers
		self.__flag = flag
		
	def rowCount(self, parent):
		return len(self.__results)
	
	def columnCount(self, parent):
		return len(self.__results[0])
	
	def flags(self, index):
		return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
	
	def data(self, index, role):
		
		if role == QtCore.Qt.DisplayRole:
			row = index.row()
			column = index.column()
			value = self.__results[row][column]
			return value
			
		if role == QtCore.Qt.TextAlignmentRole:
			#print("test")
			return QtCore.Qt.AlignCenter
			
			
	def headerData(self, section, orientation, role):
		
		
		headersList = [['Χρήστης', 'Αριθμός Ευρημάτων', 'Ημερομηνία - Ώρα Αναζήτησης'], ['Χρήστης', 'Αριθμός Ευρημάτων', 'Βάση Ιών', 'Ημερομηνία - Ώρα Αναζήτησης'],
					   ['Χρήστης', 'Αριθμός Ευρημάτων', 'Κακόβουλο Λογισμικό', 'Ημερομηνία - Ώρα Αναζήτησης'], 
					   ['Χρήστης', 'Αριθμός Ευρημάτων', 'Κακόβουλο Λογισμικό', 'Βάση Ιών', 'Ημερομηνία - Ώρα Αναζήτησης']]
		
		if role == QtCore.Qt.DisplayRole:
			if orientation == QtCore.Qt.Horizontal:
				#print(headersList[self.__flag])
				return headersList[self.__flag][section]
			else:
				return str(section + 1)
		  
		if role == QtCore.Qt.TextAlignmentRole:
			return QtCore.Qt.AlignCenter

##################################### RETRIEVE CORE AND VIRUS DB UPDATES HISTORY ################################	

class dbHistoryTableModel(QtCore.QAbstractTableModel):
	
	def __init__(self, results = [[]], parent=None):
		super(dbHistoryTableModel, self).__init__(parent)
		self.__results = results
		#self.__headers = headers
		
		
	def rowCount(self, parent):
		return len(self.__results)
	
	def columnCount(self, parent):
		return len(self.__results[0])
	
	def flags(self, index):
		return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
	
	def data(self, index, role):
		
		if role == QtCore.Qt.DisplayRole:
			row = index.row()
			column = index.column()
			value = self.__results[row][column]
			return value
			
		if role == QtCore.Qt.TextAlignmentRole:
			#print("test")
			return QtCore.Qt.AlignCenter
			
			
	def headerData(self, section, orientation, role):
		
		
		headers = ["Ημερομηνία / Ώρα Ανανέωσης", "Έκδοση Core AVG / Βάση Ιών"]
		
		if role == QtCore.Qt.DisplayRole:
			if orientation == QtCore.Qt.Horizontal:
				#print(headersList[self.__flag])
				return headers[section]
			else:
				return str(section + 1)
			
		if role == QtCore.Qt.TextAlignmentRole:
			return QtCore.Qt.AlignCenter		 

# QThread Class

class dbHistoryWorker(QtCore.QThread):
	sigHistoryRetrieved = QtCore.Signal(list)
	#sigScanTerminated = QtCore.Signal()
	
	def __init__(self, parent=None):
		super(dbHistoryWorker, self).__init__(parent)
		self.__results = []
		self.finished.connect(self.ondbHistoryProcessFinish)
				
	def run(self): 
		try:
			self.dbupdhist = subprocess.check_output(["gksu","--description=Ιστορικό", "--message='H εκτέλεση της συγκεκριμένης ενέργειας απαιτεί την εισαγωγή κωδικού χρήστη (password)'", "avgevtlog"]).decode("utf")
		except subprocess.CalledProcessError as cpe:
			print(str(cpe))				   
		print(type(self.dbupdhist))
		flagParse = False
		#flagStore = False
		tmpList = []
		for line in self.dbupdhist.splitlines():
			if ("Loaded core/iavi version:" in line):
				print(line)
			if ("Update: Started scheduled update with priority 2." in line):
				#print("in first if")
				flagParse = True
				continue
			if flagParse:
				#print("in second if")
				if ("Loaded core/iavi version:" in line):
					#print("in second second if")
					tmpList.append(line[0:19])
					tmpList.append(line[52:61])
					flagParse = False
					#print("tmpList "  + str(tmpList) )
					continue
				else:
					#print("in first else if")
					tmpList = []
					flagParse = False
					continue
			if ("Update: Update was successfully completed." in line) & (len(tmpList) > 0):
				#print("in third if" + str(tmpList))
				self.__results.append(tmpList)
				tmpList = []
				continue
			else:
				#print("in last else")
				tmpList = []
				flagParse = False
				continue
				
		#self.exec_()

	def ondbHistoryProcessFinish(self):
		print("Results")
		print(len(self.__results))
		self.sigHistoryRetrieved.emit(self.__results)
		#self.dbHistoryProc.terminate()
		self.exit()
