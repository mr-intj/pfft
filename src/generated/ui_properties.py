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
        DlgProperties.resize(338, 175)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("://images/22x22/pfft-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DlgProperties.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(DlgProperties)
        self.verticalLayout.setContentsMargins(7, 10, 7, 7)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(DlgProperties)
        self.tableWidget.setMinimumSize(QtCore.QSize(320, 128))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(24)
        self.verticalLayout.addWidget(self.tableWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgProperties)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 324))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DlgProperties)
        self.buttonBox.rejected.connect(DlgProperties.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgProperties)

    def retranslateUi(self, DlgProperties):
        _translate = QtCore.QCoreApplication.translate
        DlgProperties.setWindowTitle(_translate("DlgProperties", "Properties"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("DlgProperties", "Sampling rate"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("DlgProperties", "(dynamic)"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("DlgProperties", "Bit depth"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("DlgProperties", "(dynamic)"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("DlgProperties", "Number of channels"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("DlgProperties", "(dynamic)"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("DlgProperties", "Duration"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("DlgProperties", "(dynamic)"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

import resources_rc
