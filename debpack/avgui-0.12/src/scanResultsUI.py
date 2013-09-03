# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanResults.ui'
#
# Created: Wed Aug 28 18:50:50 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dialogScanResults(object):
    def setupUi(self, dialogScanResults):
        dialogScanResults.setObjectName("dialogScanResults")
        dialogScanResults.setWindowModality(QtCore.Qt.ApplicationModal)
        dialogScanResults.resize(952, 517)
        self.pushButton = QtGui.QPushButton(dialogScanResults)
        self.pushButton.setGeometry(QtCore.QRect(330, 390, 311, 51))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.exitButton = QtGui.QPushButton(dialogScanResults)
        self.exitButton.setGeometry(QtCore.QRect(410, 450, 141, 51))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayoutWidget = QtGui.QWidget(dialogScanResults)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 931, 371))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tblVscanResults = QtGui.QTableView(self.horizontalLayoutWidget)
        self.tblVscanResults.setAlternatingRowColors(True)
        self.tblVscanResults.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tblVscanResults.setSortingEnabled(True)
        self.tblVscanResults.setObjectName("tblVscanResults")
        self.tblVscanResults.horizontalHeader().setCascadingSectionResizes(True)
        self.tblVscanResults.horizontalHeader().setDefaultSectionSize(150)
        self.tblVscanResults.horizontalHeader().setMinimumSectionSize(150)
        self.tblVscanResults.horizontalHeader().setStretchLastSection(True)
        self.tblVscanResults.verticalHeader().setCascadingSectionResizes(True)
        self.tblVscanResults.verticalHeader().setDefaultSectionSize(30)
        self.tblVscanResults.verticalHeader().setMinimumSectionSize(30)
        self.tblVscanResults.verticalHeader().setSortIndicatorShown(True)
        self.tblVscanResults.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.tblVscanResults)

        self.retranslateUi(dialogScanResults)
        QtCore.QMetaObject.connectSlotsByName(dialogScanResults)

    def retranslateUi(self, dialogScanResults):
        dialogScanResults.setWindowTitle(QtGui.QApplication.translate("dialogScanResults", "Αποτελέσματα Αναζήτησης", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("dialogScanResults", "Εξαγωγή Αποτελεσμάτων σε .txt αρχείο", None, QtGui.QApplication.UnicodeUTF8))
        self.exitButton.setText(QtGui.QApplication.translate("dialogScanResults", "Έξοδος", None, QtGui.QApplication.UnicodeUTF8))

