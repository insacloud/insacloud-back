#!/bin/bash

# Update
sudo apt-get update -y
sudo apt-get upgrade -y
# Install required packages
sudo apt-get install python-pip python-dev -y
sudo pip install -Iv ansible==1.9.3