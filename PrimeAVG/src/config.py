from os.path import expanduser

import PySide
from PySide import QtCore
import sys

global DBFILEPATH

translationDict = {
'You are currently up-to-date':'Δεν υπάρχουν πρόσφατες ενημερώσεις',
'Update was successfully completed':'Η διαδικασία ελέγχου ενημερώσεων ολοκληρώθηκε επιτυχώς',
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
global PYSIDE_VERSION
global QT_VERSION
global PYTHON_VERSION

def init_config(devmode):


    global DBFILEPATH
    global PYSIDE_VERSION
    global QT_VERSION
    global PYTHON_VERSION

    PYTHON_VERSION=sys.version
    PYSIDE_VERSION=PySide.__version__
    QT_VERSION=PySide.QtCore.__version__
    DBFILENAME = "avghistory.sqlite"
    homedir = expanduser("~")
    if devmode:
        DBFILEPATH = DBFILENAME
        print("Python version: " + PYTHON_VERSION)
        print("PySide version: " + PYSIDE_VERSION)
        print("Qt Version: " + QT_VERSION)
    else:
        DBFILEPATH = homedir + "/.avgui/" + DBFILENAME

