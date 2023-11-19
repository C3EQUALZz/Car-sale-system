import sys

from PyQt6 import QtWidgets

from gui_interaction import MainFrame


def read_styles(filename):
    with open(filename, "r") as file:
        return file.read()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(read_styles("gui_interaction/icons/styles.qss"))
    main_frame = MainFrame()
    main_frame.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
