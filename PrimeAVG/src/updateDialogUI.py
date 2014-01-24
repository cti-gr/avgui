# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateDialog.ui'
#
# Created: Thu Jan 23 15:27:56 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import conf.language.lang as langmodule

class Ui_updateDialog(object):
    def setupUi(self, updateDialog):
        updateDialog.setObjectName("updateDialog")
        updateDialog.setWindowModality(QtCore.Qt.NonModal)
        updateDialog.resize(400, 300)
        updateDialog.setMinimumSize(QtCore.QSize(400, 300))
        updateDialog.setMaximumSize(QtCore.QSize(400, 300))
        self.verticalLayoutWidget = QtGui.QWidget(updateDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(51, 30, 302, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnUpdate = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnUpdate.setMinimumSize(QtCore.QSize(300, 50))
        self.btnUpdate.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnUpdate.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpdate.setIcon(icon)
        self.btnUpdate.setIconSize(QtCore.QSize(32, 32))
        self.btnUpdate.setAutoDefault(False)
        self.btnUpdate.setObjectName("btnUpdate")
        self.verticalLayout.addWidget(self.btnUpdate)
        self.btnUpdateSet = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnUpdateSet.setMinimumSize(QtCore.QSize(300, 50))
        self.btnUpdateSet.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnUpdateSet.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/watch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpdateSet.setIcon(icon1)
        self.btnUpdateSet.setIconSize(QtCore.QSize(32, 32))
        self.btnUpdateSet.setAutoDefault(False)
        self.btnUpdateSet.setObjectName("btnUpdateSet")
        self.verticalLayout.addWidget(self.btnUpdateSet)
        self.btnUpdateCheck = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnUpdateCheck.setMinimumSize(QtCore.QSize(300, 50))
        self.btnUpdateCheck.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnUpdateCheck.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/blueAlert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpdateCheck.setIcon(icon2)
        self.btnUpdateCheck.setIconSize(QtCore.QSize(32, 32))
        self.btnUpdateCheck.setAutoDefault(False)
        self.btnUpdateCheck.setObjectName("btnUpdateCheck")
        self.verticalLayout.addWidget(self.btnUpdateCheck)
        self.avgLabel_2 = QtGui.QLabel(updateDialog)
        self.avgLabel_2.setGeometry(QtCore.QRect(0, 0, 91, 41))
        self.avgLabel_2.setText("")
        self.avgLabel_2.setPixmap(QtGui.QPixmap(":/logo.png"))
        self.avgLabel_2.setScaledContents(True)
        self.avgLabel_2.setObjectName("avgLabel_2")
        self.labelLogo = QtGui.QLabel(updateDialog)
        self.labelLogo.setGeometry(QtCore.QRect(0, 0, 91, 41))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap(":/avg_logo.png"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setObjectName("labelLogo")
        self.btnExit = QtGui.QPushButton(updateDialog)
        self.btnExit.setGeometry(QtCore.QRect(140, 230, 111, 41))
        self.btnExit.setAutoDefault(False)
        self.btnExit.setObjectName("btnExit")

        self.retranslateUi(updateDialog)
        QtCore.QMetaObject.connectSlotsByName(updateDialog)

    def retranslateUi(self, updateDialog):
        updateDialog.setWindowTitle(QtGui.QApplication.translate("updateDialog", langmodule.dialogUpdateTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnUpdate.setText(QtGui.QApplication.translate("updateDialog", langmodule.btnUpdateTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnUpdateSet.setText(QtGui.QApplication.translate("updateDialog", langmodule.btnUpdateSetTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnUpdateCheck.setText(QtGui.QApplication.translate("updateDialog", langmodule.btnUpdateCheckTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("updateDialog", langmodule.btnExitUpdateDialogTitle, None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
