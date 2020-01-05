FROM biohaz/basic_ubuntu:latest

#MAINTAINER BioH4z <https://github.com/BioH4z>

# Set the working directory to /home
WORKDIR /home

# Set shell for conda
SHELL ["/bin/bash", "-c"] 

#set User ROOT
USER root

# config problems about region and time 
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# install libraries
RUN apt-get install -y libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev \
	libjpeg-dev libpng-dev libtiff-dev \
	libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
	libxvidcore-dev libx264-dev \
	libgtk-3-dev \
	libopenblas-dev libatlas-base-dev liblapack-dev gfortran \
	libhdf5-serial-dev \
	python3-pandas \
	python-numpy python-scipy python-matplotlib python-sympy python-nose \
        && pip3 install tensorflow multiqc
	

RUN git clone https://github.com/wangk4/piRNN.git \
	&& git clone https://github.com/keras-team/keras.git \
	&& cd piRNN \
	&& pigz -d *.zip \
	&& cd /home/keras \
	&& python3 setup.py install
