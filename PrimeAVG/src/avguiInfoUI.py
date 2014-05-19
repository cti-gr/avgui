# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'avguiinfo.ui'
#
# Created: Mon May 19 13:11:41 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import conf.language.lang as langmodule

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(663, 349)
        Dialog.setModal(True)
        self.lblAVGUIinfo1 = QtGui.QLabel(Dialog)
        self.lblAVGUIinfo1.setGeometry(QtCore.QRect(20, 10, 621, 71))
        self.lblAVGUIinfo1.setWordWrap(True)
        self.lblAVGUIinfo1.setObjectName("lblAVGUIinfo1")
        self.lblESPA = QtGui.QLabel(Dialog)
        self.lblESPA.setGeometry(QtCore.QRect(113, 190, 241, 71))
        self.lblESPA.setText("")
        self.lblESPA.setPixmap(QtGui.QPixmap(":/espa_logo.png"))
        self.lblESPA.setObjectName("lblESPA")
        self.lblCTI = QtGui.QLabel(Dialog)
        self.lblCTI.setGeometry(QtCore.QRect(393, 160, 141, 121))
        self.lblCTI.setText("")
        self.lblCTI.setPixmap(QtGui.QPixmap(":/cti_logo_gr.png"))
        self.lblCTI.setScaledContents(True)
        self.lblCTI.setObjectName("lblCTI")
        self.btnExit = QtGui.QPushButton(Dialog)
        self.btnExit.setGeometry(QtCore.QRect(270, 300, 131, 31))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")
        self.lblAVGUIinfo2 = QtGui.QLabel(Dialog)
        self.lblAVGUIinfo2.setGeometry(QtCore.QRect(20, 80, 621, 71))
        self.lblAVGUIinfo2.setWordWrap(True)
        self.lblAVGUIinfo2.setObjectName("lblAVGUIinfo2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAVGUIinfo1.setText(QtGui.QApplication.translate("Dialog", langmodule.mainLabel, None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAVGUIinfo2.setText(QtGui.QApplication.translate("Dialog", langmodule.licenceLabel, None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
