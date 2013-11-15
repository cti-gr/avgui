# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'countDown.ui'
#
# Created: Fri Nov 15 18:55:36 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_formCountDown(object):
    def setupUi(self, formCountDown):
        formCountDown.setObjectName("formCountDown")
        formCountDown.setWindowModality(QtCore.Qt.WindowModal)
        formCountDown.resize(564, 119)
        formCountDown.setMinimumSize(QtCore.QSize(564, 119))
        formCountDown.setMaximumSize(QtCore.QSize(564, 119))
        self.countDownLCD = QtGui.QLCDNumber(formCountDown)
        self.countDownLCD.setGeometry(QtCore.QRect(200, 70, 141, 31))
        self.countDownLCD.setProperty("value", 30.0)
        self.countDownLCD.setObjectName("countDownLCD")
        self.countDownLabel = QtGui.QLabel(formCountDown)
        self.countDownLabel.setGeometry(QtCore.QRect(40, 10, 501, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.countDownLabel.setFont(font)
        self.countDownLabel.setObjectName("countDownLabel")
        self.label = QtGui.QLabel(formCountDown)
        self.label.setGeometry(QtCore.QRect(100, 40, 381, 17))
        self.label.setObjectName("label")

        self.retranslateUi(formCountDown)
        QtCore.QMetaObject.connectSlotsByName(formCountDown)

    def retranslateUi(self, formCountDown):
        formCountDown.setWindowTitle(QtGui.QApplication.translate("formCountDown", "Αναζήτηση Ενημερώσεων...", None, QtGui.QApplication.UnicodeUTF8))
        self.countDownLabel.setText(QtGui.QApplication.translate("formCountDown", "Παρακαλώ περιμένετε ενώ γίνεται έλεγχος για διαθέσιμες ενημερώσεις", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("formCountDown", "Αναμενόμενος μέγιστος χρόνος ολοκλήρωσης ελέγχου...", None, QtGui.QApplication.UnicodeUTF8))

