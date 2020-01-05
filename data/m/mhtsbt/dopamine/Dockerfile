FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y git xvfb ffmpeg python-opencv python3.6 python3-pip python3-dev

# make python 3.6 the default version
RUN rm /usr/bin/python3
RUN rm /usr/bin/python
RUN ln -s /usr/bin/python3.6 /usr/bin/python3
RUN ln -s /usr/bin/python3.6 /usr/bin/python

# upgrade pip
RUN python -m pip install --upgrade pip

# python packages
RUN python -m pip install opencv-python
RUN python -m pip install gym gym[atari] 
RUN python -m pip install numpy 
RUN python -m pip install matplotlib 
RUN python -m pip install atari_py
RUN python -m pip install tensorboardX
RUN python -m pip install torch
RUN python -m pip install ray
RUN python -m pip install absl-py
RUN python -m pip install atari-py
RUN python -m pip install gin-config
RUN python -m pip install tensorflow-gpu==1.12.0