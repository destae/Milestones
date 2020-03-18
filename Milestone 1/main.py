from mainUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import adapter
import dataframe

class Main:
    def  __init__(self):
        self.datalogger_filepath = None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
