import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication

from main_window import MainWindow


def main():
    # Set these here so we can use the default QSettings constructor everywhere else
    QCoreApplication.setOrganizationName("pfft")
    QCoreApplication.setApplicationName("pfft")

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
