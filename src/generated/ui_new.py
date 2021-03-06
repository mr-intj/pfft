# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../rsrc/forms/ui_new.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgNew(object):
    def setupUi(self, DlgNew):
        DlgNew.setObjectName("DlgNew")
        DlgNew.setWindowModality(QtCore.Qt.ApplicationModal)
        DlgNew.resize(551, 260)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DlgNew.sizePolicy().hasHeightForWidth())
        DlgNew.setSizePolicy(sizePolicy)
        DlgNew.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/32x32/pfft-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DlgNew.setWindowIcon(icon)
        self.formLayout = QtWidgets.QFormLayout(DlgNew)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(9, 9, 9, 7)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.rate_label = QtWidgets.QLabel(DlgNew)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rate_label.sizePolicy().hasHeightForWidth())
        self.rate_label.setSizePolicy(sizePolicy)
        self.rate_label.setObjectName("rate_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rate_label)
        self.rate_horizLayout = QtWidgets.QHBoxLayout()
        self.rate_horizLayout.setSpacing(4)
        self.rate_horizLayout.setObjectName("rate_horizLayout")
        self.rate_comboBox = QtWidgets.QComboBox(DlgNew)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rate_comboBox.sizePolicy().hasHeightForWidth())
        self.rate_comboBox.setSizePolicy(sizePolicy)
        self.rate_comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.rate_comboBox.setEditable(True)
        self.rate_comboBox.setObjectName("rate_comboBox")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_comboBox.addItem("")
        self.rate_horizLayout.addWidget(self.rate_comboBox)
        self.rate_maxfreq_label = QtWidgets.QLabel(DlgNew)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rate_maxfreq_label.setFont(font)
        self.rate_maxfreq_label.setObjectName("rate_maxfreq_label")
        self.rate_horizLayout.addWidget(self.rate_maxfreq_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.rate_horizLayout.addItem(spacerItem)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.rate_horizLayout)
        self.bitd_label = QtWidgets.QLabel(DlgNew)
        self.bitd_label.setObjectName("bitd_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bitd_label)
        self.bitd_horizLayout = QtWidgets.QHBoxLayout()
        self.bitd_horizLayout.setObjectName("bitd_horizLayout")
        self.bitd_16bit_radioButton = QtWidgets.QRadioButton(DlgNew)
        self.bitd_16bit_radioButton.setObjectName("bitd_16bit_radioButton")
        self.bitd_buttonGroup = QtWidgets.QButtonGroup(DlgNew)
        self.bitd_buttonGroup.setObjectName("bitd_buttonGroup")
        self.bitd_buttonGroup.addButton(self.bitd_16bit_radioButton)
        self.bitd_horizLayout.addWidget(self.bitd_16bit_radioButton)
        self.bitd_24bit_radioButton = QtWidgets.QRadioButton(DlgNew)
        self.bitd_24bit_radioButton.setObjectName("bitd_24bit_radioButton")
        self.bitd_buttonGroup.addButton(self.bitd_24bit_radioButton)
        self.bitd_horizLayout.addWidget(self.bitd_24bit_radioButton)
        self.bitd_32bitfloat_radioButton = QtWidgets.QRadioButton(DlgNew)
        self.bitd_32bitfloat_radioButton.setObjectName("bitd_32bitfloat_radioButton")
        self.bitd_buttonGroup.addButton(self.bitd_32bitfloat_radioButton)
        self.bitd_horizLayout.addWidget(self.bitd_32bitfloat_radioButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bitd_horizLayout.addItem(spacerItem1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.bitd_horizLayout)
        self.chan_label = QtWidgets.QLabel(DlgNew)
        self.chan_label.setObjectName("chan_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.chan_label)
        self.chan_horizLayout = QtWidgets.QHBoxLayout()
        self.chan_horizLayout.setObjectName("chan_horizLayout")
        self.chan_1_radioButton = QtWidgets.QRadioButton(DlgNew)
        self.chan_1_radioButton.setObjectName("chan_1_radioButton")
        self.chan_buttonGroup = QtWidgets.QButtonGroup(DlgNew)
        self.chan_buttonGroup.setObjectName("chan_buttonGroup")
        self.chan_buttonGroup.addButton(self.chan_1_radioButton)
        self.chan_horizLayout.addWidget(self.chan_1_radioButton)
        self.chan_2_radioButton = QtWidgets.QRadioButton(DlgNew)
        self.chan_2_radioButton.setObjectName("chan_2_radioButton")
        self.chan_buttonGroup.addButton(self.chan_2_radioButton)
        self.chan_horizLayout.addWidget(self.chan_2_radioButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.chan_horizLayout.addItem(spacerItem2)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.chan_horizLayout)
        self.idur_label = QtWidgets.QLabel(DlgNew)
        self.idur_label.setObjectName("idur_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.idur_label)
        self.idur_gridLayout = QtWidgets.QGridLayout()
        self.idur_gridLayout.setObjectName("idur_gridLayout")
        self.idur_mins_spinBox = PaddedSpinBox(DlgNew)
        self.idur_mins_spinBox.setMinimumSize(QtCore.QSize(74, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idur_mins_spinBox.setFont(font)
        self.idur_mins_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.idur_mins_spinBox.setSuffix("")
        self.idur_mins_spinBox.setMaximum(59)
        self.idur_mins_spinBox.setObjectName("idur_mins_spinBox")
        self.idur_gridLayout.addWidget(self.idur_mins_spinBox, 1, 2, 1, 1)
        self.idur_msec_spinBox = PaddedSpinBox(DlgNew)
        self.idur_msec_spinBox.setMinimumSize(QtCore.QSize(74, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idur_msec_spinBox.setFont(font)
        self.idur_msec_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.idur_msec_spinBox.setSuffix("")
        self.idur_msec_spinBox.setMaximum(999)
        self.idur_msec_spinBox.setObjectName("idur_msec_spinBox")
        self.idur_gridLayout.addWidget(self.idur_msec_spinBox, 1, 6, 1, 1)
        self.idur_hrs_spinBox = PaddedSpinBox(DlgNew)
        self.idur_hrs_spinBox.setMinimumSize(QtCore.QSize(74, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idur_hrs_spinBox.setFont(font)
        self.idur_hrs_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.idur_hrs_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.idur_hrs_spinBox.setSuffix("")
        self.idur_hrs_spinBox.setPrefix("")
        self.idur_hrs_spinBox.setMaximum(2)
        self.idur_hrs_spinBox.setObjectName("idur_hrs_spinBox")
        self.idur_gridLayout.addWidget(self.idur_hrs_spinBox, 1, 0, 1, 1)
        self.idur_in_mem_label = QtWidgets.QLabel(DlgNew)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.idur_in_mem_label.setFont(font)
        self.idur_in_mem_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.idur_in_mem_label.setObjectName("idur_in_mem_label")
        self.idur_gridLayout.addWidget(self.idur_in_mem_label, 4, 0, 1, 7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.idur_gridLayout.addItem(spacerItem3, 1, 7, 1, 1)
        self.idur_secs_spinBox = PaddedSpinBox(DlgNew)
        self.idur_secs_spinBox.setMinimumSize(QtCore.QSize(74, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idur_secs_spinBox.setFont(font)
        self.idur_secs_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.idur_secs_spinBox.setSuffix("")
        self.idur_secs_spinBox.setMaximum(59)
        self.idur_secs_spinBox.setObjectName("idur_secs_spinBox")
        self.idur_gridLayout.addWidget(self.idur_secs_spinBox, 1, 4, 1, 1)
        self.idur_colon1_label = QtWidgets.QLabel(DlgNew)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idur_colon1_label.setFont(font)
        self.idur_colon1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.idur_colon1_label.setObjectName("idur_colon1_label")
        self.idur_gridLayout.addWidget(self.idur_colon1_label, 1, 1, 1, 1)
        self.idur_colon2_label = QtWidgets.QLabel(DlgNew)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idur_colon2_label.setFont(font)
        self.idur_colon2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.idur_colon2_label.setObjectName("idur_colon2_label")
        self.idur_gridLayout.addWidget(self.idur_colon2_label, 1, 3, 1, 1)
        self.idur_slider = QtWidgets.QSlider(DlgNew)
        self.idur_slider.setMinimumSize(QtCore.QSize(0, 0))
        self.idur_slider.setOrientation(QtCore.Qt.Horizontal)
        self.idur_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.idur_slider.setTickInterval(5)
        self.idur_slider.setObjectName("idur_slider")
        self.idur_gridLayout.addWidget(self.idur_slider, 3, 0, 1, 7)
        self.idur_colon3_label = QtWidgets.QLabel(DlgNew)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idur_colon3_label.setFont(font)
        self.idur_colon3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.idur_colon3_label.setObjectName("idur_colon3_label")
        self.idur_gridLayout.addWidget(self.idur_colon3_label, 1, 5, 1, 1)
        self.idur_hrs_label = QtWidgets.QLabel(DlgNew)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.idur_hrs_label.setFont(font)
        self.idur_hrs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.idur_hrs_label.setObjectName("idur_hrs_label")
        self.idur_gridLayout.addWidget(self.idur_hrs_label, 2, 0, 1, 1)
        self.idur_mins_label = QtWidgets.QLabel(DlgNew)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.idur_mins_label.setFont(font)
        self.idur_mins_label.setAlignment(QtCore.Qt.AlignCenter)
        self.idur_mins_label.setObjectName("idur_mins_label")
        self.idur_gridLayout.addWidget(self.idur_mins_label, 2, 2, 1, 1)
        self.idur_secs_label = QtWidgets.QLabel(DlgNew)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.idur_secs_label.setFont(font)
        self.idur_secs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.idur_secs_label.setObjectName("idur_secs_label")
        self.idur_gridLayout.addWidget(self.idur_secs_label, 2, 4, 1, 1)
        self.idur_msec_label = QtWidgets.QLabel(DlgNew)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.idur_msec_label.setFont(font)
        self.idur_msec_label.setAlignment(QtCore.Qt.AlignCenter)
        self.idur_msec_label.setObjectName("idur_msec_label")
        self.idur_gridLayout.addWidget(self.idur_msec_label, 2, 6, 1, 1)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.idur_gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgNew)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.rate_label.setBuddy(self.rate_comboBox)
        self.idur_label.setBuddy(self.idur_hrs_spinBox)

        self.retranslateUi(DlgNew)
        self.buttonBox.accepted.connect(DlgNew.accept)
        self.buttonBox.rejected.connect(DlgNew.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgNew)
        DlgNew.setTabOrder(self.idur_hrs_spinBox, self.idur_mins_spinBox)
        DlgNew.setTabOrder(self.idur_mins_spinBox, self.idur_secs_spinBox)
        DlgNew.setTabOrder(self.idur_secs_spinBox, self.idur_msec_spinBox)
        DlgNew.setTabOrder(self.idur_msec_spinBox, self.idur_slider)

    def retranslateUi(self, DlgNew):
        _translate = QtCore.QCoreApplication.translate
        DlgNew.setWindowTitle(_translate("DlgNew", "Dialog"))
        self.rate_label.setText(_translate("DlgNew", "&Sampling rate:"))
        self.rate_comboBox.setItemText(0, _translate("DlgNew", "8000 Hz"))
        self.rate_comboBox.setItemText(1, _translate("DlgNew", "11025 Hz"))
        self.rate_comboBox.setItemText(2, _translate("DlgNew", "16000 Hz"))
        self.rate_comboBox.setItemText(3, _translate("DlgNew", "22050 Hz"))
        self.rate_comboBox.setItemText(4, _translate("DlgNew", "32000 Hz"))
        self.rate_comboBox.setItemText(5, _translate("DlgNew", "44100 Hz"))
        self.rate_comboBox.setItemText(6, _translate("DlgNew", "48000 Hz"))
        self.rate_comboBox.setItemText(7, _translate("DlgNew", "64000 Hz"))
        self.rate_comboBox.setItemText(8, _translate("DlgNew", "88200 Hz"))
        self.rate_comboBox.setItemText(9, _translate("DlgNew", "96000 Hz"))
        self.rate_maxfreq_label.setText(_translate("DlgNew", "(maximum frequency {} kHz)"))
        self.bitd_label.setText(_translate("DlgNew", "&Bit depth:"))
        self.bitd_16bit_radioButton.setText(_translate("DlgNew", "1&6-bit"))
        self.bitd_24bit_radioButton.setText(_translate("DlgNew", "2&4-bit"))
        self.bitd_32bitfloat_radioButton.setText(_translate("DlgNew", "&32-bit float"))
        self.chan_label.setText(_translate("DlgNew", "&Number of channels:"))
        self.chan_1_radioButton.setText(_translate("DlgNew", "&1 channel (Mono)"))
        self.chan_2_radioButton.setText(_translate("DlgNew", "&2 channels (Stereo)"))
        self.idur_label.setText(_translate("DlgNew", "&Initial duration:"))
        self.idur_in_mem_label.setText(_translate("DlgNew", "In-memory size: n.nn MB"))
        self.idur_colon1_label.setText(_translate("DlgNew", ":"))
        self.idur_colon2_label.setText(_translate("DlgNew", ":"))
        self.idur_colon3_label.setText(_translate("DlgNew", "."))
        self.idur_hrs_label.setText(_translate("DlgNew", "hrs"))
        self.idur_mins_label.setText(_translate("DlgNew", "mins"))
        self.idur_secs_label.setText(_translate("DlgNew", "secs"))
        self.idur_msec_label.setText(_translate("DlgNew", "msec"))

from widgets.padded_spinbox import PaddedSpinBox
import resources_rc
