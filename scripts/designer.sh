#!/bin/bash

# This script starts Qt Designer with our custom widget plugin(s)

# Ensure Python can find our custom widgets
export PYQTDESIGNERPATH=../src/widgets/plugins:$PYQTDESIGNERPATH

# Ensure Qt Designer can find our custom widget plugins
export PYTHONPATH=..:../src:../src/generated:../src/widgets:../src/widgets/plugins:$PYTHONPATH

# Optionally, turn on plugin debugging to show Designer's debug output in the console
export QT_DEBUG_PLUGINS=1

# Launch Qt Designer; the custom widgets should appear in Designer's widget box in the 'Pfft' group
designer &