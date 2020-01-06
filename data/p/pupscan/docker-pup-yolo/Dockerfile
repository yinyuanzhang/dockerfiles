FROM ubuntu:18.04


RUN apt-get update && apt-get install -y \
	sudo \
	python3 \		
	python \
	curl \
	git \
	libsm6 libxext6 libxrender-dev

RUN sudo apt-get install -y \
	wget \
	python3-pip \
	unzip 


RUN pip3 install tensorflow==1.5
RUN pip3 install Cython
RUN pip3 install opencv-python
