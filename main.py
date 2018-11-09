from PyQt5 import QtWidgets
import sys
import platform
import ctypes
import os
import ErrorWindows as ew
from mainWindow import Ui_MainWindow
from subprocess import run, Popen, PIPE

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

    dfucheck = run("dfu-programmer",stderr=PIPE, stdout=PIPE)
    errormsg = "No such file or directory: 'dfu-programmer'"
    if dfucheck.returncode==1 and errormsg in dfucheck.stdout.decode("utf-8"):
        run(["sudo apt install -y dfu-programmer"])
        print("installed dfu")
    else:
        print(dfucheck.stderr)
        print(dfucheck.stdout)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
