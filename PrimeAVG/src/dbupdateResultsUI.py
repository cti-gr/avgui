# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbupdateResults.ui'
#
# Created: Thu Nov 14 20:13:34 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dialogDBResults(object):
    def setupUi(self, dialogDBResults):
        dialogDBResults.setObjectName("dialogDBResults")
        dialogDBResults.resize(550, 432)
        dialogDBResults.setMinimumSize(QtCore.QSize(550, 432))
        dialogDBResults.setMaximumSize(QtCore.QSize(550, 432))
        self.horizontalLayoutWidget = QtGui.QWidget(dialogDBResults)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 531, 351))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tblViewHistoryDB = QtGui.QTableView(self.horizontalLayoutWidget)
        self.tblViewHistoryDB.setMinimumSize(QtCore.QSize(525, 0))
        self.tblViewHistoryDB.setAlternatingRowColors(True)
        self.tblViewHistoryDB.setObjectName("tblViewHistoryDB")
        self.tblViewHistoryDB.horizontalHeader().setCascadingSectionResizes(True)
        self.tblViewHistoryDB.horizontalHeader().setDefaultSectionSize(150)
        self.tblViewHistoryDB.horizontalHeader().setMinimumSectionSize(150)
        self.tblViewHistoryDB.horizontalHeader().setStretchLastSection(True)
        self.tblViewHistoryDB.verticalHeader().setCascadingSectionResizes(True)
        self.horizontalLayout.addWidget(self.tblViewHistoryDB)
        self.btnExit = QtGui.QPushButton(dialogDBResults)
        self.btnExit.setGeometry(QtCore.QRect(210, 370, 151, 41))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")

        self.retranslateUi(dialogDBResults)
        QtCore.QMetaObject.connectSlotsByName(dialogDBResults)

    def retranslateUi(self, dialogDBResults):
        dialogDBResults.setWindowTitle(QtGui.QApplication.translate("dialogDBResults", "Ιστορικό Ενημερώσεων Βάσης Ιών", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("dialogDBResults", "Έξοδος", None, QtGui.QApplication.UnicodeUTF8))

