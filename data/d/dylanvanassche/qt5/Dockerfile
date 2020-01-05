FROM ubuntu:14.04
MAINTAINER Ali Diouri <alidiouri@gmail.com>

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN sed -i 's/ universe/ universe multiverse/' /etc/apt/sources.list
RUN apt update &&                  \
    apt upgrade -y &&              \
    apt install -y                 \
        git                        \
        wget                       \
        xvfb                       \
        flex                       \
        bison                      \
        libxcursor-dev             \
        libxcomposite-dev          \
        software-properties-common \
        build-essential            \
        libssl-dev                 \
        libxcb1-dev                \
        libx11-dev                 \
        libgl1-mesa-dev            \
        libudev-dev                \
        qt5-default

WORKDIR /home/root/

CMD ["/bin/bash"]