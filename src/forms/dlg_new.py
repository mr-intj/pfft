from PyQt5.QtCore import QSettings, QTime
from PyQt5.QtWidgets import QDialog

from generated.ui_new import Ui_DlgNew
from settings import Settings


class DlgNew(QDialog, Ui_DlgNew):
    """The new document dialog"""

    def __init__(self, parent):
        super(DlgNew, self).__init__(parent)

        self.setupUi(self)

        # Read configuration settings
        settings = QSettings()

        # TODO - need to figure out DDV/DDX
        self.sampling_rate = settings.value(Settings.DOC_SAMPLING_RATE,
                                            defaultValue=Settings.DOC_SAMPLING_RATE_DFLT)
        self.rate_comboBox.setCurrentText('{} Hz'.format(self.sampling_rate))

        # TODO - need to figure out DDV/DDX
        self.bytes_per_sample = settings.value(Settings.DOC_BYTES_PER_SAMPLE,
                                               defaultValue=Settings.DOC_BYTES_PER_SAMPLE_DFLT)
        self.bitd_16bit_radioButton.setChecked(self.bytes_per_sample == 2)
        self.bitd_24bit_radioButton.setChecked(self.bytes_per_sample == 3)
        self.bitd_32bitfloat_radioButton.setChecked(self.bytes_per_sample == 4)

        # TODO - need to figure out DDV/DDX
        self.channels = settings.value(Settings.DOC_CHANNELS,
                                       defaultValue=Settings.DOC_CHANNELS_DFLT)
        self.chan_1_radioButton.setChecked(self.channels == 1)
        self.chan_2_radioButton.setChecked(self.channels == 2)

        # TODO - need to figure out DDV/DDX
        self.frames = settings.value(Settings.DOC_FRAMES,
                                     defaultValue=Settings.DOC_FRAMES_DFLT)
        duration_msec = 1000 * self.frames / self.sampling_rate  # TODO - fix this
        duration = QTime.fromMSecsSinceStartOfDay(duration_msec)
        self.idur_hrs_spinBox.setValue(duration.hour())
        self.idur_mins_spinBox.setValue(duration.minute())
        self.idur_secs_spinBox.setValue(duration.second())
        self.idur_msec_spinBox.setValue(duration.msec())

        self.max_freq_fmt = self.rate_maxfreq_label.text()

        self.update_ui()

    def reject(self):
        self.done(1)

    def update_ui(self):
        # --- Sampling rate ---
        # self.rate_maxfreq_label.setText(self.max_freq_fmt.format(TODO))

        # --- Bit depth ---

        # --- Number of channels ---

        # --- Initial duration ---
        pass