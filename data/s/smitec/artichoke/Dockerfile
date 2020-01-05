FROM ubuntu:14.04

# Derrived from https://github.com/ikester/blender-docker/blob/master/2.73a/Dockerfile

MAINTAINER Elliot Smith <elliot.smith91@gmail.com>

ENV BLENDER_MAJOR 2.73
ENV BLENDER_VERSION 2.73a
ENV BLENDER_BZ2_URL http://mirror.cs.umn.edu/blender.org/release/Blender$BLENDER_MAJOR/blender-$BLENDER_VERSION-linux-glibc211-x86_64.tar.bz2

RUN apt-get update && \
    apt-get install -y \
        curl \
        bzip2 \
        libfreetype6 \
        libgl1-mesa-dev \
        libglu1-mesa \
        libxi6 && \
    rm -rf /var/lib/apt/lists/*
 
RUN mkdir /usr/local/blender && \
    curl -SL "$BLENDER_BZ2_URL" -o blender.tar.bz2 && \
    tar -jxvf blender.tar.bz2 -C /usr/local/blender --strip-components=1 && \
    rm blender.tar.bz2
