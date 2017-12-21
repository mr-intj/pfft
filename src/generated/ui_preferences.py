# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../rsrc/forms/ui_preferences.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgPreferences(object):
    def setupUi(self, DlgPreferences):
        DlgPreferences.setObjectName("DlgPreferences")
        DlgPreferences.setWindowModality(QtCore.Qt.ApplicationModal)
        DlgPreferences.resize(422, 310)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("://images/22x22/pfft-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DlgPreferences.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(DlgPreferences)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(DlgPreferences)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgPreferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DlgPreferences)
        self.buttonBox.accepted.connect(DlgPreferences.accept)
        self.buttonBox.rejected.connect(DlgPreferences.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgPreferences)

    def retranslateUi(self, DlgPreferences):
        _translate = QtCore.QCoreApplication.translate
        DlgPreferences.setWindowTitle(_translate("DlgPreferences", "Preferences - Pfft"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DlgPreferences", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DlgPreferences", "Tab 2"))

import resources_rc
