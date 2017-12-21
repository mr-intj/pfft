import os
import pathlib
import wave
from pathlib import Path

from PyQt5.QtCore import QSettings, QFile
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox

from dlg_about import DlgAbout
from generated.ui_mainwindow import Ui_MainWindow
from mru_list import MruList


class MainWindow(QMainWindow, Ui_MainWindow):
    # region --- Initialization ---

    def __init__(self):
        super(MainWindow, self).__init__()

        self.wave_read = None
        self.cur_filename = None
        self.is_modified = False

        # Read configuration settings
        settings = QSettings()

        self.cwd = settings.value('cwd', defaultValue=str(Path.home()))
        if not os.path.isdir(self.cwd):
            self.cwd = str(Path.home())

        self.mru_list = MruList(settings.value('mru_list', defaultValue=[]))

        self.setupUi(self)
        self.setup_signals()
        self.update_ui()

    def setup_signals(self):
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

    # region --- Menu/Toolbar item handlers ---

    def on_file_new(self):
        pass

    def on_file_open(self):
        filter_list = ['All files',
                       # 'All supported raster formats (*.bmp *.gif *.jpg *.jpeg *.png)',
                       # 'BMP - Microsoft Windows Device Independent Bitmap (*.bmp)',
                       # 'GIF - Graphics Interchange Format (*.gif)',
                       # 'JPEG - Joint Photographic Experts Group JFIF (*.jpg *.jpeg)',
                       # 'PNG - Portable Network Graphics (*.png)',
                       # -----------------
                       # 'All supported audio formats (*.flac *.mp3 *.ogg *.wav)',
                       # 'AIFF - Audio Interchange File Format (*.aif, *.aiff, *.aifc)',
                       # 'AU/SND - Sun Microsystems Audio File Format (*.au, *.snd)',
                       # 'FLAC - Free Lossless Audio Codec (*.flac)',
                       # 'MP3 - MPEG Layer 3 (*.mp3)',
                       # 'OGG - Ogg Vorbis (*.ogg)',
                       'Wave Audio File Format (*.wav)']
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  'Open File - Pfft',
                                                  self.cwd,
                                                  ";;".join(filter_list),
                                                  filter_list[-1])

        if filename:
            self.load_file(filename)

    def on_file_openrecent(self):
        action = self.sender()
        if action:
            self.load_file(action.data())

    def on_file_openrecent_clear(self):
        self.mru_list.clear()
        QSettings().setValue('mru_list', self.mru_list.items)
        self.update_ui()

    def on_file_save(self):
        if not self.cur_filename:
            self.on_file_saveas()

        self.update_ui()

    def on_file_saveas(self):
        filter_list = ['All files',
                       # 'All supported raster formats (*.bmp *.gif *.jpg *.jpeg *.png)',
                       # 'BMP - Microsoft Windows Device Independent Bitmap (*.bmp)',
                       # 'GIF - Graphics Interchange Format (*.gif)',
                       # 'JPEG - Joint Photographic Experts Group JFIF (*.jpg *.jpeg)',
                       # 'PNG - Portable Network Graphics (*.png)',
                       # -----------------
                       # 'All supported audio formats (*.flac *.mp3 *.ogg *.wav)',
                       # 'AIFF - Audio Interchange File Format (*.aif, *.aiff, *.aifc)',
                       # 'AU/SND - Sun Microsystems Audio File Format (*.au, *.snd)',
                       # 'FLAC - Free Lossless Audio Codec (*.flac)',
                       # 'MP3 - MPEG Layer 3 (*.mp3)',
                       # 'OGG - Ogg Vorbis (*.ogg)',
                       'Wave Audio File Format (*.wav)']
        filename, _ = QFileDialog.getSaveFileName(self,
                                                  'Save File As - Pfft',
                                                  self.cwd,
                                                  ";;".join(filter_list),
                                                  filter_list[-1])
        # TODO - write the file
        #if successful:
        self.cur_filename = filename
        self.is_modified = False

        self.mru_list.push(self.cur_filename)
        QSettings().setValue('mru_list', self.mru_list.items)

        self.update_ui()

    def on_file_close(self):
        # If current file has been modified, offer to save
        if self.is_modified and QMessageBox.Yes == QMessageBox.warning(
                self, "Warning - Pfft",
                "Save changes to {} before closing?".format(self.cur_filename if self.cur_filename else "Untitled"),
                QMessageBox_StandardButtons=QMessageBox.No | QMessageBox.Yes,
                QMessageBox_StandardButton=QMessageBox.Yes):
            self.on_file_save()

        if self.wave_read:
            self.wave_read.close()
            self.wave_read = None
            self.cur_filename = None
            self.is_modified = False
            self.update_ui()
        pass

    def on_file_print(self):
        pass

    def on_file_properties(self):
        pass

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

    def load_file(self, filename):
        # Close the current file, if any

        # If file isn't readable...
        if not os.access(filename, os.R_OK):
            # ...see if it's in the MRU list
            index = self.mru_list.index_of(filename)
            # Message the user
            if index == -1:
                QMessageBox.warning(self, "Warning - Pfft", "Cannot read file {}".format(filename))
            else:
                # If in the MRU list, also ask if they'd like it to be removed from the MRU list
                if QMessageBox.Yes == QMessageBox.warning(
                        self, "Warning - Pfft",
                        "Can't open file {}\n\nRemove it from the Open Recent menu?".format(
                            filename),
                        QMessageBox_StandardButtons=QMessageBox.No | QMessageBox.Yes,
                        QMessageBox_StandardButton=QMessageBox.Yes):
                    self.mru_list.pop(filename)
                    QSettings().setValue('mru_list', self.mru_list.items)
                    self.update_ui()

            return

        self.mru_list.push(filename)
        QSettings().setValue('mru_list', self.mru_list.items)

        self.statusbar.showMessage('Opening {}'.format(filename))

        try:
            self.wave_read = wave.open(filename, mode='rb')
        except wave.Error as e:
            QMessageBox.warning(self, "Warning - Pfft", "Unable to open:\n\n{}".format(e.args[0]))

        self.statusbar.clearMessage()
        self.update_ui()

    def load_mru_file(self, index):
        self.load_file(self.mru_list.get(index))

    @staticmethod
    def ellipsize(path):
        parts = list(pathlib.PurePath(path).parts)
        if len(parts) >= 4:
            parts[2:-1] = ['...']
        return str(pathlib.PurePath(*parts))

    def update_ui(self):
        enabled = True

        # --- Main Window ---

        title = ' - Pfft'
        if self.cur_filename:
            title = self.cur_filename + title
        else:
            title = 'Untitled' + title

        if self.is_modified:
            title = '*' + title

        MainWindow.setWindowTitle(title)

        # --- File menu ---

        # File|New: always enabled
        self.actionFile_New.setEnabled(True)

        # File|Open: always enabled
        self.actionFile_Open.setEnabled(True)

        # Since it's followed by a separator, the first MRU item is disabled (w/text "None") vs. invisible
        if self.mru_list.count() == 0:
            self.actionFile_OpenRecent_1.setEnabled(False)
            self.actionFile_OpenRecent_1.setText('(none)')
            self.actionFile_OpenRecent_1.setData('')
            self.actionFile_OpenRecent_1.setStatusTip('')
        else:
            self.actionFile_OpenRecent_1.setEnabled(True)
            self.actionFile_OpenRecent_1.setText('&1 ' + MainWindow.ellipsize(self.mru_list.get(0)))
            self.actionFile_OpenRecent_1.setData(self.mru_list.get(0))
            self.actionFile_OpenRecent_1.setStatusTip(self.mru_list.get(0))

        # The remainder of the MRU items are invisible if empty
        self.actionFile_OpenRecent_2.setVisible(self.mru_list.count() > 1)
        self.actionFile_OpenRecent_2.setText('&2 ' + MainWindow.ellipsize(self.mru_list.get(1)))
        self.actionFile_OpenRecent_2.setData(self.mru_list.get(1))
        self.actionFile_OpenRecent_2.setStatusTip(self.mru_list.get(1))

        self.actionFile_OpenRecent_3.setVisible(self.mru_list.count() > 2)
        self.actionFile_OpenRecent_3.setText('&3 ' + MainWindow.ellipsize(self.mru_list.get(2)))
        self.actionFile_OpenRecent_3.setData(self.mru_list.get(2))
        self.actionFile_OpenRecent_3.setStatusTip(self.mru_list.get(2))

        self.actionFile_OpenRecent_4.setVisible(self.mru_list.count() > 3)
        self.actionFile_OpenRecent_4.setText('&4 ' + MainWindow.ellipsize(self.mru_list.get(3)))
        self.actionFile_OpenRecent_4.setData(self.mru_list.get(3))
        self.actionFile_OpenRecent_4.setStatusTip(self.mru_list.get(3))

        self.actionFile_OpenRecent_5.setVisible(self.mru_list.count() > 4)
        self.actionFile_OpenRecent_5.setText('&5 ' + MainWindow.ellipsize(self.mru_list.get(4)))
        self.actionFile_OpenRecent_5.setData(self.mru_list.get(4))
        self.actionFile_OpenRecent_5.setStatusTip(self.mru_list.get(4))

        self.actionFile_OpenRecent_6.setVisible(self.mru_list.count() > 5)
        self.actionFile_OpenRecent_6.setText('&6 ' + MainWindow.ellipsize(self.mru_list.get(5)))
        self.actionFile_OpenRecent_6.setData(self.mru_list.get(5))
        self.actionFile_OpenRecent_6.setStatusTip(self.mru_list.get(5))

        self.actionFile_OpenRecent_7.setVisible(self.mru_list.count() > 6)
        self.actionFile_OpenRecent_7.setText('&7 ' + MainWindow.ellipsize(self.mru_list.get(6)))
        self.actionFile_OpenRecent_7.setData(self.mru_list.get(6))
        self.actionFile_OpenRecent_7.setStatusTip(self.mru_list.get(6))

        self.actionFile_OpenRecent_8.setVisible(self.mru_list.count() > 7)
        self.actionFile_OpenRecent_8.setText('&8 ' + MainWindow.ellipsize(self.mru_list.get(7)))
        self.actionFile_OpenRecent_8.setData(self.mru_list.get(7))
        self.actionFile_OpenRecent_8.setStatusTip(self.mru_list.get(7))

        self.actionFile_OpenRecent_Clear.setEnabled(self.mru_list.count() > 0)

        # File|Save: always enabled
        self.actionFile_Save.setEnabled(True)

        self.actionFile_SaveAs.setEnabled(enabled)
        self.actionFile_Close.setEnabled(enabled)
        self.actionFile_PrintPreview.setEnabled(enabled)
        self.actionFile_Print.setEnabled(enabled)
        self.actionFile_Properties.setEnabled(enabled)
        self.actionFile_Quit.setEnabled(enabled)

        # --- Edit menu ---

        self.actionEdit_Undo.setEnabled(enabled)
        self.actionEdit_Redo.setEnabled(enabled)
        self.actionEdit_Copy.setEnabled(enabled)
        self.actionEdit_Cut.setEnabled(enabled)
        self.actionEdit_Paste.setEnabled(enabled)
        self.actionEdit_Delete.setEnabled(enabled)
        self.actionEdit_Preferences.setEnabled(enabled)

        # --- Select menu ---

        self.actionSelect_All.setEnabled(enabled)
        self.actionSelect_None.setEnabled(enabled)
        self.actionSelect_Invert.setEnabled(enabled)

        # --- View menu ---

        self.actionView_Toolbar_Default.setEnabled(enabled)
        self.actionView_Toolbar_Editing.setEnabled(enabled)
        self.actionView_Zoom_Fit.setEnabled(enabled)
        self.actionView_Zoom_Other.setEnabled(enabled)
        self.actionView_Zoom_Reset.setEnabled(enabled)
        self.actionView_Zoom_ZoomIn.setEnabled(enabled)
        self.actionView_Zoom_ZoomOut.setEnabled(enabled)
        self.actionView_Zoom_ZoomToSel.setEnabled(enabled)
        self.actionView_FullScreen.setEnabled(enabled)
        self.actionView_StatusBar.setEnabled(enabled)
        self.actionView_Grid.setEnabled(enabled)

        # --- Help menu ---

        self.actionHelp_About.setEnabled(enabled)

        # endregion
