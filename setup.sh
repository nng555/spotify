#!/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal xfce4 vnc4server
sudo apt install python-pip
sudo snap install spotify

pip install git+https://github.com/plamere/spotipy

vncserver
cp ./xstartup ~/.vnc/xstartup
