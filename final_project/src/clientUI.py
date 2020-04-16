import sys
from final_project.src import utils
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from final_project.src.client import *
from threading import Thread
from queue import *
from final_project.src.kv_store import *
from final_project.src.serialize import *
from final_project.src.application import *
from final_project.src.dataframe import *

class Ui_MainWindow(object):
    def __init__(self, mw, node_number: int):
        self.node_number = node_number
        self.shared_queue = Queue()
        self.main_queue = Queue()
        self.app = Application(self.node_number, self.shared_queue)
        self.setupUi(mw)
        
        self.store_thread = Thread(target=self.update_store)
        self.store_thread.start()
    
    def update_store(self):
            while True:
                data = self.shared_queue.get(block=True, timeout=None)
                if (data[0] == 'add'):
                        self.add_item_keyvaluestore(data[1])
                elif (data[0] == 'remove'): 
                        for i in range(self.availableList.count()):
                                tmp_item = self.availableList.item(i)
                                if str(tmp_item.text()) == str(data[1]):
                                        self.availableList.takeItem(i)
                elif (data[0] == 'retrieve'):
                        msg_part1 = "Key Home Node: " + str(data[1].get_home()) + "\nKey Name: " + str(data[1].get_name()) + "\n" 
                        msg_part2 = "Dataframe:\n" + str(data[2].dataframe_to_string())
                        self.main_queue.put((msg_part1+msg_part2), block=True, timeout=None)
                        # self.DataframeField.setText(msg_part1 + msg_part2)
                        
    def add_item_keyvaluestore(self, msg: str):
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        item.setFont(font)
        item.setText(msg)
        self.availableList.addItem(item)  

    def add_key_value(self):
        if not(self.textEditHome.toPlainText() == "" or self.textEditKey.toPlainText() == ""):
                if(not(self.textEditDFA.toPlainText() == "")):
                        tmp_sch = Schema([utils.schema_from_list(eval(self.textEditDFA.toPlainText()))], 1, len(eval(self.textEditDFA.toPlainText())))
                        tmp_data = Dataframe([eval(self.textEditDFA.toPlainText())], tmp_sch)
                        tmp_key = Key(str(self.textEditKey.toPlainText()), int(self.textEditHome.toPlainText()))
                        self.app.add_value(tmp_key, tmp_data)    
                elif(not(self.textEditDFS.toPlainText() == "")):
                        tmp_sch = Schema([utils.determine_type(self.textEditDFS.toPlainText())], 1, 1)
                        tmp_data = Dataframe([[eval(self.textEditDFS.toPlainText())]], tmp_sch)
                        tmp_key = Key(str(self.textEditKey.toPlainText()), int(self.textEditHome.toPlainText()))
                        self.app.add_value(tmp_key, tmp_data)  
        print("Adding Key Value")

    def remove_key_value(self):
        if not(self.textEditHome.toPlainText == "" or self.textEditKey.toPlainText() == ""):
                tmp_key = Key(str(self.textEditKey.toPlainText()), int(self.textEditHome.toPlainText()))
                self.app.remove_value(tmp_key)
        print("Removing Key Value")

    def get_key_value(self):
        if not(self.textEditHome.toPlainText() == "" or self.textEditKey.toPlainText() == ""):
                tmp_key = Key(str(self.textEditKey.toPlainText()), int(self.textEditHome.toPlainText()))
                self.app.get_value(tmp_key)
                print("request sent")
                tmp_data = self.main_queue.get(block=True, timeout=None)
                self.DataframeField.setText(str(tmp_data))
        print("Get Key Value")

    def retrieve_key_value(self):
        tmp = self.availableList.currentItem()
        k = Key(tmp.text(), self.node_number)
        d = self.app.retrieve_value(k)
        self.DataframeField.setText(str(d.dataframe_to_string()))
        print("Retrieve Key Value")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1042, 539)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEditHome = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditHome.setGeometry(QtCore.QRect(10, 160, 531, 35))
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
        self.homeLabel.setGeometry(QtCore.QRect(20, 140, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.homeLabel.setFont(font)
        self.homeLabel.setObjectName("homeLabel")
        self.addKeyValue = QtWidgets.QPushButton(self.centralwidget)
        self.addKeyValue.setGeometry(QtCore.QRect(10, 470, 171, 61))
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
        self.addKeyValue.clicked.connect(self.add_key_value)
        self.textEditKey = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditKey.setGeometry(QtCore.QRect(10, 220, 531, 35))
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
        self.keyLabel.setGeometry(QtCore.QRect(10, 200, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.keyLabel.setFont(font)
        self.keyLabel.setObjectName("keyLabel")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(110, 20, 351, 91))
        font = QtGui.QFont()
        font.setPointSize(100)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.logo.setFont(font)
        self.logo.setObjectName("logo")
        self.sublogo = QtWidgets.QLabel(self.centralwidget)
        self.sublogo.setGeometry(QtCore.QRect(160, 110, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.sublogo.setFont(font)
        self.sublogo.setObjectName("sublogo")
        self.removeKeyValue = QtWidgets.QPushButton(self.centralwidget)
        self.removeKeyValue.setGeometry(QtCore.QRect(370, 470, 171, 61))
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
        self.getKeyValue.setGeometry(QtCore.QRect(190, 470, 171, 61))
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
        self.runApplication = QtWidgets.QPushButton(self.centralwidget)
        self.runApplication.setGeometry(QtCore.QRect(820, 80, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.runApplication.setFont(font)
        self.runApplication.setStyleSheet("QPushButton {\n"
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
        self.runApplication.setObjectName("runApplication")
        self.nodeID = QtWidgets.QLCDNumber(self.centralwidget)
        self.nodeID.setGeometry(QtCore.QRect(820, 10, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.nodeID.setFont(font)
        self.nodeID.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nodeID.setDigitCount(10)
        self.nodeID.setObjectName("nodeID")
        self.nodeID.display(self.node_number)
        self.DataframeField = QtWidgets.QTextBrowser(self.centralwidget)
        self.DataframeField.setEnabled(True)
        self.DataframeField.setGeometry(QtCore.QRect(550, 219, 481, 311)) ## 481 311
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
"")
        self.DataframeField.setPlaceholderText("")
        self.DataframeField.setObjectName("DataframeField")
        self.availableList = QtWidgets.QListWidget(self.centralwidget)
        self.availableList.setGeometry(QtCore.QRect(550, 9, 261, 201))
        font = QtGui.QFont()
        self.availableList.setFont(font)
        self.availableList.setStyleSheet("QListWidget {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    selection-background-color: black;\n"
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
        self.retrieveKeyValue.setGeometry(QtCore.QRect(820, 150, 211, 61))
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
        self.textEditDFA = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditDFA.setGeometry(QtCore.QRect(10, 280, 531, 111))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textEditDFA.setFont(font)
        self.textEditDFA.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEditDFA.setStyleSheet("QTextEdit {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.textEditDFA.setPlaceholderText("")
        self.textEditDFA.setObjectName("textEditDFA")
        self.keyLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel_2.setGeometry(QtCore.QRect(10, 260, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.keyLabel_2.setFont(font)
        self.keyLabel_2.setObjectName("keyLabel_2")
        self.textEditDFS = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditDFS.setGeometry(QtCore.QRect(10, 420, 531, 35))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textEditDFS.setFont(font)
        self.textEditDFS.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEditDFS.setStyleSheet("QTextEdit {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.textEditDFS.setPlaceholderText("")
        self.textEditDFS.setObjectName("textEditDFS")
        self.keyLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel_3.setGeometry(QtCore.QRect(10, 400, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.keyLabel_3.setFont(font)
        self.keyLabel_3.setObjectName("keyLabel_3")
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
        self.addKeyValue.setText(_translate("MainWindow", "Add Key Value"))
        self.textEditKey.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Mono\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.keyLabel.setText(_translate("MainWindow", "Key Name"))
        self.logo.setText(_translate("MainWindow", "EAU2"))
        self.sublogo.setText(_translate("MainWindow", "Client Application"))
        self.removeKeyValue.setText(_translate("MainWindow", "Remove Key Value"))
        self.getKeyValue.setText(_translate("MainWindow", "Get Key Value"))
        self.DataframeField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Typewriter\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:65536; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>"))
        __sortingEnabled = self.availableList.isSortingEnabled()
        self.availableList.setSortingEnabled(False)
        self.availableList.setSortingEnabled(__sortingEnabled)
        self.retrieveKeyValue.setText(_translate("MainWindow", "Retrieve Key Value"))
        self.textEditDFA.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Mono\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.keyLabel_2.setText(_translate("MainWindow", "Dataframe From Array"))
        self.textEditDFS.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Mono\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.keyLabel_3.setText(_translate("MainWindow", "Dataframe From Scalar"))
        self.runApplication.setText(_translate("MainWindow", "Run Application"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow, sys.argv[1])
    MainWindow.show()
    sys.exit(app.exec_())
