# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../rsrc/forms/ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 655)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("://images/22x22/pfft-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.gridLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView_wf_l_scale = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_wf_l_scale.setMaximumSize(QtCore.QSize(32, 16777215))
        self.graphicsView_wf_l_scale.setObjectName("graphicsView_wf_l_scale")
        self.gridLayout.addWidget(self.graphicsView_wf_l_scale, 0, 0, 1, 1)
        self.graphicsView_wf_l_disp = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_wf_l_disp.setObjectName("graphicsView_wf_l_disp")
        self.gridLayout.addWidget(self.graphicsView_wf_l_disp, 0, 1, 1, 1)
        self.graphicsView_wf_r_scale = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_wf_r_scale.setMaximumSize(QtCore.QSize(32, 16777215))
        self.graphicsView_wf_r_scale.setObjectName("graphicsView_wf_r_scale")
        self.gridLayout.addWidget(self.graphicsView_wf_r_scale, 1, 0, 1, 1)
        self.graphicsView_wf_r_disp = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_wf_r_disp.setObjectName("graphicsView_wf_r_disp")
        self.gridLayout.addWidget(self.graphicsView_wf_r_disp, 1, 1, 1, 1)
        self.graphicsView_wf_time = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_wf_time.setMaximumSize(QtCore.QSize(16777215, 24))
        self.graphicsView_wf_time.setObjectName("graphicsView_wf_time")
        self.gridLayout.addWidget(self.graphicsView_wf_time, 2, 0, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView_sg_disp = QtWidgets.QGraphicsView(self.gridLayoutWidget_2)
        self.graphicsView_sg_disp.setObjectName("graphicsView_sg_disp")
        self.gridLayout_2.addWidget(self.graphicsView_sg_disp, 0, 1, 1, 1)
        self.graphicsView_sg_scale = QtWidgets.QGraphicsView(self.gridLayoutWidget_2)
        self.graphicsView_sg_scale.setMaximumSize(QtCore.QSize(32, 16777215))
        self.graphicsView_sg_scale.setObjectName("graphicsView_sg_scale")
        self.gridLayout_2.addWidget(self.graphicsView_sg_scale, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalLayout.addWidget(self.horizontalScrollBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 20))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuRecent = QtWidgets.QMenu(self.menu_File)
        self.menuRecent.setObjectName("menuRecent")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Select = QtWidgets.QMenu(self.menubar)
        self.menu_Select.setObjectName("menu_Select")
        self.menu_View = QtWidgets.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        self.menuZoom = QtWidgets.QMenu(self.menu_View)
        self.menuZoom.setObjectName("menuZoom")
        self.menuToolbars = QtWidgets.QMenu(self.menu_View)
        self.menuToolbars.setObjectName("menuToolbars")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFile_New = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("://images/32x32/file-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFile_New.setIcon(icon1)
        self.actionFile_New.setObjectName("actionFile_New")
        self.actionFile_Open = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("://images/32x32/file-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFile_Open.setIcon(icon2)
        self.actionFile_Open.setObjectName("actionFile_Open")
        self.actionFile_OpenRecent_1 = QtWidgets.QAction(MainWindow)
        self.actionFile_OpenRecent_1.setObjectName("actionFile_OpenRecent_1")
        self.actionFile_OpenRecent_2 = QtWidgets.QAction(MainWindow)
        self.actionFile_OpenRecent_2.setObjectName("actionFile_OpenRecent_2")
        self.actionFile_OpenRecent_3 = QtWidgets.QAction(MainWindow)
        self.actionFile_OpenRecent_3.setObjectName("actionFile_OpenRecent_3")
        self.actionFile_OpenRecent_4 = QtWidgets.QAction(MainWindow)
        self.actionFile_OpenRecent_4.setObjectName("actionFile_OpenRecent_4")
        self.actionFile_OpenRecent_5 = QtWidgets.QAction(MainWindow)
        self.actionFile_OpenRecent_5.setObjectName("actionFile_OpenRecent_5")
        self.actionFile_OpenRecent_6 = QtWidgets.QAction(MainWindow)
        self.actionFile_OpenRecent_6.setObjectName("actionFile_OpenRecent_6")
        self.actionFile_OpenRecent_7 = QtWidgets.QAction(MainWindow)
        self.actionFile_OpenRecent_7.setObjectName("actionFile_OpenRecent_7")
        self.actionFile_OpenRecent_8 = QtWidgets.QAction(MainWindow)
        self.actionFile_OpenRecent_8.setObjectName("actionFile_OpenRecent_8")
        self.actionFile_OpenRecent_Clear = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("://images/32x32/edit-delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFile_OpenRecent_Clear.setIcon(icon3)
        self.actionFile_OpenRecent_Clear.setObjectName("actionFile_OpenRecent_Clear")
        self.actionFile_Save = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("://images/32x32/file-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFile_Save.setIcon(icon4)
        self.actionFile_Save.setObjectName("actionFile_Save")
        self.actionFile_SaveAs = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("://images/32x32/file-save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFile_SaveAs.setIcon(icon5)
        self.actionFile_SaveAs.setObjectName("actionFile_SaveAs")
        self.actionFile_Close = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("://images/32x32/file-close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFile_Close.setIcon(icon6)
        self.actionFile_Close.setObjectName("actionFile_Close")
        self.actionFile_Print = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("://images/32x32/file-print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFile_Print.setIcon(icon7)
        self.actionFile_Print.setObjectName("actionFile_Print")
        self.actionFile_Properties = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("://images/32x32/file-properties.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFile_Properties.setIcon(icon8)
        self.actionFile_Properties.setObjectName("actionFile_Properties")
        self.actionFile_Quit = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("://images/32x32/file-quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFile_Quit.setIcon(icon9)
        self.actionFile_Quit.setObjectName("actionFile_Quit")
        self.actionEdit_Undo = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("://images/32x32/edit-undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Undo.setIcon(icon10)
        self.actionEdit_Undo.setObjectName("actionEdit_Undo")
        self.actionEdit_Redo = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("://images/32x32/edit-redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Redo.setIcon(icon11)
        self.actionEdit_Redo.setObjectName("actionEdit_Redo")
        self.actionEdit_Cut = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("://images/32x32/edit-cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Cut.setIcon(icon12)
        self.actionEdit_Cut.setObjectName("actionEdit_Cut")
        self.actionEdit_Copy = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("://images/32x32/edit-copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Copy.setIcon(icon13)
        self.actionEdit_Copy.setObjectName("actionEdit_Copy")
        self.actionEdit_Paste = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("://images/32x32/edit-paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Paste.setIcon(icon14)
        self.actionEdit_Paste.setObjectName("actionEdit_Paste")
        self.actionEdit_Delete = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("://images/32x32/file-openrecent-clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Delete.setIcon(icon15)
        self.actionEdit_Delete.setObjectName("actionEdit_Delete")
        self.actionEdit_Preferences = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("://images/32x32/edit-preferences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Preferences.setIcon(icon16)
        self.actionEdit_Preferences.setObjectName("actionEdit_Preferences")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("://images/32x32/edit-select-all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelect_All.setIcon(icon17)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionSelect_None = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("://images/32x32/select-none.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelect_None.setIcon(icon18)
        self.actionSelect_None.setObjectName("actionSelect_None")
        self.actionSelect_Invert = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("://images/32x32/select-invert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelect_Invert.setIcon(icon19)
        self.actionSelect_Invert.setObjectName("actionSelect_Invert")
        self.actionView_Toolbar_Default = QtWidgets.QAction(MainWindow)
        self.actionView_Toolbar_Default.setCheckable(True)
        self.actionView_Toolbar_Default.setObjectName("actionView_Toolbar_Default")
        self.actionView_Toolbar_Editing = QtWidgets.QAction(MainWindow)
        self.actionView_Toolbar_Editing.setCheckable(True)
        self.actionView_Toolbar_Editing.setObjectName("actionView_Toolbar_Editing")
        self.actionView_FullScreen = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("://images/32x32/view-fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_FullScreen.setIcon(icon20)
        self.actionView_FullScreen.setObjectName("actionView_FullScreen")
        self.actionView_StatusBar = QtWidgets.QAction(MainWindow)
        self.actionView_StatusBar.setCheckable(True)
        self.actionView_StatusBar.setWhatsThis("")
        self.actionView_StatusBar.setObjectName("actionView_StatusBar")
        self.actionView_Grid = QtWidgets.QAction(MainWindow)
        self.actionView_Grid.setCheckable(True)
        self.actionView_Grid.setObjectName("actionView_Grid")
        self.actionView_Zoom_ZoomIn = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("://images/32x32/view-zoom-zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_Zoom_ZoomIn.setIcon(icon21)
        self.actionView_Zoom_ZoomIn.setObjectName("actionView_Zoom_ZoomIn")
        self.actionView_Zoom_Reset = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/images/32x32/view-zoom-reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_Zoom_Reset.setIcon(icon22)
        self.actionView_Zoom_Reset.setObjectName("actionView_Zoom_Reset")
        self.actionView_Zoom_ZoomOut = QtWidgets.QAction(MainWindow)
        self.actionView_Zoom_ZoomOut.setIcon(icon21)
        self.actionView_Zoom_ZoomOut.setObjectName("actionView_Zoom_ZoomOut")
        self.actionView_Zoom_Fit = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("://images/32x32/view-zoom-fit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_Zoom_Fit.setIcon(icon23)
        self.actionView_Zoom_Fit.setWhatsThis("")
        self.actionView_Zoom_Fit.setObjectName("actionView_Zoom_Fit")
        self.actionView_Zoom_ZoomToSel = QtWidgets.QAction(MainWindow)
        self.actionView_Zoom_ZoomToSel.setWhatsThis("")
        self.actionView_Zoom_ZoomToSel.setObjectName("actionView_Zoom_ZoomToSel")
        self.actionView_Zoom_Other = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("://images/32x32/view-zoom-other.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_Zoom_Other.setIcon(icon24)
        self.actionView_Zoom_Other.setObjectName("actionView_Zoom_Other")
        self.actionHelp_About = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("://images/32x32/help-about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp_About.setIcon(icon25)
        self.actionHelp_About.setObjectName("actionHelp_About")
        self.menuRecent.addAction(self.actionFile_OpenRecent_1)
        self.menuRecent.addAction(self.actionFile_OpenRecent_2)
        self.menuRecent.addAction(self.actionFile_OpenRecent_3)
        self.menuRecent.addAction(self.actionFile_OpenRecent_4)
        self.menuRecent.addAction(self.actionFile_OpenRecent_5)
        self.menuRecent.addAction(self.actionFile_OpenRecent_6)
        self.menuRecent.addAction(self.actionFile_OpenRecent_7)
        self.menuRecent.addAction(self.actionFile_OpenRecent_8)
        self.menuRecent.addSeparator()
        self.menuRecent.addAction(self.actionFile_OpenRecent_Clear)
        self.menu_File.addAction(self.actionFile_New)
        self.menu_File.addAction(self.actionFile_Open)
        self.menu_File.addAction(self.menuRecent.menuAction())
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionFile_Save)
        self.menu_File.addAction(self.actionFile_SaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionFile_Close)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionFile_Print)
        self.menu_File.addAction(self.actionFile_Properties)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionFile_Quit)
        self.menu_Edit.addAction(self.actionEdit_Undo)
        self.menu_Edit.addAction(self.actionEdit_Redo)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionEdit_Cut)
        self.menu_Edit.addAction(self.actionEdit_Copy)
        self.menu_Edit.addAction(self.actionEdit_Paste)
        self.menu_Edit.addAction(self.actionEdit_Delete)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionEdit_Preferences)
        self.menu_Select.addAction(self.actionSelect_All)
        self.menu_Select.addAction(self.actionSelect_None)
        self.menu_Select.addAction(self.actionSelect_Invert)
        self.menuZoom.addAction(self.actionView_Zoom_Reset)
        self.menuZoom.addSeparator()
        self.menuZoom.addAction(self.actionView_Zoom_ZoomOut)
        self.menuZoom.addAction(self.actionView_Zoom_ZoomIn)
        self.menuZoom.addAction(self.actionView_Zoom_Fit)
        self.menuZoom.addAction(self.actionView_Zoom_ZoomToSel)
        self.menuZoom.addSeparator()
        self.menuZoom.addAction(self.actionView_Zoom_Other)
        self.menuToolbars.addAction(self.actionView_Toolbar_Default)
        self.menuToolbars.addAction(self.actionView_Toolbar_Editing)
        self.menu_View.addAction(self.menuToolbars.menuAction())
        self.menu_View.addAction(self.menuZoom.menuAction())
        self.menu_View.addSeparator()
        self.menu_View.addAction(self.actionView_FullScreen)
        self.menu_View.addSeparator()
        self.menu_View.addAction(self.actionView_StatusBar)
        self.menu_View.addAction(self.actionView_Grid)
        self.menu_Help.addAction(self.actionHelp_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Select.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.actionFile_New)
        self.toolBar.addAction(self.actionFile_Open)
        self.toolBar.addAction(self.actionFile_Save)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEdit_Undo)
        self.toolBar.addAction(self.actionEdit_Redo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEdit_Cut)
        self.toolBar.addAction(self.actionEdit_Copy)
        self.toolBar.addAction(self.actionEdit_Paste)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.graphicsView_wf_l_scale, self.graphicsView_wf_l_disp)
        MainWindow.setTabOrder(self.graphicsView_wf_l_disp, self.graphicsView_wf_r_scale)
        MainWindow.setTabOrder(self.graphicsView_wf_r_scale, self.graphicsView_wf_r_disp)
        MainWindow.setTabOrder(self.graphicsView_wf_r_disp, self.graphicsView_wf_time)
        MainWindow.setTabOrder(self.graphicsView_wf_time, self.graphicsView_sg_scale)
        MainWindow.setTabOrder(self.graphicsView_sg_scale, self.graphicsView_sg_disp)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pfft"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuRecent.setTitle(_translate("MainWindow", "Open Recent"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.menu_Select.setTitle(_translate("MainWindow", "&Select"))
        self.menu_View.setTitle(_translate("MainWindow", "&View"))
        self.menuZoom.setTitle(_translate("MainWindow", "Zoom"))
        self.menuToolbars.setTitle(_translate("MainWindow", "Toolbars"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionFile_New.setText(_translate("MainWindow", "New"))
        self.actionFile_New.setStatusTip(_translate("MainWindow", "Create a new, blank audio file"))
        self.actionFile_New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionFile_Open.setText(_translate("MainWindow", "Open..."))
        self.actionFile_Open.setStatusTip(_translate("MainWindow", "Open an existing audio file"))
        self.actionFile_Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionFile_OpenRecent_1.setText(_translate("MainWindow", "&1 (dynamic)"))
        self.actionFile_OpenRecent_2.setText(_translate("MainWindow", "&2 (dynamic)"))
        self.actionFile_OpenRecent_3.setText(_translate("MainWindow", "&3 (dynamic)"))
        self.actionFile_OpenRecent_4.setText(_translate("MainWindow", "&4 (dynamic)"))
        self.actionFile_OpenRecent_5.setText(_translate("MainWindow", "&5 (dynamic)"))
        self.actionFile_OpenRecent_6.setText(_translate("MainWindow", "&6 (dynamic)"))
        self.actionFile_OpenRecent_7.setText(_translate("MainWindow", "&7 (dynamic)"))
        self.actionFile_OpenRecent_8.setText(_translate("MainWindow", "&8 (dynamic)"))
        self.actionFile_OpenRecent_Clear.setText(_translate("MainWindow", "Clear History"))
        self.actionFile_OpenRecent_Clear.setStatusTip(_translate("MainWindow", "Clear the recently used file history"))
        self.actionFile_Save.setText(_translate("MainWindow", "Save"))
        self.actionFile_Save.setStatusTip(_translate("MainWindow", "Save the current audio file"))
        self.actionFile_Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionFile_SaveAs.setText(_translate("MainWindow", "Save As..."))
        self.actionFile_SaveAs.setStatusTip(_translate("MainWindow", "Save the current audio file with a new name"))
        self.actionFile_SaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionFile_Close.setText(_translate("MainWindow", "Close"))
        self.actionFile_Close.setStatusTip(_translate("MainWindow", "Close the current audio file"))
        self.actionFile_Close.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionFile_Print.setText(_translate("MainWindow", "Print..."))
        self.actionFile_Print.setStatusTip(_translate("MainWindow", "Print the current audio file"))
        self.actionFile_Print.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionFile_Properties.setText(_translate("MainWindow", "Properties"))
        self.actionFile_Properties.setStatusTip(_translate("MainWindow", "View current audio file metadata"))
        self.actionFile_Properties.setShortcut(_translate("MainWindow", "Alt+Return"))
        self.actionFile_Quit.setText(_translate("MainWindow", "Quit"))
        self.actionFile_Quit.setStatusTip(_translate("MainWindow", "Quit the application"))
        self.actionFile_Quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionEdit_Undo.setText(_translate("MainWindow", "Undo"))
        self.actionEdit_Undo.setStatusTip(_translate("MainWindow", "Undo the last action"))
        self.actionEdit_Undo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionEdit_Redo.setText(_translate("MainWindow", "Redo"))
        self.actionEdit_Redo.setStatusTip(_translate("MainWindow", "Redo the previously undone action"))
        self.actionEdit_Redo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionEdit_Cut.setText(_translate("MainWindow", "Cut"))
        self.actionEdit_Cut.setStatusTip(_translate("MainWindow", "Cut the selection and put it on the clipboard"))
        self.actionEdit_Cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionEdit_Copy.setText(_translate("MainWindow", "Copy"))
        self.actionEdit_Copy.setStatusTip(_translate("MainWindow", "Copy the selection and put it on the clipboard"))
        self.actionEdit_Copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionEdit_Paste.setText(_translate("MainWindow", "Paste"))
        self.actionEdit_Paste.setStatusTip(_translate("MainWindow", "Insert clipboard contents"))
        self.actionEdit_Paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionEdit_Delete.setText(_translate("MainWindow", "Delete"))
        self.actionEdit_Delete.setStatusTip(_translate("MainWindow", "Erase the selection"))
        self.actionEdit_Delete.setShortcut(_translate("MainWindow", "Del"))
        self.actionEdit_Preferences.setText(_translate("MainWindow", "Preferences"))
        self.actionEdit_Preferences.setStatusTip(_translate("MainWindow", "View and edit application preferences"))
        self.actionSelect_All.setText(_translate("MainWindow", "All"))
        self.actionSelect_All.setStatusTip(_translate("MainWindow", "Select the entire audio file"))
        self.actionSelect_All.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionSelect_None.setText(_translate("MainWindow", "None"))
        self.actionSelect_None.setStatusTip(_translate("MainWindow", "Remove any selection"))
        self.actionSelect_None.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        self.actionSelect_Invert.setText(_translate("MainWindow", "Invert"))
        self.actionSelect_Invert.setStatusTip(_translate("MainWindow", "Invert the selection"))
        self.actionSelect_Invert.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionView_Toolbar_Default.setText(_translate("MainWindow", "Default"))
        self.actionView_Toolbar_Default.setStatusTip(_translate("MainWindow", "Show or hide the default toolbar"))
        self.actionView_Toolbar_Default.setWhatsThis(_translate("MainWindow", "Toggle visibility of the default toolbar"))
        self.actionView_Toolbar_Editing.setText(_translate("MainWindow", "Editing"))
        self.actionView_Toolbar_Editing.setStatusTip(_translate("MainWindow", "Show or hide the editing toolbar"))
        self.actionView_Toolbar_Editing.setWhatsThis(_translate("MainWindow", "Toggle visibility of the editing toolbar"))
        self.actionView_FullScreen.setText(_translate("MainWindow", "Full Screen"))
        self.actionView_FullScreen.setStatusTip(_translate("MainWindow", "Toggle main window between normal and full screen mode"))
        self.actionView_FullScreen.setShortcut(_translate("MainWindow", "F11"))
        self.actionView_StatusBar.setText(_translate("MainWindow", "Status Bar"))
        self.actionView_StatusBar.setStatusTip(_translate("MainWindow", "Toggle visibility of the status bar"))
        self.actionView_Grid.setText(_translate("MainWindow", "Grid"))
        self.actionView_Grid.setStatusTip(_translate("MainWindow", "Toggle visibility of the grid"))
        self.actionView_Zoom_ZoomIn.setText(_translate("MainWindow", "Zoom In"))
        self.actionView_Zoom_ZoomIn.setStatusTip(_translate("MainWindow", "Increase the zoom level to see more detail"))
        self.actionView_Zoom_ZoomIn.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.actionView_Zoom_Reset.setText(_translate("MainWindow", "Reset"))
        self.actionView_Zoom_Reset.setStatusTip(_translate("MainWindow", "Reset zoom level to the default (1:1)"))
        self.actionView_Zoom_Reset.setWhatsThis(_translate("MainWindow", "Reset zoom"))
        self.actionView_Zoom_Reset.setShortcut(_translate("MainWindow", "Ctrl+0"))
        self.actionView_Zoom_ZoomOut.setText(_translate("MainWindow", "Zoom Out"))
        self.actionView_Zoom_ZoomOut.setStatusTip(_translate("MainWindow", "Reduce the zoom level to see more of the audio file"))
        self.actionView_Zoom_ZoomOut.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionView_Zoom_Fit.setText(_translate("MainWindow", "Fit"))
        self.actionView_Zoom_Fit.setStatusTip(_translate("MainWindow", "Zoom in or out to fit the entire audio file in the window"))
        self.actionView_Zoom_ZoomToSel.setText(_translate("MainWindow", "Zoom to Selection"))
        self.actionView_Zoom_ZoomToSel.setStatusTip(_translate("MainWindow", "Zoom in or out to fit the selection in the window"))
        self.actionView_Zoom_Other.setText(_translate("MainWindow", "Other..."))
        self.actionView_Zoom_Other.setStatusTip(_translate("MainWindow", "Specify a custom zoom amount"))
        self.actionHelp_About.setText(_translate("MainWindow", "About"))
        self.actionHelp_About.setStatusTip(_translate("MainWindow", "Display program information, version number and copyright"))

import resources_rc
