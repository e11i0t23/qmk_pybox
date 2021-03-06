from PyQt5 import QtWidgets
import sys
import platform
import ctypes
import os
from lib import ErrorWindows as ew
from lib.mainWindow import Ui_MainWindow
from subprocess import run, Popen, PIPE
import shutil


def main():
    osName = platform.system()
    print(osName)
    if osName=="Windows":
        myappid = 'qmk.pybox' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    elif osName=="Linux":
        # if os.geteuid()!=0:
        #     print("please run as root")
        #     ew.root()
        #     sys.exit(1)

        dfucheck = shutil.which("dfu-programmer")
        if dfucheck == None:
            run("sudo apt install -y dfu-programmer", shell=True)
            print("installed dfu")


    if True:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
