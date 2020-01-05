FROM ubuntu:14.04
MAINTAINER ngiy

RUN apt-get update && apt-get install -y git
RUN apt-get install -y wget sudo python-pip python-dev

# OpenCV install
RUN git clone https://github.com/jayrambhia/Install-OpenCV.git

# TODO
# RUN cd Install-OpenCV/Ubuntu && bash ./opencv_latest.sh

# cuda install
RUN wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_8.0.44-1_amd64.deb
RUN dpkg -i cuda-repo-ubuntu1404_8.0.44-1_amd64.deb
RUN apt-get update
# TODO
# RUN apt-get install -y cuda
