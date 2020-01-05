FROM ubuntu:xenial
MAINTAINER orangain@gmail.com

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get build-dep -y opencv && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y dpkg-dev python3 python3-numpy python3-dev libgdal-dev libvtk6-dev doxygen dput fakeroot && \
    apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
