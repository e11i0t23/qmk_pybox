from subprocess import run, Popen, PIPE
from os import path

def FlashDFUwin(mcu, file):
    print("Starting flashing...")
    erase = run(["dfu-programmer.exe", mcu, "erase"], shell=True, capture_output=True)
    if ("dfu-programmer: no device present") in erase.stderr.decode("utf-8"):
        print("erase failed - Have you pressed the reset button")
        return
    elif erase.returncode == 0:
        print(erase.stderr.decode("utf-8"))
        
    print("flashing ", file, "to device")
    flash = run(["dfu-programmer.exe", mcu, "flash", path.abspath(file)], shell=True, capture_output=True)
    #print(flash)
    if flash.returncode == 0:
        print(flash.stderr.decode("utf-8"))

    print("flash successful")
    print("resetting device")
    run(["dfu-programmer.exe", mcu, "reset"], shell=True, capture_output=True)
    print("reset successful")
