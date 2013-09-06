from PySide import QtGui
from PySide import QtCore
from datetime import datetime, date, time
import subprocess, re, gc
import setupGui
import sqlite3
import getpass
import config

# To add utility that periodically checks for size of the database !!!

malwareFound = []
infectedFiles =[]
dbVersion = None
dbRelDate = None
user = None
numFilesHealed = 0
mutexResults = QtCore.QMutex()
foo = 0

# function to check database existence and integrity

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

class scanWorker(QtCore.QThread):
    sigWriteScan = QtCore.Signal(str)
    sigScanTerminated = QtCore.Signal()
    
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
        print(str(self.scanParams))
        
        
           
    def run(self): 
        #print("CURRENT THREAD WHEN STARTING: " +  str(self.currentThreadId()))
        print("Starting scan with scanPath: " + str(self.scanPath) + " and with scanParams: " + str(self.scanParams))
        self.finished.connect(self.onThreadFinish)
        self.avgscanProc = QtCore.QProcess()
        self.avgscanProc.readyReadStandardOutput.connect(self.printOut)
        self.avgscanProc.finished.connect(self.onAVGProcessFinish)
        if (self.avgscanProc.state() != QtCore.QProcess.ProcessState.Running) & (self.avgscanProc.state() != QtCore.QProcess.ProcessState.Starting) :
            
            #print("---- STARTING AVG SCAN ----")
            if self.scanParams != None:
                try:
                    self.avgscanProc.start("avgscan", [self.scanPath] + self.scanParams)
                except ExceptionInit as errinit:
                        print("Σφάλμα κατά την εκκίνηση της σάρωσης " + str(errinit))
            else:
                try:
                    self.avgscanProc.start("avgscan", [self.scanPath])
                except ExceptionInit as errinit:
                    print("Σφάλμα κατά την εκκίνηση της σάρωσης " + str(errinit))
                
        self.exec_()
       
        
        
    def printOut(self):
        global malwareFound
        global infectedFiles
        global dbVersion
        global dbRelDate
        global user
        global numFilesHealed
        global mutexResults
       
        try:
           self.theLine = str(self.avgscanProc.readAllStandardOutput())
        except UnicodeDecodeError:
            pass                
        self.sigWriteScan.emit(self.theLine)
        
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
        
        #self.exec_()
        
    def killScan(self):
        if (self.avgscanProc.state() == QtCore.QProcess.ProcessState.Running) | (self.avgscanProc.state() == QtCore.QProcess.ProcessState.Starting):
            #print("PROCESS was running, now exiting - KILLED")
            self.avgscanProc.kill()
            #self.exit()
       
        
    def onAVGProcessFinish(self):
        #print("--------- QProcess Terminated ----------")
        self.avgscanProc.readyReadStandardOutput.disconnect()
        self.avgscanProc.close()
        self.avgscanProc.finished.disconnect()
        self.exit()
        self.avgscanProc.terminate()
        
    
    def onThreadFinish(self):
       
        self.exit()


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
            #   add it in tblVirusDB
            ########################
            print("Executing tblVirusDBs insertion")    
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
                    print("here")
                    if (dbVersion in virusDBslist[cnt][1]):
                        print(cnt)
                        break
                    cnt = cnt + 1
                if cnt >= len(virusDBslist):
                    toInsert = (dbVersion, dbRelDate)
                    print(str(toInsert))
                    print("cnt: " + str(cnt))
                    cur.execute('insert into tblVirusDBs (DBVersion, DBrDate) values (?, ?)', toInsert)
                    #conn.commit()
                                     
            
            #################################
            # for all malware identified
            #    if name does not exist
            #        add it in the tblMalware
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
            print("dbVersion is: " + dbVersion)
            dbVerTuple = (dbVersion, )
            print("dbVerTuple: " + str(dbVerTuple))
            dbs = cur.execute('select ID from tblVirusDBs where DBVersion = ?', dbVerTuple)
            dblist = dbs.fetchall()
            print("dblist: " + str(dblist))
            if len(dblist) > 1:
                print("Σφάλμα κατά την εξαγωγή του dbID")
                conn.close()
                raise Exception("Error getting dbID")
                exit(-1)
            else:
                print("foufoutos")
                #exit(1)
                dbID = dblist[0][0]
           
                     
            
            tupleToInsert = (user, numInfections, numFilesHealed, curDateTime, dbID)
            
            
            # inserting Scan Event
            cur.execute('insert into tblScanEvent (User, NoOfInfections, NoOfHealings, DateTime, VirusDBID) values (?,?,?,?,?)', tupleToInsert)
            #conn.commit()
            
            ################################
            # for each file infected 
            #     add entry in tblInfections
            ################################
            
            # get Scan Event ID just entered
            y = conn.execute('select * from tblScanEvent order by ID desc limit 1')
            z = 0
            for rowSEID in y:
                scaneventID = rowSEID[0]
                print("scan event ID: " + str(scaneventID))
                z = z + 1
            if z != 1:
                print("Σφάλμα κατά την εξαγωγή του Scan Event ID " + str(scaneventID))
                raise Exception("Error getting Scan Event ID")
                conn.close()
                exit(-1)
            
            # for each infected file of the specific Scan Event, i.e. in infectedFiles
            #     get the malware ID from tblMalware
            #     get the file name/path
            
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
             print("Σφάλμα κατά την εισαγωγή στοιχείων στη βάση: "  + str(err))
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
            queryWhere = queryWhere + """tblScanEvent.DateTime >= datetime('""" + startDate  + """') """
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
        print(queryString)
        results = cur.execute(queryString)
        resultsList = results.fetchall()
        print("resultsList: " + str(resultsList))
    
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
        except CalledProcessError as cpe:
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
        
################################################################################################