# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanResults.ui'
#
# Created: Wed Nov 20 12:46:09 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dialogScanResults(object):
    def setupUi(self, dialogScanResults):
        dialogScanResults.setObjectName("dialogScanResults")
        dialogScanResults.setWindowModality(QtCore.Qt.ApplicationModal)
        dialogScanResults.resize(952, 517)
        self.btnExtractTxt = QtGui.QPushButton(dialogScanResults)
        self.btnExtractTxt.setGeometry(QtCore.QRect(330, 390, 311, 51))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnExtractTxt.setFont(font)
        self.btnExtractTxt.setObjectName("btnExtractTxt")
        self.btnExit = QtGui.QPushButton(dialogScanResults)
        self.btnExit.setGeometry(QtCore.QRect(410, 450, 141, 51))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")
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
        self.btnExtractTxt.setText(QtGui.QApplication.translate("dialogScanResults", "Εξαγωγή Αποτελεσμάτων σε .txt αρχείο", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("dialogScanResults", "Έξοδος", None, QtGui.QApplication.UnicodeUTF8))

