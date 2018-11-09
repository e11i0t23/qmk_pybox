from subprocess import run, Popen, PIPE
from os import path
import platform

def FlashDFU(mcu, file, log):
    erase = run(["dfu-programmer", mcu, "erase"], stderr=PIPE, stdout=PIPE)
    if ("dfu-programmer: no device present") in erase.stderr.decode("utf-8"):
        log.appendHtml("<font color=\"Red\">erase failed - Have you pressed the reset button")
        return
    elif erase.returncode == 0:
        log.appendPlainText(erase.stderr.decode("utf-8"))

    log.appendPlainText(("flashing " + file + " to device"))
    flash = run(["dfu-programmer", mcu, "flash", path.abspath(file)], stderr=PIPE, stdout=PIPE)
    #print(flash)
    if flash.returncode == 0:
        log.appendPlainText(flash.stderr.decode("utf-8"))

    print("flash successful")
    print("resetting device")
    run(["dfu-programmer", mcu, "reset"], stderr=PIPE, stdout=PIPE)
    print("reset successful")


def ResetDFU(mcu, log):
    reset = run(["dfu-programmer", mcu, "reset"], stderr=PIPE, stdout=PIPE)
    if ("dfu-programmer: no device present") in reset.stderr.decode("utf-8"):
        log.appendHtml("<font color=\"Red\">Error Reset Failed No Device Present")
        return
    elif reset.returncode == 0:
        log.appendPlainText("Reset successful")
