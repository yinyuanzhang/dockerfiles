FROM arm32v7/python:3.7-slim

ARG ARCH=arm32v7

COPY qemu-arm-static /usr/bin

RUN apt-get update && apt-get install --no-install-recommends -y make gcc libc6-dev libxml2-dev libxslt1-dev libz-dev libczmq-dev libzmq5 procps usbutils

RUN pip3 install --no-cache-dir Cython pyserial pymodbus opcua pyzmq peewee kafka-python twisted RPi.GPIO spidev paho-mqtt netifaces cpplint
