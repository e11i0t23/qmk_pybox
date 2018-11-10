#!/bin/sh

sudo apt-get update
sudo apt-get install -y python3 python3-pip
sudo pip3 install easygui pyinstaller PyQt5
pyinstaller entry_point.py
