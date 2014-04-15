# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showScanResults.ui'
#
# Created: Tue Apr 15 18:18:54 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import conf.language.lang as langmodule

class Ui_showScanResultsDialog(object):
    def setupUi(self, showScanResultsDialog):
        showScanResultsDialog.setObjectName("showScanResultsDialog")
        showScanResultsDialog.resize(690, 500)
        showScanResultsDialog.setMinimumSize(QtCore.QSize(690, 500))
        showScanResultsDialog.setMaximumSize(QtCore.QSize(690, 500))
        self.label = QtGui.QLabel(showScanResultsDialog)
        self.label.setGeometry(QtCore.QRect(310, 10, 71, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/attention.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btnExit = QtGui.QPushButton(showScanResultsDialog)
        self.btnExit.setGeometry(QtCore.QRect(270, 440, 151, 51))
        self.btnExit.setObjectName("btnExit")
        self.tableWidget = QtGui.QTableWidget(showScanResultsDialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 140, 671, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.theLabel = QtGui.QLabel(showScanResultsDialog)
        self.theLabel.setGeometry(QtCore.QRect(40, 90, 611, 31))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.theLabel.setFont(font)
        self.theLabel.setStyleSheet("QLabel#theLabel {\n"
"    font-weight: bold;\n"
"    color: red;\n"
"}")
        self.theLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.theLabel.setObjectName("theLabel")

        self.retranslateUi(showScanResultsDialog)
        QtCore.QMetaObject.connectSlotsByName(showScanResultsDialog)

    def retranslateUi(self, showScanResultsDialog):
        showScanResultsDialog.setWindowTitle(QtGui.QApplication.translate("showScanResultsDialog", langmodule.scanResultsDialogTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("showScanResultsDialog", langmodule.btnExitHistoryTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.theLabel.setText(QtGui.QApplication.translate("showScanResultsDialog", langmodule.attentionMsg, None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
import avg_rc
