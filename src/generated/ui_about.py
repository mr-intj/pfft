# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../rsrc/forms/ui_about.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(454, 171)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(454, 171))
        Dialog.setMaximumSize(QtCore.QSize(454, 171))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("://images/22x22/pfft-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_logo = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_logo.sizePolicy().hasHeightForWidth())
        self.widget_logo.setSizePolicy(sizePolicy)
        self.widget_logo.setMinimumSize(QtCore.QSize(96, 96))
        self.widget_logo.setMaximumSize(QtCore.QSize(96, 96))
        self.widget_logo.setBaseSize(QtCore.QSize(0, 0))
        self.widget_logo.setStyleSheet("background-image: url(resources/images/pfft-logo.png)")
        self.widget_logo.setObjectName("widget_logo")
        self.gridLayout.addWidget(self.widget_logo, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_line1 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_line1.setFont(font)
        self.label_line1.setObjectName("label_line1")
        self.verticalLayout.addWidget(self.label_line1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_line2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_line2.setFont(font)
        self.label_line2.setObjectName("label_line2")
        self.verticalLayout.addWidget(self.label_line2)
        self.label_line3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_line3.setFont(font)
        self.label_line3.setTextFormat(QtCore.Qt.RichText)
        self.label_line3.setObjectName("label_line3")
        self.verticalLayout.addWidget(self.label_line3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About Pfft"))
        self.label_line1.setText(_translate("Dialog", "Pfft 0.1.0"))
        self.label_line2.setText(_translate("Dialog", "Python FFT audio spectrogram editor"))
        self.label_line3.setText(_translate("Dialog", "Copyright © 2017 <a href=\"http://github.com/mr-intj/pfft\">github.com/mr-intj</a>"))

import resources_rc
