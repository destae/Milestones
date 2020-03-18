from mainUI import Ui_MainWindow
from adapter import Adapter
from PyQt5 import QtCore, QtGui, QtWidgets
from dataframe import Dataframe
import sys

class Main:
    def  __init__(self):
        self.datalogger_filepath = None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
