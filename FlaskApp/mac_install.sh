#!/bin/bash

# Check if Homebrew is installed
if ! command -v brew &> /dev/null
then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed."
fi

# Install Python 3.9 using Homebrew
if ! python3 --version | grep -q "3.9"
then
    echo "Installing Python 3.9..."
    brew install python@3.9
else
    echo "Python 3.9 is already installed."
fi

# Upgrade pip
python3 -m pip install --upgrade pip

# Install dependencies
python3 -m pip install --no-input flask selenium pyvo

# Installation complete message
echo
echo "-------------------------"
echo "!!INSTALLATION COMPLETE!!"
echo "-------------------------"
echo
