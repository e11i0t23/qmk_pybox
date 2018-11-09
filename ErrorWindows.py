import PyQt5
from PyQt5 import QtWidgets


def root():
    app = QtWidgets.QApplication([])
    error_dialog = QtWidgets.QErrorMessage()
    error_dialog.showMessage('Please run as root')
    app.exec_()
