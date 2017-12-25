from PyQt5.QtWidgets import *


class PaddedSpinBox(QSpinBox):
    """Subclassed to display zero-padded values"""

    def __init__(self, parent=None):
        super(PaddedSpinBox, self).__init__(parent)

    def valueFromText(self, text):
        return int(text)

    def textFromValue(self, value):
        # Generate a format string like '{:0n}' where 'n' is the number of digits in the max field value;
        # e.g. if maximum is 999 then 'n' is 3, so the output will be '001', etc.
        fmt = '{{:0{}}}'.format(len(str(self.maximum())))
        return fmt.format(value)
