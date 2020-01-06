FROM ubuntu:16.04

# Update Packages
RUN apt-get update -y

# Install Python Dev Tools
RUN apt-get install -q -y python-pip python-dev python-setuptools build-essential pkg-config

# Install packages for pip dependencies
RUN apt-get install -q -y libpng-dev libfreetype6-dev

# Add and install Python modules
ADD requirements.txt /app/requirements.txt
RUN cd /app; pip install --no-cache-dir -r requirements.txt

