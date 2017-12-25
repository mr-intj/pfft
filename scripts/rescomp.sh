#!/bin/bash

# This script compiles the Qt resources (.qrc) and forms (.ui) to generate python files

pyrcc5 ../rsrc/resources.qrc            -o ../src/generated/resources_rc.py

pyuic5 ../rsrc/forms/ui_about.ui        -o ../src/generated/ui_about.py
pyuic5 ../rsrc/forms/ui_mainwindow.ui   -o ../src/generated/ui_mainwindow.py
pyuic5 ../rsrc/forms/ui_new.ui          -o ../src/generated/ui_new.py
pyuic5 ../rsrc/forms/ui_preferences.ui  -o ../src/generated/ui_preferences.py
pyuic5 ../rsrc/forms/ui_properties.ui   -o ../src/generated/ui_properties.py
