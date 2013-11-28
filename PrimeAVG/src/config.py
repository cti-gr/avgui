from os.path import expanduser

import PySide
from PySide import QtCore
import sys

global avgmonitor
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
'iAVI database':'Βάση iAVI',
'Running update.':'Έλεγχος Διαθεσιμότητας Ενημερώσεων',
'Operation failed. The exit code could not be got because the thread or process is still alive.':'Η Διεργασία Δεν Μπόρεσε να Ολοκληρωθεί. Παρακαλούμε Επαναλάβατε την Εκτέλεσή της.',
'Initializing':'Αρχικοποίηση',
'Analyzing':'Ανάλυση Διαθέσιμων Ενημερώσεων'
}
global PYSIDE_VERSION
global QT_VERSION
global PYTHON_VERSION

def init_config(devmode):

	global avgmonitor
	global DBFILEPATH
	global PYSIDE_VERSION
	global QT_VERSION
	global PYTHON_VERSION

	avgmonitor = "avgmonitor.py"
	PYTHON_VERSION=sys.version
	PYSIDE_VERSION=PySide.__version__
	QT_VERSION=PySide.QtCore.__version__
	DBFILENAME = "avghistory.sqlite"
	homedir = expanduser("~")
	if devmode:
		DBFILEPATH = DBFILENAME
	else:
		DBFILEPATH = homedir + "/.avgui/" + DBFILENAME

