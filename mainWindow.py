# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from openFile import Open
import flashing as f
import easygui


from fileDrop import FileEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.file = FileEdit(self.centralwidget)
        self.file.setMaximumSize(QtCore.QSize(16777215, 20))
        self.file.setObjectName("file")
        self.horizontalLayout_3.addWidget(self.file)
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout_3.addWidget(self.openButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mcuList = QtWidgets.QComboBox(self.centralwidget)
        self.mcuList.setEditable(True)
        self.mcuList.setObjectName("mcuList")
        self.mcuList.addItem("")
        self.mcuList.addItem("")
        self.mcuList.addItem("")
        self.mcuList.addItem("")
        self.verticalLayout.addWidget(self.mcuList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.flashButton = QtWidgets.QPushButton(self.centralwidget)
        self.flashButton.setObjectName("flashButton")
        self.horizontalLayout.addWidget(self.flashButton)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.afBox = QtWidgets.QCheckBox(self.centralwidget)
        self.afBox.setObjectName("afBox")
        self.verticalLayout.addWidget(self.afBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.log = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.log.setMinimumSize(QtCore.QSize(0, 500))
        self.log.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.log.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.log.setFont(font)
        self.log.setMouseTracking(False)
        self.log.setAutoFillBackground(True)
        self.log.setStyleSheet("background-color:rgb(30, 30, 30);\n"
"color: rgb(230, 230, 230);\n"
"")
        self.log.setObjectName("log")
        self.verticalLayout_5.addWidget(self.log)
        self.file.raise_()
        self.log.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.flashButton.clicked.connect(self.flash_on_click)
        self.resetButton.clicked.connect(self.reset_on_click)
        self.openButton.clicked.connect(self.open_on_click)
        #self.afBox.clicked.connect(self.af_on_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QMK PYBOX"))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.openButton.setText(_translate("MainWindow", "Open"))
        self.mcuList.setItemText(0, _translate("MainWindow", "atmega32u4"))
        self.mcuList.setItemText(1, _translate("MainWindow", "at90usb1286"))
        self.mcuList.setItemText(2, _translate("MainWindow", "atmega32u2"))
        self.mcuList.setItemText(3, _translate("MainWindow", "atmega16u2"))
        self.flashButton.setText(_translate("MainWindow", "Flash"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.afBox.setText(_translate("MainWindow", "Auto-Flash WIP"))


    def flash_on_click(self):

        textboxValue = self.file.text()
        mcuDropdown = self.mcuList.currentText()
        if (".hex" not in textboxValue):
            self.log.appendHtml("<font color=\"Red\">Flashing failed - No hex file selected")
            return
        self.log.appendPlainText("Starting flashing...")
        f.FlashDFU(mcuDropdown,textboxValue, self.log)

    def reset_on_click(self):
        mcuDropdown = self.mcuList.currentText()
        f.ResetDFU(mcuDropdown, self.log)

    def open_on_click(self):
        path = ""
        try:
            while ".hex" not in path:
                path = easygui.fileopenbox()
            self.file.setText(path)
        except Exception as e:
            print(e)

        print(path)
