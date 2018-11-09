from PyQt5 import QtWidgets
import sys
import platform
import ctypes
import os
import ErrorWindows as ew
from mainWindow import Ui_MainWindow
import actions as a

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
