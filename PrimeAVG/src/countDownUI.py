# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'countDown.ui'
#
# Created: Thu Jan 23 20:22:29 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import conf.language.lang as langmodule

class Ui_formCountDown(object):
    def setupUi(self, formCountDown):
        formCountDown.setObjectName("formCountDown")
        formCountDown.setWindowModality(QtCore.Qt.WindowModal)
        formCountDown.resize(564, 119)
        formCountDown.setMinimumSize(QtCore.QSize(564, 119))
        formCountDown.setMaximumSize(QtCore.QSize(564, 119))
        self.countDownLCD = QtGui.QLCDNumber(formCountDown)
        self.countDownLCD.setGeometry(QtCore.QRect(200, 70, 141, 31))
        self.countDownLCD.setProperty("value", 30.0)
        self.countDownLCD.setObjectName("countDownLCD")
        self.lblCountDown = QtGui.QLabel(formCountDown)
        self.lblCountDown.setGeometry(QtCore.QRect(40, 10, 501, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblCountDown.setFont(font)
        self.lblCountDown.setObjectName("lblCountDown")
        self.lblTimeToCompletion = QtGui.QLabel(formCountDown)
        self.lblTimeToCompletion.setGeometry(QtCore.QRect(100, 40, 381, 17))
        self.lblTimeToCompletion.setObjectName("lblTimeToCompletion")

        self.retranslateUi(formCountDown)
        QtCore.QMetaObject.connectSlotsByName(formCountDown)

    def retranslateUi(self, formCountDown):
        formCountDown.setWindowTitle(QtGui.QApplication.translate("formCountDown", langmodule.formCountDownTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.lblCountDown.setText(QtGui.QApplication.translate("formCountDown", langmodule.lblCountDownTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.lblTimeToCompletion.setText(QtGui.QApplication.translate("formCountDown", langmodule.lblCountDownTimeToCompletionTitle, None, QtGui.QApplication.UnicodeUTF8))

