# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri May 16 13:00:24 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import conf.language.lang as langmodule

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 455)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(766, 455))
        MainWindow.setMaximumSize(QtCore.QSize(766, 455))
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 40, 631, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnScan = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnScan.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnScan.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/scan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnScan.setIcon(icon1)
        self.btnScan.setIconSize(QtCore.QSize(64, 64))
        self.btnScan.setObjectName("btnScan")
        self.gridLayout.addWidget(self.btnScan, 0, 0, 1, 1)
        self.btnUpdate = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnUpdate.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnUpdate.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpdate.setIcon(icon2)
        self.btnUpdate.setIconSize(QtCore.QSize(64, 64))
        self.btnUpdate.setObjectName("btnUpdate")
        self.gridLayout.addWidget(self.btnUpdate, 1, 0, 1, 1)
        self.btnStatus = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnStatus.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnStatus.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/status.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStatus.setIcon(icon3)
        self.btnStatus.setIconSize(QtCore.QSize(64, 64))
        self.btnStatus.setObjectName("btnStatus")
        self.gridLayout.addWidget(self.btnStatus, 1, 1, 1, 1)
        self.btnHistory = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnHistory.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnHistory.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHistory.setIcon(icon4)
        self.btnHistory.setIconSize(QtCore.QSize(64, 64))
        self.btnHistory.setObjectName("btnHistory")
        self.gridLayout.addWidget(self.btnHistory, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 0, 161, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 10, 121, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/avg_logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.btnExitMain = QtGui.QPushButton(self.centralwidget)
        self.btnExitMain.setGeometry(QtCore.QRect(300, 340, 181, 51))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnExitMain.setFont(font)
        self.btnExitMain.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/power_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExitMain.setIcon(icon5)
        self.btnExitMain.setObjectName("btnExitMain")
        self.comLangsel = QtGui.QComboBox(self.centralwidget)
        self.comLangsel.setGeometry(QtCore.QRect(680, 10, 78, 27))
        self.comLangsel.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.comLangsel.setObjectName("comLangsel")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/flagGreece.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comLangsel.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/flagUK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comLangsel.addItem(icon7, "")
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
        self.action_AVGui = QtGui.QAction(MainWindow)
        self.action_AVGui.setObjectName("action_AVGui")
        self.menu.addAction(self.action_AVG)
        self.menu.addAction(self.action_AVGui)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", langmodule.mainWindowTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnScan.setText(QtGui.QApplication.translate("MainWindow", langmodule.btnMainScanTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnUpdate.setText(QtGui.QApplication.translate("MainWindow", langmodule.btnMainUpdateTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnStatus.setText(QtGui.QApplication.translate("MainWindow", langmodule.btnMainStatusTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnHistory.setText(QtGui.QApplication.translate("MainWindow", langmodule.btnMainHistoryTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnExitMain.setText(QtGui.QApplication.translate("MainWindow", langmodule.btnExitTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.comLangsel.setItemText(0, QtGui.QApplication.translate("MainWindow", "EL", None, QtGui.QApplication.UnicodeUTF8))
        self.comLangsel.setItemText(1, QtGui.QApplication.translate("MainWindow", "EN", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", langmodule.lblAbout, None, QtGui.QApplication.UnicodeUTF8))
        self.action_AVG.setText(QtGui.QApplication.translate("MainWindow", langmodule.lblAvgProtectionTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.action_AVGui.setText(QtGui.QApplication.translate("MainWindow", langmodule.lblGraphicFrameworkTitle, None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
