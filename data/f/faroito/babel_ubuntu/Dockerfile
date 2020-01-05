#
# Dockerfile for the Epitech Project: Arcade
# 	     With Ncurses, Allegro and SFML installed
#

FROM ubuntu:16.04

MAINTAINER Timothée Couble

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    git \
    gcc \
    clang \
    g++ \
    sudo \
    cmake \
    python3 \
    python-pip \
    python-dev

RUN pip install --upgrade pip 
RUN pip install conan

RUN conan remote add public-conan https://bintray.com/bincrafters/
RUN conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan
RUN conan remote add epitech https://api.bintray.com/conan/epitech/public-conan

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer