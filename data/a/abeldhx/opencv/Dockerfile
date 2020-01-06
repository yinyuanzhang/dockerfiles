FROM ubuntu:16.04

WORKDIR /usr/local/src/

RUN apt-get -qq update \
    && apt-get install -qqy  build-essential cmake git wget pkg-config  \
       	       	              ffmpeg libopencv-dev libgtk-3-dev python-numpy python3-numpy \
                       	      libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff5-dev \
		       	      libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libavresample-dev libxine2-dev \
		       	      libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libv4l-dev libtbb-dev \
		       	      qtbase5-dev libmp3lame-dev libopencore-amrnb-dev  \
		       	      libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev \
		       	      x264 v4l-utils unzip \
    && apt-get install -qqy libboost-dev libboost-filesystem-dev   \
    && apt-get install -qqy libopenblas-dev liblapack-dev \ 
    && apt-get clean \
    && wget -q https://github.com/Itseez/opencv/archive/3.1.0.zip \
    && unzip 3.1.0.zip \
    && cd opencv-3.1.0 \
    && mkdir build \
    && cd build/  \
    && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON .. \
    && make -j4 \
    && make install \
    && /bin/bash -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf' \
    && ldconfig \
    && rm -rf /usr/local/src/*
     








