#!/bin/sh

sudo apt-get update
sudo apt-get install -y python3 python3-pip dfu-programmer
sudo pip3 install easygui pyinstaller PyQt5
sudo pyinstaller entry_point.py --onefile --name 'QMK-Pybox'
cp ./dist/QMK-Pybox ~/Desktop
sudo cp ./50-QMK-Pybox.rules /etc/udev/rules.d/
