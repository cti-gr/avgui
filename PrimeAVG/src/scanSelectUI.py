# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanSelect.ui'
#
# Created: Wed Jan 22 20:27:07 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import conf.language.lang as langmodule

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
        self.lblScanSelect = QtGui.QLabel(scanSelectDialog)
        self.lblScanSelect.setGeometry(QtCore.QRect(80, 50, 261, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblScanSelect.setFont(font)
        self.lblScanSelect.setObjectName("lblScanSelect")
        self.radioFile = QtGui.QRadioButton(scanSelectDialog)
        self.radioFile.setGeometry(QtCore.QRect(60, 90, 116, 22))
        self.radioFile.setObjectName("radioFile")
        self.radioFolder = QtGui.QRadioButton(scanSelectDialog)
        self.radioFolder.setGeometry(QtCore.QRect(240, 90, 116, 22))
        self.radioFolder.setObjectName("radioFolder")
        self.btnExit = QtGui.QPushButton(scanSelectDialog)
        self.btnExit.setGeometry(QtCore.QRect(150, 130, 101, 41))
        self.btnExit.setAutoDefault(False)
        self.btnExit.setObjectName("btnExit")

        self.retranslateUi(scanSelectDialog)
        QtCore.QMetaObject.connectSlotsByName(scanSelectDialog)

    def retranslateUi(self, scanSelectDialog):
        scanSelectDialog.setWindowTitle(QtGui.QApplication.translate("scanSelectDialog", langmodule.dialogScanSelectTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.lblScanSelect.setText(QtGui.QApplication.translate("scanSelectDialog", langmodule.lblScanSelectTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.radioFile.setText(QtGui.QApplication.translate("scanSelectDialog", langmodule.radioFileTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.radioFolder.setText(QtGui.QApplication.translate("scanSelectDialog", langmodule.radioFolderTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("scanSelectDialog", langmodule.btnExitScanSelectTitle, None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
