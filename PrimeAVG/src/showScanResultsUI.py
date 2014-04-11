# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showScanResults.ui'
#
# Created: Fri Apr 11 18:45:15 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_showScanResultsDialog(object):
    def setupUi(self, showScanResultsDialog):
        showScanResultsDialog.setObjectName("showScanResultsDialog")
        showScanResultsDialog.resize(472, 399)
        self.listWidget = QtGui.QListWidget(showScanResultsDialog)
        self.listWidget.setGeometry(QtCore.QRect(0, 100, 471, 231))
        self.listWidget.setObjectName("listWidget")
        self.label = QtGui.QLabel(showScanResultsDialog)
        self.label.setGeometry(QtCore.QRect(190, 10, 81, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/attention.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btnExit = QtGui.QPushButton(showScanResultsDialog)
        self.btnExit.setGeometry(QtCore.QRect(180, 340, 131, 51))
        self.btnExit.setObjectName("btnExit")

        self.retranslateUi(showScanResultsDialog)
        QtCore.QMetaObject.connectSlotsByName(showScanResultsDialog)

    def retranslateUi(self, showScanResultsDialog):
        showScanResultsDialog.setWindowTitle(QtGui.QApplication.translate("showScanResultsDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("showScanResultsDialog", "Έξοδος", None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
import avg_rc
