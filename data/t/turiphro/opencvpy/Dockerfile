FROM ubuntu:16.04

## Fixing unicode requirement error
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update && apt-get upgrade -y && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    cmake build-essential \
    git \
    python3-pip python3-numpy python3-scipy python3-dev \
    libeigen3-dev libjpeg-dev libpng-dev libtiff.dev libjasper-dev libssl-dev \
    # for GUI:
    libgtk2.0-dev libdc1394-22-dev

ENV OPENCV_VERSION 3.1.0

COPY build.sh /build.sh
RUN bash /build.sh \
    && rm /build.sh

RUN apt-get purge -y cmake build-essential git
RUN apt-get autoremove -y
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/
