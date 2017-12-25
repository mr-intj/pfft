from pathlib import Path

from PyQt5.QtCore import QDir, QSettings


class Settings:
    # Current Working Directory (default for File>Open, File>SaveAs, etc)
    # (default value for this is the current user's home directory)
    CWD = 'cwd'
    CWD_DFLT = str(Path.home())

    # When True, save/save-as will create a backup in the same directory
    CREATE_BACKUP_ON_SAVE = 'CreateBackupOnSave'
    CREATE_BACKUP_ON_SAVE_DFLT = False

    # Sampling rate (in Hertz)
    DOC_SAMPLING_RATE = 'SamplingRate'
    DOC_SAMPLING_RATE_DFLT = 44100

    # Sample width (in bytes), 2 = 16-bit, 3 = 24-bit, 4 = 32-bit float
    DOC_BYTES_PER_SAMPLE = 'BytesPerSample'
    DOC_BYTES_PER_SAMPLE_DFLT = 3

    # Number of audio channels (1 = mono, 2 = stereo)
    DOC_CHANNELS = 'Channels'
    DOC_CHANNELS_DFLT = 2

    # Number of frames
    DOC_FRAMES = 'Frames'
    DOC_FRAMES_DFLT = 5 * DOC_SAMPLING_RATE_DFLT

    # Most Recently Used file list (File > Open Recent)
    MRU_LIST = 'mru_list'
    MRU_LIST_DFLT = []

    @staticmethod
    def set_cwd(new_value):
        """Set the current working directory (default for file open and save-as)"""
        cwd = QDir(new_value)
        if cwd.exists():
            settings = QSettings()
            settings.setValue(Settings.CWD, cwd.canonicalPath())  # resolve symlinks and relative paths

    @staticmethod
    def get_cwd():
        """Get the current working directory (default for file open and save-as)"""
        settings = QSettings()
        cwd = QDir(settings.value(Settings.CWD, defaultValue=Settings.CWD_DFLT))

        if not cwd.exists():
            cwd = QDir(str(Path.home()))

        return cwd.canonicalPath()  # resolve symlinks and relative paths
