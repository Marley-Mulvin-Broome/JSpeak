#!/bin/bash

# Author: Marley Mulvin Broome
# Date: 2021-08-15
# Description: This script builds the JSpeak addon and copies it to the Anki addons directory.
#              This script is intended to be run from the root of the project directory.

ADDON_DIR="$HOME/.local/share/Anki2/addons21"

# Build the project
echo "Building the project..."
anki_dir=$(which anki)

if [ -z "$anki_dir" ]; then
    echo "Anki not found. Please install Anki and try again."
    exit 1
fi

if [ ! -d "$ADDON_DIR" ]; then
    echo "Addons directory not found at '$ADDON_DIR'. Where is your addons folder?"
    exit 1
fi

real_addon_dir="$ADDON_DIR/JSpeak"

if [ -d "$real_addon_dir" ]; then
    echo "Removing old JSpeak addon..."
    rm -rf "$real_addon_dir" || exit 1
fi

echo "Copying files to addons directory..."
echo "../JSpeak -> $real_addon_dir"
cp -r "../JSpeak" "$real_addon_dir" || exit 1

echo "Done!"