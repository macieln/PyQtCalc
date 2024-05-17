# pycalc.py

"""PyCalc is a simple calculator built with Python and PyQt"""

import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget

WINDOW_SIZE = 235


class PyCalcWindow(QMainWindow):
    """PyCalc's main window (GUI or view)."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)


def main():
    """PyCalc's main function."""

    py_calc_app = QApplication([])
    py_calc_window = PyCalcWindow()
    py_calc_window.show()

    sys.exit(py_calc_app.exec())


if __name__ == "__main__":
    main()
