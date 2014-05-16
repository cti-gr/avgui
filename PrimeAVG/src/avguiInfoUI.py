# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'avguiinfo.ui'
#
# Created: Fri May 16 12:06:55 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(663, 349)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 621, 71))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(113, 190, 241, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/espa_logo.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(393, 160, 141, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/cti_logo_gr.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 300, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 621, 71))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "To AVGui αναπτύχθηκε από το Ινστιτούτο Τεχνολογίας Υπολογιστών και Εκδόσεων ΔΙΟΦΑΝΤΟΣ στα πλαίσια του έργου \"Ολοκληρωμένες Υπηρεσίες Ενίσχυσης Ψηφιακής Εμπιστοσύνης\" του Επιχειρισιακού Προγράμματος Ψηφιακή Σύγκλιση", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "To AVGui διατίθεται με άδεια GPLv3", None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
