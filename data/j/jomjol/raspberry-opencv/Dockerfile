FROM balenalib/raspberrypi3

RUN [ "cross-build-start" ]

WORKDIR /

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install apt-utils

RUN apt-get -y install python3-dev python3-pip
RUN apt-get -y install python3-h5py

RUN apt-get -y install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
RUN apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
RUN apt-get -y install libxvidcore-dev libx264-dev
RUN apt-get -y install libgtk2.0-dev libgtk-3-dev
RUN apt-get -y install libatlas-base-dev gfortran
RUN apt-get -y install libilmbase-dev libopenexr-dev libgstreamer1.0-dev
RUN apt-get -y install libqtgui4 libqt4-test

RUN apt-get -y install python3-numpy
RUN apt-get -y install python-opencv

COPY wheels ./wheels
RUN pip3 install --no-cache-dir ./wheels/opencv_contrib_python-4.1.1.26-cp37-cp37m-linux_armv7l.whl

RUN [ "cross-build-end" ]

ENV LD_PRELOAD=$LD_PRELOAD:/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0
