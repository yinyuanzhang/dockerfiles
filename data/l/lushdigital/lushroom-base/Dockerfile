# lushroom-base Dockerfile

FROM balenalib/raspberrypi3-debian:stretch

ENTRYPOINT []

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get upgrade

RUN apt-get install -y --no-install-recommends \
  apt-utils build-essential gcc make git wget ntp ifmetric man iputils-ping

RUN apt-get install -y libfreetype6 dbus dbus-*dev libsmbclient libssh-4 \
  libpcre3 fonts-freefont-ttf

RUN apt-get -y install fbset omxplayer \
    python3-dev python3-pip python3-pil python3-numpy python3-scipy

RUN apt-get clean

RUN pip3 install rpi.gpio
RUN pip3 install pycrypto
RUN pip3 install requests
RUN pip3 install tinkerforge
RUN pip3 install pillow
RUN pip3 install rdflib

RUN [ "cross-build-end" ]

