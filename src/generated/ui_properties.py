# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../rsrc/forms/ui_properties.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgProperties(object):
    def setupUi(self, DlgProperties):
        DlgProperties.setObjectName("DlgProperties")
        DlgProperties.resize(324, 214)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("://images/22x22/pfft-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DlgProperties.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(DlgProperties)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(DlgProperties)
        self.listView.setMidLineWidth(0)
        self.listView.setModelColumn(0)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgProperties)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DlgProperties)
        self.buttonBox.rejected.connect(DlgProperties.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgProperties)

    def retranslateUi(self, DlgProperties):
        _translate = QtCore.QCoreApplication.translate
        DlgProperties.setWindowTitle(_translate("DlgProperties", "Dialog"))

import resources_rc
