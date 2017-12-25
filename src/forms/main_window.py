import os
from pathlib import Path

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import (QMainWindow, QMessageBox)

from document import Document
from forms.dlg_about import DlgAbout
from forms.dlg_properties import DlgProperties
from generated.ui_mainwindow import Ui_MainWindow
from helpers import *
from mru_list import MruList
from settings import Settings


class MainWindow(QMainWindow, Ui_MainWindow):
    """The main application window"""

    # region --- Initialization ---

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        # Document and signals
        self.document = Document()
        self.document.contents_changed.connect(self.on_contents_changed)
        self.document.filename_changed.connect(self.on_filename_changed)
        self.document.modified_changed.connect(self.on_modified_changed)

        # Read configuration settings
        settings = QSettings()

        self.cwd = settings.value(Settings.CWD, defaultValue=Settings.CWD_DFLT)
        if not os.path.isdir(self.cwd):
            self.cwd = str(Path.home())

        # MRU (File > Open Recent) list and signals
        self.mru_list = MruList(settings.value(Settings.MRU_LIST, defaultValue=Settings.MRU_LIST_DFLT))
        self.mru_list.changed.connect(self.on_mru_changed)

        self._mru_actions = [self.actionFile_OpenRecent_1, self.actionFile_OpenRecent_2,
                             self.actionFile_OpenRecent_3, self.actionFile_OpenRecent_4,
                             self.actionFile_OpenRecent_5, self.actionFile_OpenRecent_6,
                             self.actionFile_OpenRecent_7, self.actionFile_OpenRecent_8]

        self.setup_ui_signals()
        self.update_ui()

    def setup_ui_signals(self):
        # File menu
        self.actionFile_New.triggered.connect(self.on_file_new)
        self.actionFile_Open.triggered.connect(self.on_file_open)
        self.actionFile_OpenRecent_1.triggered.connect(self.on_file_openrecent)
        self.actionFile_OpenRecent_2.triggered.connect(self.on_file_openrecent)
        self.actionFile_OpenRecent_3.triggered.connect(self.on_file_openrecent)
        self.actionFile_OpenRecent_4.triggered.connect(self.on_file_openrecent)
        self.actionFile_OpenRecent_5.triggered.connect(self.on_file_openrecent)
        self.actionFile_OpenRecent_6.triggered.connect(self.on_file_openrecent)
        self.actionFile_OpenRecent_7.triggered.connect(self.on_file_openrecent)
        self.actionFile_OpenRecent_8.triggered.connect(self.on_file_openrecent)
        self.actionFile_OpenRecent_Clear.triggered.connect(self.on_file_openrecent_clear)
        self.actionFile_Save.triggered.connect(self.on_file_save)
        self.actionFile_SaveAs.triggered.connect(self.on_file_saveas)
        self.actionFile_Close.triggered.connect(self.on_file_close)
        self.actionFile_Print.triggered.connect(self.on_file_print)
        self.actionFile_Properties.triggered.connect(self.on_file_properties)
        self.actionFile_Quit.triggered.connect(self.on_file_quit)

        # Edit menu
        self.actionEdit_Undo.triggered.connect(self.on_edit_undo)
        self.actionEdit_Redo.triggered.connect(self.on_edit_redo)
        self.actionEdit_Copy.triggered.connect(self.on_edit_copy)
        self.actionEdit_Cut.triggered.connect(self.on_edit_cut)
        self.actionEdit_Paste.triggered.connect(self.on_edit_paste)
        self.actionEdit_Delete.triggered.connect(self.on_edit_delete)
        self.actionEdit_Preferences.triggered.connect(self.on_edit_preferences)

        # Select menu
        self.actionSelect_All.triggered.connect(self.on_select_all)
        self.actionSelect_None.triggered.connect(self.on_select_none)
        self.actionSelect_Invert.triggered.connect(self.on_select_invert)

        # View menu
        self.actionView_Toolbar_Default.triggered.connect(self.on_view_toolbar_default)
        self.actionView_Toolbar_Editing.triggered.connect(self.on_view_toolbar_editing)
        self.actionView_Zoom_Fit.triggered.connect(self.on_view_zoom_fit)
        self.actionView_Zoom_Other.triggered.connect(self.on_view_zoom_other)
        self.actionView_Zoom_Reset.triggered.connect(self.on_view_zoom_reset)
        self.actionView_Zoom_ZoomIn.triggered.connect(self.on_view_zoom_zoomin)
        self.actionView_Zoom_ZoomOut.triggered.connect(self.on_view_zoom_zoomout)
        self.actionView_Zoom_ZoomToSel.triggered.connect(self.on_view_zoom_zoomtosel)
        self.actionView_FullScreen.triggered.connect(self.on_view_fullscreen)
        self.actionView_StatusBar.triggered.connect(self.on_view_statusbar)
        self.actionView_Grid.triggered.connect(self.on_view_grid)

        # Help menu
        self.actionHelp_About.triggered.connect(self.on_help_about)

    # endregion

    # region --- Slots (menu, toolbar, mru, etc) ---

    def on_contents_changed(self):
        """Called when document contents have changed"""
        pass

    def on_filename_changed(self):
        """Called when document filename has changed"""
        # Add the new filename (or move it) to the front of the list
        self.mru_list.push(self.document.filename)

    def on_modified_changed(self):
        """Called when document is_modified flag changes"""
        self.update_ui()

    def on_mru_changed(self):
        """Called when MRU list contents have changed"""
        # Persist the changed MRU list to user settings
        QSettings().setValue('mru_list', self.mru_list.items)

    def on_file_new(self):
        if self.document.new(self) is True:
            self.update_ui()

    def on_file_open(self):
        if self.document.open(self) is True:
            self.mru_list.push(self.document.filename)
            self.update_ui()

    def on_file_openrecent(self):
        action = self.sender()
        if action:
            filename = action.data()

            # If a file listed in the MRU list no longer exists...
            if os.path.isfile(filename) is False:
                # ...inform user and ask to remove filename from the MRU list
                if QMessageBox.Yes == QMessageBox.warning(
                        self, make_caption('Warning'),
                        "<p>File not found <tt>{}</tt></p><p>Remove it from the Open Recent menu?</p>".format(filename),
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes):
                    self.mru_list.pop(filename)
                    return False

            if self.document.open(self, filename):
                self.mru_list.push(self.document.filename)
                self.update_ui()

    def on_file_openrecent_clear(self):
        self.mru_list.clear()
        self.update_ui()

    def on_file_save(self):
        if self.document.save(self) is True:
            self.mru_list.push(self.document.filename)
            self.update_ui()

    def on_file_saveas(self):
        if self.document.save_as(self) is True:
            self.mru_list.push(self.document.filename)
            self.update_ui()

    def on_file_close(self):
        if self.document.close(self) is True:
            self.update_ui()

    def on_file_print(self):
        pass

    def on_file_properties(self):
        dlg = DlgProperties(self, self.document)
        dlg.exec_()

    def on_file_quit(self):
        pass

    def on_edit_undo(self):
        pass

    def on_edit_redo(self):
        pass

    def on_edit_copy(self):
        pass

    def on_edit_cut(self):
        pass

    def on_edit_paste(self):
        pass

    def on_edit_delete(self):
        pass

    def on_edit_preferences(self):
        pass

    def on_select_all(self):
        pass

    def on_select_none(self):
        pass

    def on_select_invert(self):
        pass

    def on_view_toolbar_default(self):
        pass

    def on_view_toolbar_editing(self):
        pass

    def on_view_zoom_fit(self):
        pass

    def on_view_zoom_other(self):
        pass

    def on_view_zoom_reset(self):
        pass

    def on_view_zoom_zoomin(self):
        pass

    def on_view_zoom_zoomout(self):
        pass

    def on_view_zoom_zoomtosel(self):
        pass

    def on_view_fullscreen(self):
        pass

    def on_view_statusbar(self):
        pass

    def on_view_grid(self):
        pass

    def on_help_about(self):
        dlg = DlgAbout(self)
        dlg.exec_()

    # endregion

    # region --- Helper methods ---

    def update_ui(self):
        not_implemented_yet = False

        # --- Main Window ---

        self.setWindowTitle(make_caption('{}{}'.format('*' if self.document.is_modified else '', self.document.title)))

        # --- File menu ---

        # File|New: always enabled
        # self.actionFile_New.setEnabled(True)

        # File|Open: always enabled
        # self.actionFile_Open.setEnabled(True)

        # File|Open Recent
        for idx, action in enumerate(self._mru_actions):
            if idx < self.mru_list.count():
                full_path = self.mru_list.get(idx)
                menu_text = "&{} {}".format(idx + 1, ellipsize(full_path))
            else:
                full_path = ''
                menu_text = '(none)'

            action.setEnabled(idx < self.mru_list.count())
            action.setVisible(idx < max(1, self.mru_list.count()))
            action.setText(menu_text)
            action.setData(full_path)
            action.setStatusTip(full_path)

        self.actionFile_OpenRecent_Clear.setEnabled(self.mru_list.count() > 0)

        # File|Save: always enabled
        # self.actionFile_Save.setEnabled(True)

        # File|SaveAs: always enabled
        # self.actionFile_SaveAs.setEnabled(True)

        # File|Close: always enabled
        # self.actionFile_Close.setEnabled(True)

        # File|Print: always enabled
        # self.actionFile_Print.setEnabled(True)

        # File|Properties: always enabled
        # self.actionFile_Properties.setEnabled(True)

        # File|Quit: always enabled
        # self.actionFile_Quit.setEnabled(True)

        # --- Edit menu ---

        self.actionEdit_Undo.setEnabled(not_implemented_yet)
        self.actionEdit_Redo.setEnabled(not_implemented_yet)
        self.actionEdit_Copy.setEnabled(not_implemented_yet)
        self.actionEdit_Cut.setEnabled(not_implemented_yet)
        self.actionEdit_Paste.setEnabled(not_implemented_yet)
        self.actionEdit_Delete.setEnabled(not_implemented_yet)
        self.actionEdit_Preferences.setEnabled(not_implemented_yet)

        # --- Select menu ---

        self.actionSelect_All.setEnabled(not_implemented_yet)
        self.actionSelect_None.setEnabled(not_implemented_yet)
        self.actionSelect_Invert.setEnabled(not_implemented_yet)

        # --- View menu ---

        self.actionView_Toolbar_Default.setEnabled(not_implemented_yet)
        self.actionView_Toolbar_Editing.setEnabled(not_implemented_yet)
        self.actionView_Zoom_Fit.setEnabled(not_implemented_yet)
        self.actionView_Zoom_Other.setEnabled(not_implemented_yet)
        self.actionView_Zoom_Reset.setEnabled(not_implemented_yet)
        self.actionView_Zoom_ZoomIn.setEnabled(not_implemented_yet)
        self.actionView_Zoom_ZoomOut.setEnabled(not_implemented_yet)
        self.actionView_Zoom_ZoomToSel.setEnabled(not_implemented_yet)
        self.actionView_FullScreen.setEnabled(not_implemented_yet)
        self.actionView_StatusBar.setEnabled(not_implemented_yet)
        self.actionView_Grid.setEnabled(not_implemented_yet)

        # --- Help menu ---

        # Help|About: always enabled
        # self.actionHelp_About.setEnabled(True)

        # endregion
