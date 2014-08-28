# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'avgavinfo.ui'
#
# Created: Thu Aug 28 08:09:36 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import conf.language.lang as langmodule

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 216)
        Dialog.setMinimumSize(QtCore.QSize(650, 216))
        Dialog.setMaximumSize(QtCore.QSize(650, 216))
        Dialog.setModal(True)
        self.lblAVGinfo1 = QtGui.QLabel(Dialog)
        self.lblAVGinfo1.setGeometry(QtCore.QRect(0, 0, 661, 51))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblAVGinfo1.setFont(font)
        self.lblAVGinfo1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAVGinfo1.setObjectName("lblAVGinfo1")
        self.lblAVGlogo = QtGui.QLabel(Dialog)
        self.lblAVGlogo.setGeometry(QtCore.QRect(220, 80, 211, 81))
        self.lblAVGlogo.setText("")
        self.lblAVGlogo.setPixmap(QtGui.QPixmap(":/avg_logo.png"))
        self.lblAVGlogo.setScaledContents(True)
        self.lblAVGlogo.setObjectName("lblAVGlogo")
        self.btnExit = QtGui.QPushButton(Dialog)
        self.btnExit.setGeometry(QtCore.QRect(270, 170, 111, 31))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")
        self.lblAVGinfo2 = QtGui.QLabel(Dialog)
        self.lblAVGinfo2.setGeometry(QtCore.QRect(140, 40, 381, 51))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblAVGinfo2.setFont(font)
        self.lblAVGinfo2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAVGinfo2.setObjectName("lblAVGinfo2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAVGinfo1.setText(QtGui.QApplication.translate("Dialog", langmodule.lbl1, None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAVGinfo2.setText(QtGui.QApplication.translate("Dialog", langmodule.lbl2, None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
