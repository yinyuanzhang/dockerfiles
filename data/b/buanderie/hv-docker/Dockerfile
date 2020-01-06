FROM ubuntu:18.04

MAINTAINER Nicolas Said <nicolas.said@gmail.com>

# install needed packages
RUN apt-get update -y \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
            libglfw3-dev libgles2-mesa-dev libavformat-dev libswscale-dev \
            libavdevice-dev libavfilter-dev libavresample-dev cmake cmake-curses-gui git \
            pkg-config libbsd-dev zlib1g-dev libpulse-dev qtmultimedia5-dev dos2unix p7zip-full cpio gzip genisoimage whois pwgen wget fakeroot isolinux xorriso \
            openssh-client build-essential libopencv-dev

# RUN ssh-keygen -q -t rsa -N '' -f /root/.ssh/id_rsa
