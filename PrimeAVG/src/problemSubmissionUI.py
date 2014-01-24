# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'problemSubmission.ui'
#
# Created: Thu Jan 23 21:05:01 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import conf.language.lang as langmodule

class Ui_problemDialog(object):
    def setupUi(self, problemDialog):
        problemDialog.setObjectName("problemDialog")
        problemDialog.resize(502, 822)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        problemDialog.setFont(font)
        self.lblLogo = QtGui.QLabel(problemDialog)
        self.lblLogo.setGeometry(QtCore.QRect(190, 0, 111, 51))
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(":/avg_logo.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setObjectName("lblLogo")
        self.gridLayoutWidget = QtGui.QWidget(problemDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 461, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lblUser = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUser.sizePolicy().hasHeightForWidth())
        self.lblUser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblUser.setFont(font)
        self.lblUser.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblUser.setFrameShadow(QtGui.QFrame.Raised)
        self.lblUser.setLineWidth(1)
        self.lblUser.setMidLineWidth(0)
        self.lblUser.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUser.setObjectName("lblUser")
        self.gridLayout.addWidget(self.lblUser, 2, 0, 1, 2)
        self.lblAvg = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblAvg.setFont(font)
        self.lblAvg.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblAvg.setFrameShadow(QtGui.QFrame.Raised)
        self.lblAvg.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAvg.setObjectName("lblAvg")
        self.gridLayout.addWidget(self.lblAvg, 6, 0, 1, 2)
        self.lblKernel = QtGui.QLabel(self.gridLayoutWidget)
        self.lblKernel.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblKernel.setFrameShadow(QtGui.QFrame.Raised)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblKernel.setFont(font)
        self.lblKernel.setAlignment(QtCore.Qt.AlignCenter)
        self.lblKernel.setObjectName("lblKernel")
        self.gridLayout.addWidget(self.lblKernel, 4, 0, 1, 2)
        self.lblUbuntu = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblUbuntu.setFont(font)
        self.lblUbuntu.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblUbuntu.setFrameShadow(QtGui.QFrame.Raised)
        self.lblUbuntu.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUbuntu.setObjectName("lblUbuntu")
        self.gridLayout.addWidget(self.lblUbuntu, 3, 0, 1, 2)
        self.lblUserValue = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUserValue.sizePolicy().hasHeightForWidth())
        self.lblUserValue.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblUserValue.setFont(font)
        self.lblUserValue.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblUserValue.setFrameShadow(QtGui.QFrame.Raised)
        self.lblUserValue.setText("")
        self.lblUserValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUserValue.setObjectName("lblUserValue")
        self.gridLayout.addWidget(self.lblUserValue, 2, 2, 1, 1)
        self.lblKernelValue = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblKernelValue.setFont(font)
        self.lblKernelValue.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblKernelValue.setFrameShadow(QtGui.QFrame.Raised)
        self.lblKernelValue.setText("")
        self.lblKernelValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblKernelValue.setObjectName("lblKernelValue")
        self.gridLayout.addWidget(self.lblKernelValue, 4, 2, 1, 1)
        self.lblUbuntuValue = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblUbuntuValue.setFont(font)
        self.lblUbuntuValue.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblUbuntuValue.setFrameShadow(QtGui.QFrame.Raised)
        self.lblUbuntuValue.setText("")
        self.lblUbuntuValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUbuntuValue.setObjectName("lblUbuntuValue")
        self.gridLayout.addWidget(self.lblUbuntuValue, 3, 2, 1, 1)
        self.lblAvguiValue = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblAvguiValue.setFont(font)
        self.lblAvguiValue.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblAvguiValue.setFrameShadow(QtGui.QFrame.Raised)
        self.lblAvguiValue.setText("")
        self.lblAvguiValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAvguiValue.setObjectName("lblAvguiValue")
        self.gridLayout.addWidget(self.lblAvguiValue, 5, 2, 1, 1)
        self.lblAvgValue = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblAvgValue.setFont(font)
        self.lblAvgValue.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblAvgValue.setFrameShadow(QtGui.QFrame.Raised)
        self.lblAvgValue.setText("")
        self.lblAvgValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAvgValue.setObjectName("lblAvgValue")
        self.gridLayout.addWidget(self.lblAvgValue, 6, 2, 1, 1)
        self.lblAvgui = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblAvgui.setFont(font)
        self.lblAvgui.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblAvgui.setFrameShadow(QtGui.QFrame.Raised)
        self.lblAvgui.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAvgui.setObjectName("lblAvgui")
        self.gridLayout.addWidget(self.lblAvgui, 5, 0, 1, 2)
        self.btnSubmit = QtGui.QPushButton(problemDialog)
        self.btnSubmit.setGeometry(QtCore.QRect(110, 760, 141, 41))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnSubmit.setFont(font)
        self.btnSubmit.setObjectName("btnSubmit")
        self.btnCancel = QtGui.QPushButton(problemDialog)
        self.btnCancel.setGeometry(QtCore.QRect(270, 760, 141, 41))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.lblProbDesc = QtGui.QLabel(problemDialog)
        self.lblProbDesc.setGeometry(QtCore.QRect(20, 280, 461, 36))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblProbDesc.sizePolicy().hasHeightForWidth())
        self.lblProbDesc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblProbDesc.setFont(font)
        self.lblProbDesc.setFrameShape(QtGui.QFrame.WinPanel)
        self.lblProbDesc.setFrameShadow(QtGui.QFrame.Raised)
        self.lblProbDesc.setLineWidth(1)
        self.lblProbDesc.setMidLineWidth(0)
        self.lblProbDesc.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProbDesc.setObjectName("lblProbDesc")
        self.txtProbDesc = QtGui.QPlainTextEdit(problemDialog)
        self.txtProbDesc.setGeometry(QtCore.QRect(20, 320, 461, 431))
        self.txtProbDesc.setObjectName("txtProbDesc")

        self.retranslateUi(problemDialog)
        QtCore.QMetaObject.connectSlotsByName(problemDialog)

    def retranslateUi(self, problemDialog):
        problemDialog.setWindowTitle(QtGui.QApplication.translate("problemDialog", langmodule.dialogProblemTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.lblUser.setText(QtGui.QApplication.translate("problemDialog", langmodule.lblUserTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.lblAvg.setText(QtGui.QApplication.translate("problemDialog", langmodule.lblAvgTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.lblKernel.setText(QtGui.QApplication.translate("problemDialog", langmodule.lblKernelTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.lblUbuntu.setText(QtGui.QApplication.translate("problemDialog", langmodule.lblUbuntuTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.lblAvgui.setText(QtGui.QApplication.translate("problemDialog", langmodule.lblAvguiTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.btnSubmit.setText(QtGui.QApplication.translate("problemDialog", langmodule.btnSubmitProblemSubmissionTitle , None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("problemDialog", langmodule.btnCancelProblemSubmissionTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.lblProbDesc.setText(QtGui.QApplication.translate("problemDialog", langmodule.lblProbDescTitle, None, QtGui.QApplication.UnicodeUTF8))

import avg_rc
