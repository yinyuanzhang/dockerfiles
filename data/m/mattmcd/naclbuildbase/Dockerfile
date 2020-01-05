FROM ubuntu:16.04
# Title: 'Install steps for OpenCV NaCl development on Ubuntu 14.04'
# Date: 20160828
# Author: Matt McDonnell (matt@matt-mcdonnell.com)
# Description: Steps for setting up a development environment for OpenCV
#   using Google Native Client (NaCl) on a bare Ubuntu 14.04 instance.
#   Tested on Amazon EC2 using a t2.micro instance running Ubuntu Server
#   14.04 LTS.  
#   

# Install packages needed for NaCl SDK and naclports
# Note that the NaCl SDK uses 32 bit versions of some libraries so these
# need to be installed as well as the 64 bit versions.  If a particular
# naclport fails to build check for missing 32 bit library first.
RUN dpkg --add-architecture i386 && apt-get update && apt-get -yqq install unzip git build-essential python python-dev\
  lib32stdc++6 cmake curl \
  gettext texinfo pkg-config \
  autoconf automake libtool make curl sed libglib2.0-dev libglib2.0-0:i386 zlib1g-dev:i386 libssl-dev:i386

# Install NaCl SDK
RUN curl -O https://storage.googleapis.com/nativeclient-mirror/nacl/nacl_sdk/nacl_sdk.zip
RUN unzip nacl_sdk.zip 

RUN cd nacl_sdk/ && ./naclsdk update -vv pepper_49

# Install depo-tools needed to install naclports
RUN git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git

# Add lines below (without #) to .bashrc, modifying for location and SDK version if necessary
ENV PATH="$HOME/depot_tools":"$PATH"
ENV NACL_SDK_ROOT="$HOME/nacl_sdk/pepper_49/"

# Install NaCl ports 
RUN mkdir naclports
RUN cd naclports && gclient config --name=src https://chromium.googlesource.com/webports && \
  gclient clean && gclient sync
