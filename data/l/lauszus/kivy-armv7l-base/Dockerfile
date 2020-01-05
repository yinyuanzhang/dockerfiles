FROM balenalib/armv7hf-debian:buster

RUN [ "cross-build-start" ]

# Get apt-get dependencies.
RUN apt-get update
RUN apt-get -y install apt-utils
RUN apt-get -y install libsdl2-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-mixer-dev
RUN apt-get -y install libgstreamer1.0-dev gstreamer1.0-alsa gstreamer1.0-plugins-base
RUN apt-get -y install python3-dev libsmpeg-dev libswscale-dev libavformat-dev libavcodec-dev libjpeg-dev libtiff5-dev libx11-dev libmtdev-dev
RUN apt-get -y install python3-setuptools build-essential libgl1-mesa-dev libgles2-mesa-dev
RUN apt-get -y install xvfb pulseaudio xsel
RUN apt-get -y install python3-pip

RUN [ "cross-build-end" ]
