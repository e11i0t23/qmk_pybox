import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, qApp
from PyQt5.QtGui import QIcon

class Open(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Open'
        self.left = 20
        self.top = 20
        self.width = 640
        self.height = 480
        self.initUI()
        self.file = ""

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.openFileNameDialog()


        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if (".hex" in fileName):
            self.file = fileName
            print(fileName)

    def returnValue(self):
        return self.file
