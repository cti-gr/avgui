from os.path import expanduser
import PySide

global DBFILEPATH

translationDict = {
'Virus update':'Βάση Ιών',
'Download':'Μέγεθος Αρχείου',
'Component':'Μέρος Προγράμματος',
'priority':'Προτεραιότητα Ενημέρωσης',
'Installed version':'Έγκατεστημένη έκδοση',
'Available version':'Έκδοση διαθέσιμη για μεταφόρτωση',
'Recommended update':'Συνιστώμενη Ενημέρωση',
'Program update':'Ενημέρωση Προγράμματος',
'iAVI database':'Βάση iAVI'
}

def init_config(devmode):
    DBFILENAME = "avghistory.sqlite"
    global DBFILEPATH
    homedir = expanduser("~")
    if devmode:
        DBFILEPATH = DBFILENAME
    else:
        DBFILEPATH = homedir + "/.avgui/" + DBFILENAME
    
