FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

RUN apt-get update && apt-get install -y autoconf automake libtool build-essential git wget curl python3 libglib2.0-0 libsm6 libxext6 libxrender1 libfontconfig1 kmod awscli
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py
RUN ln -sf /usr/bin/python3.5 /usr/bin/python && python -V && which python

# Make workspace
RUN mkdir /workspace
WORKDIR /workspace

# Darknet GPU mode build
RUN git clone https://github.com/pjreddie/darknet.git
RUN cd darknet && sed -i '/GPU=0/c\GPU=1' Makefile && make

# Download pre-trained Darknet53 & yolov3 model
RUN cd darknet && wget -q https://pjreddie.com/media/files/darknet53.conv.74 && wget -q https://pjreddie.com/media/files/yolov3.weights
