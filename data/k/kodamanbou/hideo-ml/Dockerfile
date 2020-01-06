FROM tensorflow/tensorflow:latest-py3
MAINTAINER Hideo Kodama

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y \
        libpq-dev \
        build-essential \
        git \
        sudo \
        cmake zlib1g-dev libjpeg-dev xvfb libav-tools xorg-dev libboost-all-dev libsdl2-dev swig \
    && rm -rf /var/lib/apt/lists/*

RUN pip install "gym[atari,box2d,classic_control]"
ARG username=kodamanbou
ARG userid=114514

ARG home=/home/${username}
ARG workdir=${home}/ml

RUN adduser ${username} --uid ${userid} --gecos '' --disabled-password \
    && echo "${username} ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/${username} \
    && chmod 0440 /etc/sudoers.d/${username}

WORKDIR ${workdir}
RUN chown ${username}:${username} ${workdir}

EXPOSE 6006