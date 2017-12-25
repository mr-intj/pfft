from PyQt5.QtWidgets import QDialog

from generated.ui_about import Ui_DlgAbout


class DlgAbout(QDialog, Ui_DlgAbout):
    """The application's About dialog"""

    def __init__(self, parent):
        super(DlgAbout, self).__init__(parent)

        self.setupUi(self)

    def reject(self):
        self.done(1)
