# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../rsrc/forms/ui_about.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgAbout(object):
    def setupUi(self, DlgAbout):
        DlgAbout.setObjectName("DlgAbout")
        DlgAbout.setWindowModality(QtCore.Qt.ApplicationModal)
        DlgAbout.resize(454, 171)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DlgAbout.sizePolicy().hasHeightForWidth())
        DlgAbout.setSizePolicy(sizePolicy)
        DlgAbout.setMinimumSize(QtCore.QSize(454, 171))
        DlgAbout.setMaximumSize(QtCore.QSize(454, 171))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("://images/22x22/pfft-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DlgAbout.setWindowIcon(icon)
        DlgAbout.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(DlgAbout)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_logo = QtWidgets.QWidget(DlgAbout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_logo.sizePolicy().hasHeightForWidth())
        self.widget_logo.setSizePolicy(sizePolicy)
        self.widget_logo.setMinimumSize(QtCore.QSize(96, 96))
        self.widget_logo.setMaximumSize(QtCore.QSize(96, 96))
        self.widget_logo.setBaseSize(QtCore.QSize(0, 0))
        self.widget_logo.setStyleSheet("background-image: url(rsrc/images/pfft-logo.png)")
        self.widget_logo.setObjectName("widget_logo")
        self.gridLayout.addWidget(self.widget_logo, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_line1 = QtWidgets.QLabel(DlgAbout)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_line1.setFont(font)
        self.label_line1.setObjectName("label_line1")
        self.verticalLayout.addWidget(self.label_line1)
        self.line = QtWidgets.QFrame(DlgAbout)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_line2 = QtWidgets.QLabel(DlgAbout)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_line2.setFont(font)
        self.label_line2.setObjectName("label_line2")
        self.verticalLayout.addWidget(self.label_line2)
        self.label_line3 = QtWidgets.QLabel(DlgAbout)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_line3.setFont(font)
        self.label_line3.setTextFormat(QtCore.Qt.RichText)
        self.label_line3.setObjectName("label_line3")
        self.verticalLayout.addWidget(self.label_line3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgAbout)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(DlgAbout)
        self.buttonBox.rejected.connect(DlgAbout.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgAbout)

    def retranslateUi(self, DlgAbout):
        _translate = QtCore.QCoreApplication.translate
        DlgAbout.setWindowTitle(_translate("DlgAbout", "About Pfft"))
        self.label_line1.setText(_translate("DlgAbout", "Pfft 0.1.0"))
        self.label_line2.setText(_translate("DlgAbout", "Python FFT audio spectrogram editor"))
        self.label_line3.setText(_translate("DlgAbout", "Copyright © 2017 <a href=\"http://github.com/mr-intj/pfft\">github.com/mr-intj</a>"))

import resources_rc
