from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt5.QtGui import QIcon

from widgets.padded_spinbox import PaddedSpinBox


class PaddedSpinBoxPlugin(QPyDesignerCustomWidgetPlugin):
    def __init__(self, parent=None):
        super(PaddedSpinBoxPlugin, self).__init__(parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return PaddedSpinBox(parent)

    def name(self):
        return "PaddedSpinBox"

    def group(self):
        return "Input Widgets"

    def icon(self):
        return QIcon()

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    # Returns an XML description of a custom widget instance that describes default values for its properties.
    # Each custom widget created by this plugin will be configured using this description.
    def domXml(self):
        return '<widget class="PaddedSpinBox" name="paddedSpinBoxWidget" />\n'

    def includeFile(self):
        return "padded_spinbox"
