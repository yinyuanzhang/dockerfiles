FROM ubuntu:bionic

RUN apt-get update -q && \
    apt-get install -y git make avr-libc binutils-avr gcc-avr avrdude libusb-dev

WORKDIR /build
