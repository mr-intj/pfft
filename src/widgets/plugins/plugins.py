import os
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QProcessEnvironment, QDir, QFileInfo
from PyQt5.QtWidgets import QApplication, QMessageBox
import shutil as sh

def env_path_append(path, elem):
    if not path:
        return elem
    elif not elem.lower() in path.lower().split(os.pathsep):
        return '{}{}{}'.format(path, os.pathsep, elem)
    return path

DEBUG_PLUGINS = 'QT_DEBUG_PLUGINS'
PYQTDESIGNERPATH = 'PYQTDESIGNERPATH'
PYTHONPATH = 'PYTHONPATH'

app = QApplication(sys.argv)

if QMessageBox.Cancel == QMessageBox.information(
        None, "Qt Designer Plugins for Pfft",
        "<p>Click <b>OK</b> to start Qt Designer with the Pfft custom widget plugin.</p>",
        QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok):
    sys.exit(0)

# Use the directory of this module to set up paths to the plugin and widget directories
plugin_dir = os.path.dirname(__file__)
widget_dir = os.path.abspath(os.path.join(plugin_dir, '..'))

# Get a copy of the environment from our process
env = QProcessEnvironment.systemEnvironment()

# Add our custom widget directory to the Python path
env.insert(PYTHONPATH, env_path_append(env.value(PYTHONPATH), widget_dir))

# Add our plugin directory to the environment variable used by Qt Designer for custom widget plugins
env.insert(PYQTDESIGNERPATH, env_path_append(env.value(PYQTDESIGNERPATH), plugin_dir))

# Optionally, turn on plugin debugging to show Designer's debug output in the console
env.insert(DEBUG_PLUGINS, '1')

# Launch Qt Designer; the custom widgets should appear in Designer's widget box in the 'Pfft' group
process = QtCore.QProcess()
process.setProcessEnvironment(env)

qt_bin_dir = sh.which('designer')
if qt_bin_dir:
    qt_bin_dir = os.path.dirname(qt_bin_dir)
else:
    qt_bin_dir = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.BinariesPath)

if sys.platform.startswith('linux'):
    qt_bin_dir = os.path.join(qt_bin_dir, 'designer')
elif sys.platform.startswith('darwin'):
    qt_bin_dir = os.path.join(qt_bin_dir, 'Designer.app/Contents/MacOS/Designer')
elif sys.platform == 'win32':
    # TODO - check this - it should be something like 'C:\Qt\5.8\mingw53_32\bin\designer.exe'
    qt_bin_dir = os.path.join(qt_bin_dir, 'designer.exe')
else:
    raise RuntimeError('Platform not supported/recognized: ' + sys.platform)

# process.setWorkingDirectory(plugin_dir)
process.start(qt_bin_dir)
print('ProcessState is: {}'.format(process.exitCode()))
process.waitForFinished(-1)

print('Exit Code is: {}'.format(process.exitCode()))
print('Exit Status is: {}'.format(process.exitStatus()))
print('Process Error is: {}'.format(process.error()))
stdout = process.readAllStandardOutput()
stderr = process.readAllStandardError()
print('stdout is: {}'.format(stdout))
print('stderr is: {}'.format(stderr))

sys.exit(process.exitCode())
