# Set the base image to Debian:wheezy
FROM ennexa/ubuntu:base

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential autogen libtool shtool

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
        autoconf automake pkg-config texinfo libass-dev libfreetype6-dev zlib1g-dev \
        python # Python is required for compiling yasm

