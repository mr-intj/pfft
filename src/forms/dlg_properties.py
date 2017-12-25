from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QDialog

from generated.ui_properties import Ui_DlgProperties


class DlgProperties(QDialog, Ui_DlgProperties):
    """The document properties dialog"""

    def __init__(self, parent, document):
        super(DlgProperties, self).__init__(parent)

        self.setupUi(self)

        self.document = document

        self.setWindowTitle('{} Properties'.format(self.document.title))

        # Sampling rate
        self.tableWidget.item(0, 1).setText(
            '{:} kHz ({:,} Hz)'.format(self.document.sampling_rate / 1000.0, self.document.sampling_rate))

        # Bit depth
        self.tableWidget.item(1, 1).setText('{}-bit'.format(self.document.bytes_per_sample * 8))

        # Number of channels
        self.tableWidget.item(2, 1).setText(str(self.document.channels))

        # Duration
        duration = QTime.fromMSecsSinceStartOfDay(1000 * self.document.frames / self.document.sampling_rate)
        self.tableWidget.item(3, 1).setText(
            '{:02}:{:02}:{:02}.{:03}'.format(duration.hour(), duration.minute(), duration.second(), duration.msec()))

    def reject(self):
        self.done(1)
