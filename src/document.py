import os
import sys
import wave
from stat import *

from PyQt5.QtCore import QObject, pyqtSignal, QSettings, QTemporaryFile, QFile, QIODevice, QFileInfo
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from forms.dlg_new import DlgNew
from helpers import *
from settings import Settings


class Document(QObject):
    """Manages opening and saving the document, modified status, etc"""

    # region --- Class constants ---

    # File Open dialog extension filters for file types we can read
    OPEN_FILTERS = ['All files',
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

    # Default File Open dialog extension filter (list index)
    DFLT_OPEN_FILTER = -1

    # File Save As dialog extension filters for file types we can write
    SAVE_FILTERS = ['All files',
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

    # Default File Save As dialog extension filter (list index)
    DFLT_SAVE_FILTER = -1

    # Mask for rw-rw-rw- permissions
    PERMISSION_MASK = ~(QFile.ReadOwner | QFile.WriteOwner |
                        QFile.ReadGroup | QFile.WriteGroup |
                        QFile.ReadOther | QFile.WriteOther)

    # Application name suffix (used in window captions)
    UNTITLED_DOC_NAME = 'Untitled'

    # endregion

    # region --- Signals ---

    # The document contents have changed
    contents_changed = pyqtSignal()

    # A document property has changed; parameters are: bool old_value, bool new_value
    modified_changed = pyqtSignal(bool, bool)

    # A document property has changed; parameters are: str old_name, str new_name
    filename_changed = pyqtSignal(str, str)

    # endregion

    # region --- Initialization ---

    def __init__(self):
        super(Document, self).__init__()

        self.bytes_per_sample = Settings.DOC_BYTES_PER_SAMPLE_DFLT
        self.channels = Settings.DOC_CHANNELS_DFLT
        self.sampling_rate = Settings.DOC_SAMPLING_RATE_DFLT
        self.frames = Settings.DOC_FRAMES_DFLT

        self.contents = bytes(self.frames * self.bytes_per_sample * self.channels)

        self._filename = None
        self._is_modified = False

    # endregion

    # region --- Properties ---

    @property
    def filename(self):
        """Get or set the full path of the document.
        """
        return self._filename

    # This is a function vs property because it has associated logic but isn't public
    def _set_filename(self, new_value):
        if self._filename != new_value:
            old_value = self._filename
            self._filename = new_value
            if new_value:
                # Update our default open/save directory
                Settings.set_cwd(QFileInfo(new_value).dir().canonicalPath())
            self.filename_changed.emit(old_value, new_value)

    @property
    def is_modified(self):
        """Get or set the is_modified flag. Changing is_modified will emit a modified_changed signal."""
        return self._is_modified

    @is_modified.setter
    def is_modified(self, new_value):
        if self._is_modified != new_value:
            old_value = self._is_modified
            self._is_modified = new_value
            self.modified_changed.emit(old_value, new_value)

    @property
    def title(self):
        """Get or set the current filename. Setting the filename to a new value will update the title automatically,
        and emit a filename_changed signal.
        """
        return ellipsize(self.filename) if self.filename else Document.UNTITLED_DOC_NAME

    # endregion

    # region --- Commands ---

    def new(self, parent):
        # If current file has been modified, offer to save
        if self.close(parent) is False:
            return False

        # Allow the user to specify properties of the new document
        dlg = DlgNew(parent)
        if dlg.exec_() is False:
            return False

        self.bytes_per_sample = dlg.bytes_per_sample
        self.channels = dlg.channels
        self.sampling_rate = dlg.sampling_rate
        self.frames = dlg.frames

        self.contents = bytes(self.frames * self.bytes_per_sample * self.channels)

        self._set_filename(None)
        self.is_modified = False

        return True

    def open(self, parent, filename=None):
        """Opens the specified file and reads the contents into memory, setting filename and is_modified
        appropriately.
        :type parent: QWidget - The parent window for dialogs, alerts, etc.
        :type filename: str - Full path of file or None (the default)
        :rtype: bool - True = Successfully opened file, False = error or cancelled (user was notified)
        """
        # If no filename was passed in, prompt the user
        if filename is None:
            filename, _ = QFileDialog.getOpenFileName(parent,
                                                      make_caption('Open File'),
                                                      Settings.get_cwd(),
                                                      ";;".join(Document.OPEN_FILTERS),
                                                      Document.OPEN_FILTERS[Document.DFLT_OPEN_FILTER])
            if not filename:
                return False

        # If current file has been modified, offer to save
        if self.close(parent) is False:
            return False

        # Read in the WAV file
        try:
            with wave.open(filename, mode='rb') as wave_read:
                # Get the audio file properties
                self.bytes_per_sample = wave_read.getsampwidth()
                self.channels = wave_read.getnchannels()
                self.sampling_rate = wave_read.getframerate()
                self.frames = wave_read.getnframes()

                # Read the content into memory
                # TODO - Read entire file into memory (need to enable chunking eventually)
                self.contents = wave_read.readframes(self.frames)

        except wave.Error as e:
            # An error occurred, notify user and return False
            QMessageBox.critical(parent, make_caption('Warning'),
                                 "Unable to open file:\n\n\t<b>{}</b>\n\n\n{}".format(filename, e.args[0]))
            return False

        # except IOError as e:   # TODO - test this; can we detect file_not_found and read_permission_error?

        self._set_filename(filename)
        self.contents_changed.emit()

        return True

    def save(self, parent, filename=None):
        """Saves the current file and sets is_modified to False.
        If the file has never been saved (i.e., doesn't have a filename) or is not writable, this method calls save_as.
        :type parent: QWidget - The parent window for dialogs, alerts, etc.
        :type filename: str - Full path of file or None (the default)
        :rtype: bool - True = Successfully saved file, False = error (user was notified) or user cancelled
        """
        if filename is None:
            filename = self.filename

        # If the current file has never been saved...
        if filename is None:
            # ...call save_as instead
            self.on_file_saveas()

        wavfile = QFile(filename)
        # If the original file exists, but can't be opened for writing...
        if wavfile.exists() and not wavfile.open(QIODevice.ReadWrite):
            # ...then treat this as a Save-As command
            return self.save_as(parent)

        tmpfile = QTemporaryFile(filename)
        # If we can't open our temporary file for writing...
        if not QTemporaryFile.open(QIODevice.WriteOnly):
            # ...something's wrong (disk full?), so report it to the user and exit
            QMessageBox.critical(parent, make_caption('Warning'),
                                 "Unable to create temporary file:\n\n\t<b>{}</b>\n\n\n{}".format(tmpfile.fileName(),
                                                                                                  tmpfile.errorString()))
            return False

        # If the original file exists...
        if wavfile.exists():
            # ...set the temporary file permissions to match the original
            tmpfile.setPermissions(wavfile.permissions())  # Ignore errors
        elif sys.platform == 'win32':
            # ...otherwise (on Windows) use standard permissions
            tmpfile.setPermissions(QFile.WriteGroup | QFile.WriteOther)
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            # ...otherwise (on Linux) use the file mode creation mask for the current process
            tmpfile.setPermissions(self.umask_as_permission() & Document.PERMISSION_MASK)
        else:
            raise RuntimeError('Unsupported platform: ' + sys.platform)  # TODO - check this at startup, not here

        tmpfile.close()  # TODO - is this necessary?

        # Write out the WAV file
        try:
            with wave.open(tmpfile.fileName(), mode='wb') as wave_write:
                # Set the audio file properties
                wave_write.setnchannels(self.channels)
                wave_write.setsampwidth(self.bytes_per_sample)
                wave_write.setframerate(self.sampling_rate)
                wave_write.setnframes(self.frames)
                wave_write.setcomptype(None)

                # Write the contents of memory out to the file
                wave_write.writeframes(self.frames)

        except wave.Error as e:
            # An error occurred, notify user and return False
            QMessageBox.critical(parent, make_caption('Warning'),
                                 "Unable to write file:\n\n\t<b>{}</b>\n\n\n{}".format(tmpfile.fileName(), e.args[0]))
            return False

        # Data was written successfully to temp file, so inform QTemporaryFile not to remove it automatically; we're
        # going to rename it to the original file
        tmpfile.setAutoRemove(False)

        backup_filename = filename + '~'
        # Remove any previous backup
        QFile.remove(backup_filename)
        # Rename the original file to the backup name
        QFile.rename(filename, backup_filename)
        # Rename the temporary file to the original name
        if not tmpfile.rename(filename):
            # If anything goes wrong, rename the backup file back to the original name
            QFile.rename(backup_filename, filename)
            QMessageBox.critical(parent, make_caption('Warning'),
                                 "Unable to rename file:\n\n\tFrom: <b>{}</b>\n\tTo: <b>{}</b>\n\n\n{}".format(
                                     backup_filename, filename, tmpfile.errorString()))
            return False

        settings = QSettings()
        if not settings.value(Settings.CREATE_BACKUP_ON_SAVE, defaultValue=Settings.CREATE_BACKUP_ON_SAVE_DFLT):
            QFile.remove(backup_filename)

        self.is_modified = False
        self._set_filename(filename)

        return True

    def save_as(self, parent):
        """Prompts the user for a filename, saves the current file, and sets is_modified to False.
        :type parent: QWidget - The parent window for dialogs, alerts, etc.
        :rtype: bool - True = Successfully saved file, False = error (user was notified) or user cancelled
        """
        # Prompt for a save file name. If the file already exists, QFileDialog will prompt for overwrite permission.
        filename, _ = QFileDialog.getSaveFileName(parent,
                                                  make_caption('Save File As'),
                                                  Settings.get_cwd(),
                                                  ";;".join(Document.SAVE_FILTERS),
                                                  Document.SAVE_FILTERS[Document.DFLT_SAVE_FILTER])

        # If user canceled, just return False
        if not filename:
            return False

        return self.save(parent, filename)

    def close(self, parent):
        """Prompts the user to save if there are unsaved changes, then closes the file and sets is_modified to False.
        :type parent: QWidget - The parent window for dialogs, alerts, etc.
        :rtype: bool - True = Successfully closed file, False = error (user was notified) or user cancelled
        """
        # If current file has been modified, offer to save
        if self.is_modified:
            response = QMessageBox.warning(parent, make_caption('Warning'),
                                           'Save changes to {} before closing?'.format(self.title),
                                           QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                           QMessageBox.Save)
            # If user cancels, return False
            if response == QMessageBox.Cancel:
                return False
            # IF use attempts to save, and it either fails or the user cancels, return False
            elif response == QMessageBox.Save and self.save(self) is False:
                return False

        self.bytes_per_sample = Settings.DOC_BYTES_PER_SAMPLE_DFLT
        self.channels = Settings.DOC_CHANNELS_DFLT
        self.sampling_rate = Settings.DOC_SAMPLING_RATE_DFLT
        self.frames = Settings.DOC_FRAMES_DFLT

        self.contents = bytes(self.frames * self.bytes_per_sample * self.channels)

        self._set_filename(None)
        self.is_modified = False

        return True

    def undo(self):
        # Search for QUndoStack
        # and https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/qtjambi-undoframework.html
        pass

    def redo(self):
        pass

    # endregion

    # region --- Helpers ---

    @staticmethod
    def umask_as_permission():
        # Get the file mode creation mask for the current process
        umask = os.umask(0)

        # Restore the original mask (note that this isn't thread-safe)
        os.umask(umask)

        # Convert it into a combination of Qt Permission flags
        return (0 if not S_IRUSR(umask) else QFile.ReadOwner) | \
               (0 if not S_IWUSR(umask) else QFile.WriteOwner) | \
               (0 if not S_IXUSR(umask) else QFile.ExeOwner) | \
               (0 if not S_IRGRP(umask) else QFile.ReadGroup) | \
               (0 if not S_IWGRP(umask) else QFile.WriteGroup) | \
               (0 if not S_IXGRP(umask) else QFile.ExeGroup) | \
               (0 if not S_IROTH(umask) else QFile.ReadOther) | \
               (0 if not S_IWOTH(umask) else QFile.WriteOther) | \
               (0 if not S_IXOTH(umask) else QFile.ExeOther)

        # endregion
