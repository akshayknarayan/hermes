#!/bin/bash

echo "Your password is needed to copy files."

sudo mkdir /opt/hermes
sudo cp lib/parser.py /opt/hermes
sudo cp lib/reader.py /opt/hermes

sudo pip-3.3 install feedparser

echo "Done! Use ./hermes.command to run the program."
