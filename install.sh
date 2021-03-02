#!/bin/bash

# Copy the with file to `/usr/bin/`
sudo cp cipher_utility /usr/bin/

# Modify the path to `icon.png` in cipher_utility.desktop
path=$PWD
echo "Icon=$path/images/icon.png" >> cipher_utility.desktop

# Copy `cipher_utility.desktop` to `/usr/share/applications/`
sudo cp cipher_utility.desktop /usr/share/applications/
