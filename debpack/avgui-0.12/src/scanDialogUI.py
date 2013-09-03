# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanDialog.ui'
#
# Created: Wed Aug 28 18:50:50 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_scanDialog(object):
    def setupUi(self, scanDialog):
        scanDialog.setObjectName("scanDialog")
        scanDialog.setWindowModality(QtCore.Qt.NonModal)
        scanDialog.resize(500, 360)
        scanDialog.setMinimumSize(QtCore.QSize(500, 360))
        scanDialog.setMaximumSize(QtCore.QSize(500, 360))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        scanDialog.setWindowIcon(icon)
        scanDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        scanDialog.setAutoFillBackground(False)
        self.avgLabel = QtGui.QLabel(scanDialog)
        self.avgLabel.setGeometry(QtCore.QRect(0, 0, 91, 41))
        self.avgLabel.setText("")
        self.avgLabel.setPixmap(QtGui.QPixmap(":/logo.png"))
        self.avgLabel.setScaledContents(True)
        self.avgLabel.setObjectName("avgLabel")
        self.verticalLayoutWidget = QtGui.QWidget(scanDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 20, 302, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnBeginScan = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBeginScan.sizePolicy().hasHeightForWidth())
        self.btnBeginScan.setSizePolicy(sizePolicy)
        self.btnBeginScan.setMinimumSize(QtCore.QSize(300, 50))
        self.btnBeginScan.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnBeginScan.setFont(font)
        self.btnBeginScan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnBeginScan.setLocale(QtCore.QLocale(QtCore.QLocale.Greek, QtCore.QLocale.Greece))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/scan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBeginScan.setIcon(icon1)
        self.btnBeginScan.setIconSize(QtCore.QSize(32, 32))
        self.btnBeginScan.setAutoDefault(False)
        self.btnBeginScan.setObjectName("btnBeginScan")
        self.verticalLayout.addWidget(self.btnBeginScan)
        self.btnScanSettings = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnScanSettings.sizePolicy().hasHeightForWidth())
        self.btnScanSettings.setSizePolicy(sizePolicy)
        self.btnScanSettings.setMinimumSize(QtCore.QSize(300, 50))
        self.btnScanSettings.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnScanSettings.setFont(font)
        self.btnScanSettings.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnScanSettings.setLocale(QtCore.QLocale(QtCore.QLocale.Greek, QtCore.QLocale.Greece))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/scanSettings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnScanSettings.setIcon(icon2)
        self.btnScanSettings.setIconSize(QtCore.QSize(32, 32))
        self.btnScanSettings.setAutoDefault(False)
        self.btnScanSettings.setObjectName("btnScanSettings")
        self.verticalLayout.addWidget(self.btnScanSettings)
        self.btnSelectF = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSelectF.sizePolicy().hasHeightForWidth())
        self.btnSelectF.setSizePolicy(sizePolicy)
        self.btnSelectF.setMinimumSize(QtCore.QSize(300, 50))
        self.btnSelectF.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnSelectF.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSelectF.setIcon(icon3)
        self.btnSelectF.setIconSize(QtCore.QSize(32, 32))
        self.btnSelectF.setAutoDefault(False)
        self.btnSelectF.setObjectName("btnSelectF")
        self.verticalLayout.addWidget(self.btnSelectF)
        self.labelLogo = QtGui.QLabel(scanDialog)
        self.labelLogo.setGeometry(QtCore.QRect(0, 0, 91, 41))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap(":/avg_logo.png"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setObjectName("labelLogo")
        self.fileToScanLabel = QtGui.QLabel(scanDialog)
        self.fileToScanLabel.setGeometry(QtCore.QRect(0, 220, 500, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileToScanLabel.sizePolicy().hasHeightForWidth())
        self.fileToScanLabel.setSizePolicy(sizePolicy)
        self.fileToScanLabel.setMinimumSize(QtCore.QSize(500, 50))
        self.fileToScanLabel.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.fileToScanLabel.setFont(font)
        self.fileToScanLabel.setStyleSheet("QLabel#fileToScanLabel {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"}")
        self.fileToScanLabel.setFrameShape(QtGui.QFrame.Panel)
        self.fileToScanLabel.setFrameShadow(QtGui.QFrame.Raised)
        self.fileToScanLabel.setLineWidth(0)
        self.fileToScanLabel.setMidLineWidth(0)
        self.fileToScanLabel.setTextFormat(QtCore.Qt.RichText)
        self.fileToScanLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fileToScanLabel.setWordWrap(True)
        self.fileToScanLabel.setObjectName("fileToScanLabel")
        self.exitButton = QtGui.QPushButton(scanDialog)
        self.exitButton.setGeometry(QtCore.QRect(180, 290, 131, 41))
        self.exitButton.setAutoDefault(False)
        self.exitButton.setObjectName("exitButton")
        self.infoLabel = QtGui.QLabel(scanDialog)
        self.infoLabel.setGeometry(QtCore.QRect(100, 210, 301, 20))
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")

        self.retranslateUi(scanDialog)
        QtCore.QMetaObject.connectSlotsByName(scanDialog)

    def retranslateUi(self, scanDialog):
        scanDialog.setWindowTitle(QtGui.QApplication.translate("scanDialog", "Αναζήτηση Ιών", None, QtGui.QApplication.UnicodeUTF8))
        scanDialog.setToolTip(QtGui.QApplication.translate("scanDialog", "Εκκίνηση Αναζήτησης", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBeginScan.setText(QtGui.QApplication.translate("scanDialog", "Έναρξη Αναζήτησης", None, QtGui.QApplication.UnicodeUTF8))
        self.btnScanSettings.setText(QtGui.QApplication.translate("scanDialog", "Ρυθμίσεις Αναζήτησης", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectF.setToolTip(QtGui.QApplication.translate("scanDialog", "Επιλογή Αρχείων / Φακέλων", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectF.setText(QtGui.QApplication.translate("scanDialog", "Επιλογή Αρχείων", None, QtGui.QApplication.UnicodeUTF8))
        self.fileToScanLabel.setToolTip(QtGui.QApplication.translate("scanDialog", "Αρχεία / Φάκελοι για αναζήτηση κακόβουλου λογισμικού", None, QtGui.QApplication.UnicodeUTF8))
        self.fileToScanLabel.setText(QtGui.QApplication.translate("scanDialog", "Δεν έχουν επιλεγεί αρχεία / φάκελοι", None, QtGui.QApplication.UnicodeUTF8))
        self.exitButton.setToolTip(QtGui.QApplication.translate("scanDialog", "Κλείσιμο Παραθύρου", None, QtGui.QApplication.UnicodeUTF8))
        self.exitButton.setText(QtGui.QApplication.translate("scanDialog", "Έξοδος", None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
import avg_rc
import avg_rc
