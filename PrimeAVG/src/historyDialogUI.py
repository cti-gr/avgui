# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historyDialog.ui'
#
# Created: Thu Jan 23 18:55:42 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import conf.language.lang as langmodule

class Ui_historyDialog(object):
    def setupUi(self, historyDialog):
        historyDialog.setObjectName("historyDialog")
        historyDialog.resize(500, 500)
        historyDialog.setMinimumSize(QtCore.QSize(500, 500))
        historyDialog.setMaximumSize(QtCore.QSize(500, 500))
        self.historyTabWidget = QtGui.QTabWidget(historyDialog)
        self.historyTabWidget.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.historyTabWidget.setMinimumSize(QtCore.QSize(500, 400))
        self.historyTabWidget.setMaximumSize(QtCore.QSize(500, 400))
        self.historyTabWidget.setObjectName("historyTabWidget")
        self.searchTab = QtGui.QWidget()
        self.searchTab.setObjectName("searchTab")
        self.gridLayoutWidget = QtGui.QWidget(self.searchTab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 491, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comMalware = QtGui.QComboBox(self.gridLayoutWidget)
        self.comMalware.setObjectName("comMalware")
        self.gridLayout.addWidget(self.comMalware, 2, 1, 1, 1)
        self.lblTo = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblTo.setFont(font)
        self.lblTo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTo.setObjectName("lblTo")
        self.gridLayout.addWidget(self.lblTo, 1, 0, 1, 1)
        self.comEndDate = QtGui.QDateEdit(self.gridLayoutWidget)
        self.comEndDate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comEndDate.setCalendarPopup(True)
        self.comEndDate.setObjectName("comEndDate")
        self.gridLayout.addWidget(self.comEndDate, 1, 1, 1, 1)
        self.comStartDate = QtGui.QDateEdit(self.gridLayoutWidget)
        self.comStartDate.setCalendarPopup(True)
        self.comStartDate.setObjectName("comStartDate")
        self.gridLayout.addWidget(self.comStartDate, 0, 1, 1, 1)
        self.lblMalware = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblMalware.setFont(font)
        self.lblMalware.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMalware.setObjectName("lblMalware")
        self.gridLayout.addWidget(self.lblMalware, 2, 0, 1, 1)
        self.lblDatabase = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblDatabase.setFont(font)
        self.lblDatabase.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDatabase.setObjectName("lblDatabase")
        self.gridLayout.addWidget(self.lblDatabase, 3, 0, 1, 1)
        self.lblFrom = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFrom.sizePolicy().hasHeightForWidth())
        self.lblFrom.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblFrom.setFont(font)
        self.lblFrom.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFrom.setObjectName("lblFrom")
        self.gridLayout.addWidget(self.lblFrom, 0, 0, 1, 1)
        self.comDatabase = QtGui.QComboBox(self.gridLayoutWidget)
        self.comDatabase.setObjectName("comDatabase")
        self.gridLayout.addWidget(self.comDatabase, 3, 1, 1, 1)
        self.btnExecute = QtGui.QPushButton(self.searchTab)
        self.btnExecute.setGeometry(QtCore.QRect(160, 310, 191, 41))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.btnExecute.setFont(font)
        self.btnExecute.setObjectName("btnExecute")
        self.historyTabWidget.addTab(self.searchTab, "")
        self.upTab = QtGui.QWidget()
        self.upTab.setObjectName("upTab")
        self.btnHistoryDB = QtGui.QPushButton(self.upTab)
        self.btnHistoryDB.setGeometry(QtCore.QRect(100, 150, 291, 61))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnHistoryDB.setFont(font)
        self.btnHistoryDB.setObjectName("btnHistoryDB")
        self.historyTabWidget.addTab(self.upTab, "")
        self.btnExit = QtGui.QPushButton(historyDialog)
        self.btnExit.setGeometry(QtCore.QRect(200, 420, 111, 41))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnExit.setFont(font)
        self.btnExit.setAutoDefault(False)
        self.btnExit.setObjectName("btnExit")

        self.retranslateUi(historyDialog)
        self.historyTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(historyDialog)

    def retranslateUi(self, historyDialog):
        historyDialog.setWindowTitle(QtGui.QApplication.translate("historyDialog", langmodule.dialogHistoryTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.lblTo.setText(QtGui.QApplication.translate("historyDialog", langmodule.lblToTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.comEndDate.setDisplayFormat(QtGui.QApplication.translate("historyDialog", "dd.MM.yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.comStartDate.setDisplayFormat(QtGui.QApplication.translate("historyDialog", "dd.MM.yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMalware.setText(QtGui.QApplication.translate("historyDialog", langmodule.lblMalwareTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.lblDatabase.setText(QtGui.QApplication.translate("historyDialog", langmodule.lblDatabaseTable, None, QtGui.QApplication.UnicodeUTF8))
        self.lblFrom.setText(QtGui.QApplication.translate("historyDialog", langmodule.lblFromTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnExecute.setText(QtGui.QApplication.translate("historyDialog", langmodule.btnExecuteTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.historyTabWidget.setTabText(self.historyTabWidget.indexOf(self.searchTab), QtGui.QApplication.translate("historyDialog", langmodule.historyTabWidgetScansTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnHistoryDB.setText(QtGui.QApplication.translate("historyDialog", langmodule.btnHistoryDBTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.historyTabWidget.setTabText(self.historyTabWidget.indexOf(self.upTab), QtGui.QApplication.translate("historyDialog", langmodule.historyTabWidgetUpdatesTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("historyDialog", langmodule.btnExitHistoryTitle, None, QtGui.QApplication.UnicodeUTF8))

