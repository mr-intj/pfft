#
pyrcc5 ../rsrc/resources.qrc            -o ../src/generated/resources_rc.py

pyuic5 ../rsrc/forms/ui_about.ui        -o ../src/generated/ui_about.py
pyuic5 ../rsrc/forms/ui_mainwindow.ui   -o ../src/generated/ui_mainwindow.py
pyuic5 ../rsrc/forms/ui_preferences.ui  -o ../src/generated/ui_preferences.py
pyuic5 ../rsrc/forms/ui_properties.ui   -o ../src/generated/ui_properties.py
