# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Nov  8 13:57:41 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 470)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(766, 470))
        MainWindow.setMaximumSize(QtCore.QSize(766, 470))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/avg_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QPushButton#btnExitMain { \n"
"border: 1px solid orange;    \n"
"border-radius: 5px ;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 160, 68, 196), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Greek, QtCore.QLocale.Greece))
        MainWindow.setIconSize(QtCore.QSize(64, 24))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 40, 620, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scanBtn = QtGui.QPushButton(self.gridLayoutWidget)
        self.scanBtn.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.scanBtn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/scan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scanBtn.setIcon(icon1)
        self.scanBtn.setIconSize(QtCore.QSize(64, 64))
        self.scanBtn.setObjectName("scanBtn")
        self.gridLayout.addWidget(self.scanBtn, 0, 0, 1, 1)
        self.updateBtn = QtGui.QPushButton(self.gridLayoutWidget)
        self.updateBtn.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.updateBtn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updateBtn.setIcon(icon2)
        self.updateBtn.setIconSize(QtCore.QSize(64, 64))
        self.updateBtn.setObjectName("updateBtn")
        self.gridLayout.addWidget(self.updateBtn, 1, 0, 1, 1)
        self.issueBtn = QtGui.QPushButton(self.gridLayoutWidget)
        self.issueBtn.setMinimumSize(QtCore.QSize(200, 50))
        self.issueBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.issueBtn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/issue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.issueBtn.setIcon(icon3)
        self.issueBtn.setIconSize(QtCore.QSize(32, 32))
        self.issueBtn.setObjectName("issueBtn")
        self.gridLayout.addWidget(self.issueBtn, 2, 0, 1, 2)
        self.settingsBtn = QtGui.QPushButton(self.gridLayoutWidget)
        self.settingsBtn.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.settingsBtn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QtCore.QSize(64, 64))
        self.settingsBtn.setObjectName("settingsBtn")
        self.gridLayout.addWidget(self.settingsBtn, 1, 1, 1, 1)
        self.logBtn = QtGui.QPushButton(self.gridLayoutWidget)
        self.logBtn.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.logBtn.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logBtn.setIcon(icon5)
        self.logBtn.setIconSize(QtCore.QSize(64, 64))
        self.logBtn.setObjectName("logBtn")
        self.gridLayout.addWidget(self.logBtn, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 0, 161, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 0, 121, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/avg_logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.btnExitMain = QtGui.QPushButton(self.centralwidget)
        self.btnExitMain.setGeometry(QtCore.QRect(300, 360, 181, 51))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnExitMain.setFont(font)
        self.btnExitMain.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/power_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExitMain.setIcon(icon6)
        self.btnExitMain.setObjectName("btnExitMain")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_AVG = QtGui.QAction(MainWindow)
        self.action_AVG.setObjectName("action_AVG")
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action_AVG)
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Προστασία από Κακόβουλο Λογισμικό", None, QtGui.QApplication.UnicodeUTF8))
        self.scanBtn.setText(QtGui.QApplication.translate("MainWindow", "Αναζήτηση για Ιούς", None, QtGui.QApplication.UnicodeUTF8))
        self.updateBtn.setText(QtGui.QApplication.translate("MainWindow", "Ενημέρωση Προγράμματος", None, QtGui.QApplication.UnicodeUTF8))
        self.issueBtn.setText(QtGui.QApplication.translate("MainWindow", "Αναφορά Προβλήματος", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsBtn.setText(QtGui.QApplication.translate("MainWindow", "Ρυθμίσεις", None, QtGui.QApplication.UnicodeUTF8))
        self.logBtn.setText(QtGui.QApplication.translate("MainWindow", "Ιστορικό", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExitMain.setText(QtGui.QApplication.translate("MainWindow", "Έξοδος", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "Σχετικά", None, QtGui.QApplication.UnicodeUTF8))
        self.action_AVG.setText(QtGui.QApplication.translate("MainWindow", "Πρόγραμμα ΠροστασίαςAVG", None, QtGui.QApplication.UnicodeUTF8))
        self.action.setText(QtGui.QApplication.translate("MainWindow", "Γραφικό Περιβάλλον", None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
