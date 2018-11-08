import sys
import platform
import flashing as f
import ctypes
import os

import ErrorWindows as ew


from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QComboBox, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


from openFile import Open

osName = platform.system()
print(osName)

if osName=="Windows":
    myappid = 'qmk.pybox' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
elif osName=="Linux":
    if os.geteuid()!=0:
        print("please run as root")
        ew.root()
        sys.exit(1)


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'QMK PYBOX'
        self.left = 50
        self.top = 50
        self.width = 800
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.file = QLineEdit(self)
        self.file.move(20, 20)
        self.file.resize(480,20)

        # Create dropdown
        self.mcuList = QComboBox(self)
        self.mcuList.addItems(["atmega32u4", "at90usb1286"])
        self.mcuList.setEditable(True)
        self.mcuList.move(585,20)
        self.mcuList.resize(150,20)

        # Create flash button in the window
        self.flash = QPushButton('flash', self)
        self.flash.move(585,50)
        self.flash.resize(70,20)

        # Create reset button in the window
        self.reset = QPushButton('reset', self)
        self.reset.move(665,50)
        self.reset.resize(70,20)

        # Create open button in the window
        self.open = QPushButton('open', self)
        self.open.move(510,20)
        self.open.resize(70,20)

        # Create output textbox
        self.log = QPlainTextEdit(self)
        self.log.setReadOnly(True)
        self.log.move(20,120)
        self.log.resize(750,350)


        # connect button to function on_click
        self.flash.clicked.connect(self.flash_on_click)
        self.reset.clicked.connect(self.reset_on_click)
        self.open.clicked.connect(self.open_on_click)
        self.show()

    @pyqtSlot()
    def flash_on_click(self):
        textboxValue = self.file.text()
        mcuDropdown = self.mcuList.currentText()
        if (".hex" not in textboxValue):
            return
        #if os == "Windows":
        f.FlashDFU(mcuDropdown,textboxValue, self.log)

    @pyqtSlot()
    def reset_on_click(self):
        mcuDropdown = self.mcuList.currentText()
        f.ResetDFU(mcuDropdown, self.log)

    @pyqtSlot()
    def open_on_click(self):
        o = self.next=Open()
        print(o.returnValue())





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
