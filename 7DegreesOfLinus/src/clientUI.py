import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 624)
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
        self.nodeID = QtWidgets.QLCDNumber(self.centralwidget)
        self.nodeID.setGeometry(QtCore.QRect(400, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.nodeID.setFont(font)
        self.nodeID.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nodeID.setDigitCount(10)
        self.nodeID.setObjectName("nodeID")
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())