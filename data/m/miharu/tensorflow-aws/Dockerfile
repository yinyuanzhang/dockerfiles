FROM ubuntu:16.04

MAINTAINER Toshiaki Inahata <inahata@miharu.co.jp>


#
# Set UP Ubuntu
#
RUN apt-get update && apt-get upgrade -y \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
        git curl wget unzip vim \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*


#
# Set UP AWS CLI
RUN apt-get update && apt-get install -y \
        python-pip python-dev \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && pip install awscli


#
# Install Python
#
RUN apt-get update && apt-get install -y \
        python3-pip python3-dev \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && pip3 install --upgrade pip


#
# Install Libraries
#
RUN pip3 install Pillow && pip3 install --upgrade tensorflow==1.6.0


#
# Install OpenCV
#
RUN apt-get update && apt-get install -y \
        python-opencv \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && echo 'ln /dev/null /dev/raw1394' >> ~/.bashrc
