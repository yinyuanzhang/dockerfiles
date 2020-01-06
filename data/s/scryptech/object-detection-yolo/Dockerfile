FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

# ARG https_proxy
# ARG http_proxy

# Install python 3
RUN apt-get update --fix-missing && apt-get install -qy \
	python3-numpy python3-scipy python3-pip python3-setuptools \
	libjpeg-dev libtiff5-dev libjasper1 libjasper-dev libpng12-dev libavcodec-dev libavformat-dev \
	libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libgtk2.0-dev libatlas-base-dev \
	gfortran  python3-dev build-essential pkg-config wget \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

RUN pip3 install torch torchvision
RUN pip3 install Flask
RUN pip3 install pybase64
RUN pip3 install opencv-python
RUN pip3 install matplotlib
RUN pip3 install pandas

# Download Project
RUN cd
RUN mkdir detect
RUN cd detect
COPY pytorch-yolo-v3 ./
COPY v1.0 ./
RUN wget -O yolov3.weights https://s3-us-west-2.amazonaws.com/streem-weights/v1yolov3.weights
CMD python3 detect.py
