from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 624)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectFile = QtWidgets.QPushButton(self.centralwidget)
        self.selectFile.setGeometry(QtCore.QRect(660, 190, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selectFile.setFont(font)
        self.selectFile.setStyleSheet("QPushButton {\n"
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
        self.selectFile.setObjectName("selectFile")
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(660, 120, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.generate.setFont(font)
        self.generate.setStyleSheet("QPushButton {\n"
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
        self.generate.setObjectName("generate")
        self.fileName = QtWidgets.QTextBrowser(self.centralwidget)
        self.fileName.setEnabled(True)
        self.fileName.setGeometry(QtCore.QRect(600, 20, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(12)
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
        self.fileName.setPlaceholderText("")
        self.fileName.setObjectName("fileName")
        self.treeGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.treeGroupBox.setGeometry(QtCore.QRect(410, 270, 421, 291))
        self.treeGroupBox.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.treeGroupBox.setTitle("")
        self.treeGroupBox.setObjectName("treeGroupBox")
        self.treeSelectedData = QtWidgets.QTreeWidget(self.treeGroupBox)
        self.treeSelectedData.setEnabled(True)
        self.treeSelectedData.setGeometry(QtCore.QRect(10, 10, 401, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeSelectedData.sizePolicy().hasHeightForWidth())
        self.treeSelectedData.setSizePolicy(sizePolicy)
        self.treeSelectedData.setMinimumSize(QtCore.QSize(401, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.treeSelectedData.setFont(font)
        self.treeSelectedData.setStyleSheet("QTreeWidget#treeSelectedData {\n"
"    background-color: rgb(238, 238, 236);\n"
"      border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    selection-background-color: black;\n"
"}\n"
"\n"
"")
        self.treeSelectedData.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeSelectedData.setLineWidth(1)
        self.treeSelectedData.setItemsExpandable(True)
        self.treeSelectedData.setAllColumnsShowFocus(False)
        self.treeSelectedData.setColumnCount(2)
        self.treeSelectedData.setObjectName("treeSelectedData")
        self.treeSelectedData.headerItem().setText(0, "Node Number")
        self.treeSelectedData.headerItem().setTextAlignment(0, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.treeSelectedData.headerItem().setFont(0, font)
        self.treeSelectedData.headerItem().setText(1, "Port Number")
        self.treeSelectedData.headerItem().setTextAlignment(1, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.treeSelectedData.headerItem().setFont(1, font)
        self.treeSelectedData.header().setCascadingSectionResizes(True)
        self.treeSelectedData.header().setDefaultSectionSize(200)
        self.treeSelectedData.header().setMinimumSectionSize(70)
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
        self.DataframeField.setGeometry(QtCore.QRect(10, 280, 381, 211))
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
        self.addKeyValue.setGeometry(QtCore.QRect(100, 500, 171, 61))
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
        self.logo.setGeometry(QtCore.QRect(220, 20, 351, 91))
        font = QtGui.QFont()
        font.setPointSize(100)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.logo.setFont(font)
        self.logo.setObjectName("logo")
        self.sublogo = QtWidgets.QLabel(self.centralwidget)
        self.sublogo.setGeometry(QtCore.QRect(290, 100, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.sublogo.setFont(font)
        self.sublogo.setObjectName("sublogo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectFile.setText(_translate("MainWindow", "Select File"))
        self.generate.setText(_translate("MainWindow", "Generate"))
        self.fileName.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Typewriter\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:65536; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>"))
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
        self.sublogo.setText(_translate("MainWindow", "Main Application"))
