FROM ubuntu:bionic

RUN apt-get update && \
apt-get -y install build-essential gcc-avr avr-libc curl git bzip2 make python clang cmake cpputest cppcheck && \
curl -OSs https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-rm/7-2018q2/gcc-arm-none-eabi-7-2018-q2-update-linux.tar.bz2 && \
tar -xf gcc-arm-none-eabi-7-2018-q2-update-linux.tar.bz2 --strip-components=1 -C /usr/
