FROM ubuntu:16.04

RUN apt-get update && apt-get install -y libc6-i386 lib32z1 iputils-ping

WORKDIR /xware
ADD ./Xware3.0.32.253_x86_32_glibc /xware


VOLUME /data
