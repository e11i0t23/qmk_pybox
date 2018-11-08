from subprocess import run, Popen, PIPE
from os import path

def FlashDFUwin(mcu, file):
    print("Starting flashing...")
    erase = run(["dfu-programmer", mcu, "erase"], shell=True, stderr=PIPE)
    if ("dfu-programmer: no device present") in erase.stderr.decode("utf-8"):
        print("erase failed - Have you pressed the reset button")
        return
    elif erase.returncode == 0:
        print(erase.stderr.decode("utf-8"))

    print("flashing ", file, "to device")
    flash = run(["dfu-programmer", mcu, "flash", path.abspath(file)], shell=True, stderr=PIPE)
    #print(flash)
    if flash.returncode == 0:
        print(flash.stderr.decode("utf-8"))

    print("flash successful")
    print("resetting device")
    run(["dfu-programmer", mcu, "reset"], shell=True, stderr=PIPE)
    print("reset successful")
