# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateDialog.ui'
#
# Created: Mon Sep  9 12:17:21 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

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
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(300, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(300, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/watch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(300, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/blueAlert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
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
        self.exitButton = QtGui.QPushButton(updateDialog)
        self.exitButton.setGeometry(QtCore.QRect(140, 230, 111, 41))
        self.exitButton.setAutoDefault(False)
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(updateDialog)
        QtCore.QMetaObject.connectSlotsByName(updateDialog)

    def retranslateUi(self, updateDialog):
        updateDialog.setWindowTitle(QtGui.QApplication.translate("updateDialog", "Ενημέρωση Προγράμματος", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("updateDialog", "Ενημέρωση Προγράμματος", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("updateDialog", "Ρύθμιση Ενημερώσεων", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("updateDialog", "Έλεγχος Κατάστασης", None, QtGui.QApplication.UnicodeUTF8))
        self.exitButton.setText(QtGui.QApplication.translate("updateDialog", "Έξοδος", None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
