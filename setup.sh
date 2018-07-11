#!/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal xfce4 vnc4server pip
sudo snap install spotify
xhost + localhost

pip install git+https://github.com/plamere/spotipy

cp ./xstartup ~/.vnc/xstartup
vncserver
