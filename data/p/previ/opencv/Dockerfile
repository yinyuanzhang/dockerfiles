FROM ubuntu:latest
 
MAINTAINER Roberto Previtera <roberto.previtera@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && \
    apt-get install -y \
      build-essential \
      wget \
      unzip

RUN apt-get -y install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev libjpeg-dev
RUN apt-get -y install python-pip python-numpy python-dev

RUN apt-get install cmake cmake-curses-gui -y

WORKDIR /tmp/downloads

RUN wget -O opencv-2.4.11.zip http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.11/opencv-2.4.11.zip/download

RUN unzip opencv-2.4.11.zip && \
      cd opencv-2.4.11 && \
      mkdir build && \
      cd build && \
      cmake -DCMAKE_BUILD_TYPE=RELEASE -D INSTALL_C_EXAMPLES=OFF -D INSTALL_PYTHON_EXAMPLES=OFF -D BUILD_EXAMPLES=OFF  .. && \
      make -j4 && \
      sudo make install && \
      cd ../.. && \
      rm -rf opencv-2.4.11*

