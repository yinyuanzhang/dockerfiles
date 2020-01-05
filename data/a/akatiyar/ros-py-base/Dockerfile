FROM ubuntu:16.04
MAINTAINER "Abhinav K"

RUN apt-get update \
    && apt-get install -yq lsb-release sudo \
    && sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' \
    && apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116 \
    && apt-get update \
    && apt-get install -yq python-dev python-pip \
    && pip install --upgrade distribute RPi.GPIO pyserial redis requests futures \
    && apt-get install -yq ros-kinetic-ros-base \
       python-rosinstall python-rosinstall-generator python-wstool build-essential \
    && rosdep init \
    && rosdep update \
    && echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc \
    && rm -rf /var/lib/apt/lists/*

RUN git clone git://git.drogon.net/wiringPi \
    && cd wiringPi \
    && ./build
