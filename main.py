import sys
import platform
import flashing as f

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

os = platform.system()

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'QMK PYBOX'
        self.left = 50
        self.top = 50
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.file = QLineEdit(self)
        self.file.move(20, 20)
        self.file.resize(280,20)

        # Create a button in the window
        self.flash = QPushButton('flash', self)
        self.flash.move(20,80)

        # connect button to function on_click
        self.flash.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.file.text()
        if (".hex" not in textboxValue):
            return
        if os == "Windows":
            f.FlashDFUwin("atmega32u4",textboxValue)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
