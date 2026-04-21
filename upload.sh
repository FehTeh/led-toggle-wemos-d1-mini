#!/bin/bash

# Script to upload all files from src/ to the Wemos D1 Mini device
# Assumes mpremote is installed and device is connected

echo "Uploading files to Wemos D1 Mini..."

# Create necessary directories on the device
mpremote fs mkdir -p www

# Upload all files recursively from src/ to the device root
mpremote fs cp -r src/ :

echo "Upload complete. Files uploaded:"
echo "- boot.py"
echo "- config.py"
echo "- main.py"
echo "- www/index.html"

echo "Reset the device to run the new code."