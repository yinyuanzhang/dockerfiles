FROM            ubuntu:latest
MAINTAINER      Bokum Guro <jiojiajiu@gmail.com>

RUN             apt-get update && \
                apt-get -y install build-essential cmake wget python2.7 python2.7-dev unzip && \
                apt-get -y clean
RUN             wget https://bootstrap.pypa.io/get-pip.py && python2.7 get-pip.py
RUN             pip install numpy
RUN             mkdir /opencv
WORKDIR         /opencv

RUN             wget https://github.com/Itseez/opencv/archive/3.0.0-rc1.zip && unzip 3.0.0-rc1.zip
RUN             cd opencv-3.0.0-rc1 && cmake . && make && make install
