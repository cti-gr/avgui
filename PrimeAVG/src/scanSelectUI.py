# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanSelect.ui'
#
# Created: Wed Nov 20 18:07:56 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_scanSelectDialog(object):
    def setupUi(self, scanSelectDialog):
        scanSelectDialog.setObjectName("scanSelectDialog")
        scanSelectDialog.setWindowModality(QtCore.Qt.WindowModal)
        scanSelectDialog.resize(400, 180)
        scanSelectDialog.setMinimumSize(QtCore.QSize(400, 180))
        scanSelectDialog.setMaximumSize(QtCore.QSize(400, 180))
        self.label = QtGui.QLabel(scanSelectDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/avg_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(scanSelectDialog)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 261, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioFile = QtGui.QRadioButton(scanSelectDialog)
        self.radioFile.setGeometry(QtCore.QRect(60, 90, 116, 22))
        self.radioFile.setObjectName("radioFile")
        self.radioFolder = QtGui.QRadioButton(scanSelectDialog)
        self.radioFolder.setGeometry(QtCore.QRect(240, 90, 116, 22))
        self.radioFolder.setObjectName("radioFolder")
        self.exitButton = QtGui.QPushButton(scanSelectDialog)
        self.exitButton.setGeometry(QtCore.QRect(150, 130, 101, 41))
        self.exitButton.setAutoDefault(False)
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(scanSelectDialog)
        QtCore.QMetaObject.connectSlotsByName(scanSelectDialog)

    def retranslateUi(self, scanSelectDialog):
        scanSelectDialog.setWindowTitle(QtGui.QApplication.translate("scanSelectDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("scanSelectDialog", "Αναζήτηση Κακόβουλου Λογισμικού", None, QtGui.QApplication.UnicodeUTF8))
        self.radioFile.setText(QtGui.QApplication.translate("scanSelectDialog", "Σε Αρχείο", None, QtGui.QApplication.UnicodeUTF8))
        self.radioFolder.setText(QtGui.QApplication.translate("scanSelectDialog", "Σε Φάκελο", None, QtGui.QApplication.UnicodeUTF8))
        self.exitButton.setText(QtGui.QApplication.translate("scanSelectDialog", "Έξοδος", None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
