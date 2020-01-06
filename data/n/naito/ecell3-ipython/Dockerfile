# Installs E-Cell3
# Another Docker container should build from this one to get services like the notebook

FROM ubuntu:14.04

MAINTAINER Yasuhiro Naito <ynaito@e-cell.org>

ENV DEBIAN_FRONTEND noninteractive

# Make sure apt is up to date
RUN apt-get update
RUN apt-get upgrade -y

# dependencies
RUN apt-get install -y -q build-essential make autoconf libtool automake gcc g++ zlib1g-dev git

# install LibSBML
RUN apt-get install -y -q bzip2 libbz2-dev libxml++2.6-dev
RUN apt-get install -y -q python python-dev python-pip
RUN pip install python-libsbml

RUN apt-get install -y -q python-numpy python-ply
#RUN apt-get install -y -q ipython-notebook
RUN apt-get install -y -q python-matplotlib
RUN pip install "ipython[notebook]"

# RUN apt-get install -y -q python-gtk2 python-gnome2

RUN apt-get install -y -q libboost-random-dev libboost-python-dev gsl-bin libgsl0-dev

RUN cd /tmp; git clone git://github.com/ecell/ecell3
RUN cd /tmp/ecell3; sh autogen.sh && ./configure --disable-gui && make && make install

RUN ln -s /usr/local/lib/libecs* /usr/lib/
RUN ln -s /usr/local/lib/libemc* /usr/lib/

VOLUME /ecell3
WORKDIR /ecell3
