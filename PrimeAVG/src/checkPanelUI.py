# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkPanel.ui'
#
# Created: Tue Jan 21 12:14:57 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import conf.language.lang as langmodule

class Ui_formCheck(object):
    def setupUi(self, formCheck):
        formCheck.setObjectName("formCheck")
        formCheck.setEnabled(True)
        formCheck.resize(759, 414)
        self.txtCheck = QtGui.QPlainTextEdit(formCheck)
        self.txtCheck.setGeometry(QtCore.QRect(10, 10, 741, 341))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.txtCheck.setFont(font)
        self.txtCheck.setObjectName("txtCheck")
        self.btnExit = QtGui.QPushButton(formCheck)
        self.btnExit.setGeometry(QtCore.QRect(297, 356, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")

        self.retranslateUi(formCheck)
        QtCore.QMetaObject.connectSlotsByName(formCheck)

    def retranslateUi(self, formCheck):
        formCheck.setWindowTitle(QtGui.QApplication.translate("formCheck", langmodule.formCheckTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("formCheck", langmodule.btnExitFormCheckTitle, None, QtGui.QApplication.UnicodeUTF8))

