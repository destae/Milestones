from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow, QPushButton


class Ui_MainWindow(object):
    def __init__(self):
        self.filePath = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 294)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.selectFile = QtWidgets.QPushButton(self.centralwidget)
        self.selectFile.clicked.connect(self.fileSelect)
        self.selectFile.setGeometry(QtCore.QRect(510, 130, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(16)
        self.selectFile.setFont(font)
        self.selectFile.setStyleSheet("QPushButton#selectFile {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#selectFile:hover {\n"
"    background-color: rgb(211, 215, 207);\n"
"}\n"
"\n"
"QPushButton#selectFile:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(238, 238, 236);\n"
"}")
        self.selectFile.setObjectName("selectFile")

        self.fileName = QtWidgets.QTextBrowser(self.centralwidget)
        self.fileName.setEnabled(False)
        self.fileName.setGeometry(QtCore.QRect(480, 40, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(13)
        self.fileName.setFont(font)
        self.fileName.setStyleSheet("QTextBrowser#fileName {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.fileName.setObjectName("fileName")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 461, 291))
        self.logo.setObjectName("logo")

        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.clicked.connect(self.generateDataframe)
        self.generate.setGeometry(QtCore.QRect(510, 210, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(16)
        self.generate.setFont(font)
        self.generate.setStyleSheet("QPushButton#generate {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#generate:hover {\n"
"    background-color: rgb(211, 215, 207);\n"
"}\n"
"\n"
"QPushButton#generate:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(238, 238, 236);\n"
"}")
        self.generate.setObjectName("generate")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectFile.setText(_translate("MainWindow", "Select File"))
        self.fileName.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Serif\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:65536; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>"))
        self.logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/logo/eau_logo.png\"/></p></body></html>"))
        self.generate.setText(_translate("MainWindow", "Generate"))

    def fileSelect(self):
        self.filePath = QFileDialog.getOpenFileName()[0]
        self.fileName.setText(self.filePath)

    def retrieveFileName(self):
        return self.filePath

    def generateDataframe(self):
        print("Will generate the Dataframe here")

import resources_rc
