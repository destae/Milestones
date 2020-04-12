import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from client import *
from threading import Thread
from queue import *
from kv_store import *
from serialize import *

class Ui_MainWindow(object):
    def __init__(self, node_number: int):
        self.node_number = node_number
        print("HER HER")
        # self.c = Client(node_number)
 
    def add_item_keyvaluestore(self, msg: str):
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        item.setFont(font)
        item.setText(msg)
        self.availableList.addItem(item)  

    def add_key_value(self):
        print("Adding Key Value")

    def remove_key_value(self):
        print("Removing Key Value")

    def get_key_value(self):
        print("Get Key Value")

    def retrieve_key_value(self):
        print("Retrieve Key Value")

    def remove_item_keyvaluestore(self, msg: str):
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        item.setFont(font)
        item.setText(msg)
        self.availableList.removeItemWidget(item)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 624)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEditHome = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditHome.setGeometry(QtCore.QRect(10, 170, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textEditHome.setFont(font)
        self.textEditHome.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEditHome.setStyleSheet("QTextEdit {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.textEditHome.setPlaceholderText("")
        self.textEditHome.setObjectName("textEditHome")
        self.homeLabel = QtWidgets.QLabel(self.centralwidget)
        self.homeLabel.setGeometry(QtCore.QRect(20, 150, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.homeLabel.setFont(font)
        self.homeLabel.setObjectName("homeLabel")
        self.DataframeField = QtWidgets.QTextBrowser(self.centralwidget)
        self.DataframeField.setEnabled(True)
        self.DataframeField.setGeometry(QtCore.QRect(10, 280, 591, 331))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(12)
        self.DataframeField.setFont(font)
        self.DataframeField.setStyleSheet("QTextBrowser {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.DataframeField.setPlaceholderText("")
        self.DataframeField.setObjectName("DataframeField")
        self.addKeyValue = QtWidgets.QPushButton(self.centralwidget)
        self.addKeyValue.setGeometry(QtCore.QRect(430, 70, 171, 61))
        self.addKeyValue.clicked.connect(self.add_key_value)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addKeyValue.setFont(font)
        self.addKeyValue.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(211, 215, 207);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(238, 238, 236);\n"
"}")
        self.addKeyValue.setObjectName("addKeyValue")
        self.textEditKey = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditKey.setGeometry(QtCore.QRect(10, 230, 381, 35))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textEditKey.setFont(font)
        self.textEditKey.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEditKey.setStyleSheet("QTextEdit {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.textEditKey.setPlaceholderText("")
        self.textEditKey.setObjectName("textEditKey")
        self.keyLabel = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel.setGeometry(QtCore.QRect(10, 210, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.keyLabel.setFont(font)
        self.keyLabel.setObjectName("keyLabel")
        self.StartLabel = QtWidgets.QLabel(self.centralwidget)
        self.StartLabel.setGeometry(QtCore.QRect(150, 150, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.StartLabel.setFont(font)
        self.StartLabel.setObjectName("StartLabel")
        self.endLabel = QtWidgets.QLabel(self.centralwidget)
        self.endLabel.setGeometry(QtCore.QRect(290, 150, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.endLabel.setFont(font)
        self.endLabel.setObjectName("endLabel")
        self.textEditEnd = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditEnd.setGeometry(QtCore.QRect(270, 170, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textEditEnd.setFont(font)
        self.textEditEnd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEditEnd.setStyleSheet("QTextEdit {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.textEditEnd.setPlaceholderText("")
        self.textEditEnd.setObjectName("textEditEnd")
        self.textEditStart = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditStart.setGeometry(QtCore.QRect(140, 170, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textEditStart.setFont(font)
        self.textEditStart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEditStart.setStyleSheet("QTextEdit {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.textEditStart.setPlaceholderText("")
        self.textEditStart.setObjectName("textEditStart")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(20, 20, 351, 91))
        font = QtGui.QFont()
        font.setPointSize(100)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.logo.setFont(font)
        self.logo.setObjectName("logo")
        self.sublogo = QtWidgets.QLabel(self.centralwidget)
        self.sublogo.setGeometry(QtCore.QRect(70, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.sublogo.setFont(font)
        self.sublogo.setObjectName("sublogo")
        self.removeKeyValue = QtWidgets.QPushButton(self.centralwidget)
        self.removeKeyValue.setGeometry(QtCore.QRect(430, 140, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.removeKeyValue.setFont(font)
        self.removeKeyValue.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(211, 215, 207);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(238, 238, 236);\n"
"}")
        self.removeKeyValue.setObjectName("removeKeyValue")
        self.removeKeyValue.clicked.connect(self.remove_key_value)
        self.getKeyValue = QtWidgets.QPushButton(self.centralwidget)
        self.getKeyValue.setGeometry(QtCore.QRect(430, 210, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.getKeyValue.setFont(font)
        self.getKeyValue.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(211, 215, 207);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(238, 238, 236);\n"
"}")
        self.getKeyValue.setObjectName("getKeyValue")
        self.getKeyValue.clicked.connect(self.get_key_value)
        self.nodeID = QtWidgets.QLCDNumber(self.centralwidget)
        self.nodeID.setGeometry(QtCore.QRect(850, 10, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.nodeID.setFont(font)
        self.nodeID.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nodeID.setDigitCount(10)
        self.nodeID.setObjectName("nodeID")
        self.nodeID.display(self.node_number)
        self.DataframeField_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.DataframeField_2.setEnabled(True)
        self.DataframeField_2.setGeometry(QtCore.QRect(620, 280, 481, 331))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(12)
        self.DataframeField_2.setFont(font)
        self.DataframeField_2.setStyleSheet("QTextBrowser {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.DataframeField_2.setPlaceholderText("")
        self.DataframeField_2.setObjectName("DataframeField_2")
        self.availableList = QtWidgets.QListWidget(self.centralwidget)
        self.availableList.setGeometry(QtCore.QRect(620, 70, 280, 201))
        font = QtGui.QFont()
        self.availableList.setFont(font)
        self.availableList.setStyleSheet("QListWidget {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QScrollBar:vertical {              \n"
"    border: none;\n"
"    background:rgb(238, 238, 236);\n"
"    width:3px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(0, 0, 0);\n"
"    min-height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background: rgb(0, 0, 0);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    background: rgb(0, 0, 0);\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"}     \n"
"      ")
        self.availableList.setObjectName("availableList")
        self.retrieveKeyValue = QtWidgets.QPushButton(self.centralwidget)
        self.retrieveKeyValue.setGeometry(QtCore.QRect(910, 211, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.retrieveKeyValue.setFont(font)
        self.retrieveKeyValue.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(211, 215, 207);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(238, 238, 236);\n"
"}")
        self.retrieveKeyValue.setObjectName("retrieveKeyValue")
        self.retrieveKeyValue.clicked.connect(self.retrieve_key_value)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEditHome.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Mono\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.homeLabel.setText(_translate("MainWindow", "Home Node"))
        self.DataframeField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Typewriter\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:65536; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>"))
        self.addKeyValue.setText(_translate("MainWindow", "Add Key Value"))
        self.textEditKey.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Mono\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.keyLabel.setText(_translate("MainWindow", "Key Name"))
        self.StartLabel.setText(_translate("MainWindow", "Line Start"))
        self.endLabel.setText(_translate("MainWindow", "Line End"))
        self.textEditEnd.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Mono\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEditStart.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Mono\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.logo.setText(_translate("MainWindow", "EAU2"))
        self.sublogo.setText(_translate("MainWindow", "Client Application"))
        self.removeKeyValue.setText(_translate("MainWindow", "Remove Key Value"))
        self.getKeyValue.setText(_translate("MainWindow", "Get Key Value"))
        self.DataframeField_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Typewriter\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:65536; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>"))
        __sortingEnabled = self.availableList.isSortingEnabled()
        self.availableList.setSortingEnabled(False)
        self.availableList.setSortingEnabled(__sortingEnabled)
        self.retrieveKeyValue.setText(_translate("MainWindow", "Retrieve Key Value"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(2)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
