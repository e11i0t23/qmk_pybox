import sys
import platform
import flashing as f
import ctypes
myappid = 'qmk.pybox' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QComboBox, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

os = platform.system()

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'QMK PYBOX'
        self.left = 50
        self.top = 50
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.file = QLineEdit(self)
        self.file.move(20, 20)
        self.file.resize(280,30)

        # Create dropdown
        self.mcuList = QComboBox(self)
        self.mcuList.addItems(["atmega32u4", "at90usb1286"])
        self.mcuList.move(320,20)

        # Create a button in the window
        self.flash = QPushButton('flash', self)
        self.flash.move(20,80)

        # Create output textbox
        self.log = QPlainTextEdit(self)
        self.log.setReadOnly(True)
        self.log.move(20,120)
        self.log.resize(450,350)


        # connect button to function on_click
        self.flash.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.file.text()
        mcuDropdown = self.mcuList.currentText()
        if (".hex" not in textboxValue):
            return
        #if os == "Windows":
        f.FlashDFU(mcuDropdown,textboxValue, self.log)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
