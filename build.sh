#!/bin/bash

# Author: Marley Mulvin Broome
# Date: 2023-07-19
# Description: This script builds the JSpeak addon and copies it to the Anki addons directory.
#              This script is intended to be run from the root of the project directory.

deploy() {
  real_addon_dir="$ADDON_DIR/JSpeak"
  source_dir="./src"

  if [ -d "$real_addon_dir" ]; then
      echo "Removing old JSpeak addon..."
      rm -rf "$real_addon_dir" || exit 1
  fi

  echo "Copying files to addons directory..."
  echo "$source_dir -> $real_addon_dir"
  cp -r "$source_dir" "$real_addon_dir" || exit 1
}

package() {
  echo "Building anki package for JSpeak..."

  if [ -f "JSpeak.ankiaddon" ]; then
      echo "Removing old JSpeak.ankiaddon..."
      rm "JSpeak.ankiaddon" || exit 1
  fi

  cd src || exit 1
  zip -r "../JSpeak.ankiaddon" ./* || exit 1
  cd ../ || exit 1
}

usage() {
  echo "Usage: build.sh [-dh] [-a <addons directory>]"
  echo "Builds the JSpeak addon into a .ankiaddon file"
  echo "Options:"
  echo "  -d  Deploy the addon to the Anki addons directory."
  echo "    This will overwrite any existing JSpeak addon."
  echo "  -h  Display this help message."
  echo "  -a  Manually specify the addons directory."
  exit 0
}

check_dirs() {
  anki_dir=$(which anki)

  if [ -z "$anki_dir" ]; then
      echo "Anki not found. Please install Anki and try again."
      exit 1
  fi

  if [ ! -d "$ADDON_DIR" ]; then
      echo "Addons directory not found at '$ADDON_DIR'. Where is your addons folder?"
      exit 1
  fi
}


ADDON_DIR="$HOME/.local/share/Anki2/addons21"

deploy="false"

if [ "$1" = "help" ]; then
  usage
fi

# get optional options of -d
while getopts "dha:" opt; do
    case "$opt" in
        d)
            deploy="true"
            echo "DEPLOY"
            ;;
        h)
            usage
            ;;
        a)
            ADDON_DIR="$OPTARG"
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
    esac
done

# Build the project
echo "Building the project..."

check_dirs

# removing all pycache files
echo "Removing pycache files..."
find . -name "__pycache__" -type d -exec rm -rf {} + || exit 1

package

if [ "$deploy" = "true" ]; then
    deploy
fi

echo "Done!"