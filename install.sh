#!/bin/bash

# Copy the with file to `/usr/bin/`
sudo cp cipher_utility /usr/bin/

# Modify the path to `icon.png` in cipher_utility.desktop
path=$PWD
if !([[ $(grep -o "Icon" cipher_utility.desktop) == "Icon" ]])
then
	echo "Icon=$path/images/icon.png" >> cipher_utility.desktop
fi

# Copy `cipher_utility.desktop` to `/usr/share/applications/`
sudo cp cipher_utility.desktop /usr/share/applications/
