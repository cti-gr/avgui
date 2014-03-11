# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created: Thu Feb 20 13:12:19 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dialogRegistration(object):
    def setupUi(self, dialogRegistration):
        dialogRegistration.setObjectName("dialogRegistration")
        dialogRegistration.setWindowModality(QtCore.Qt.ApplicationModal)
        dialogRegistration.resize(504, 258)
        self.gridLayoutWidget = QtGui.QWidget(dialogRegistration)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 100, 461, 95))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lblEmail = QtGui.QLabel(self.gridLayoutWidget)
        self.lblEmail.setObjectName("lblEmail")
        self.gridLayout.addWidget(self.lblEmail, 0, 0, 1, 1)
        self.lblPassword = QtGui.QLabel(self.gridLayoutWidget)
        self.lblPassword.setObjectName("lblPassword")
        self.gridLayout.addWidget(self.lblPassword, 1, 0, 1, 1)
        self.lblPassword2 = QtGui.QLabel(self.gridLayoutWidget)
        self.lblPassword2.setObjectName("lblPassword2")
        self.gridLayout.addWidget(self.lblPassword2, 2, 0, 1, 1)
        self.txtPassword2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtPassword2.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword2.setObjectName("txtPassword2")
        self.gridLayout.addWidget(self.txtPassword2, 2, 1, 1, 2)
        self.txtPassword = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.gridLayout.addWidget(self.txtPassword, 1, 1, 1, 2)
        self.txtEmail = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtEmail.setObjectName("txtEmail")
        self.gridLayout.addWidget(self.txtEmail, 0, 1, 1, 2)
        self.btnCancel = QtGui.QPushButton(dialogRegistration)
        self.btnCancel.setGeometry(QtCore.QRect(130, 210, 131, 31))
        self.btnCancel.setObjectName("btnCancel")
        self.btnSubmit = QtGui.QPushButton(dialogRegistration)
        self.btnSubmit.setGeometry(QtCore.QRect(270, 210, 131, 31))
        self.btnSubmit.setObjectName("btnSubmit")
        self.label = QtGui.QLabel(dialogRegistration)
        self.label.setGeometry(QtCore.QRect(10, 0, 491, 81))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(dialogRegistration)
        QtCore.QMetaObject.connectSlotsByName(dialogRegistration)

    def retranslateUi(self, dialogRegistration):
        dialogRegistration.setWindowTitle(QtGui.QApplication.translate("dialogRegistration", "Εγγραφή", None, QtGui.QApplication.UnicodeUTF8))
        self.lblEmail.setText(QtGui.QApplication.translate("dialogRegistration", "e-mail", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPassword.setText(QtGui.QApplication.translate("dialogRegistration", "password", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPassword2.setText(QtGui.QApplication.translate("dialogRegistration", "password (confirmation)", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("dialogRegistration", "Ακύρωση", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSubmit.setText(QtGui.QApplication.translate("dialogRegistration", "Υποβολή", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dialogRegistration", "Προσοχή: Για να μπορέσετε να υποβάλλετε αναφορές προβλημάτων πρέπει να ολοκληρώσετε επιτυχώς τη διαδικασία εγγραφής (registration) στο σύστημα.", None, QtGui.QApplication.UnicodeUTF8))

