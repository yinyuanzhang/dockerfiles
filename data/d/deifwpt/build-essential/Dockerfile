FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq \
 && apt-get install -qq -y \
	build-essential ssh-client git subversion curl wget smbclient \
	check psmisc bc tofrodos \
	autoconf automake libtool gettext autoconf-archive pkg-config \
	doxygen \
	libjansson-dev \
	zlib1g-dev \
	ruby ruby-dev bundler \
	ssmtp \
	libnl-3-dev \
	libnl-cli-3-dev libnl-genl-3-dev libnl-nf-3-dev libnl-route-3-dev \
	ucspi-unix ucspi-tcp \
	python3-pip \
	cppcheck \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN gem install ceedling --version 0.28.3

# /bin/sh should be bash
RUN echo "dash dash/sh boolean false" | debconf-set-selections \
 && dpkg-reconfigure dash

# Install skalibs
RUN git clone https://github.com/skarnet/skalibs.git \
 && cd skalibs \
 && git checkout v2.6.2.0 \
 && ./configure \
 && make install \
 && cd .. \
 && rm -rf skalibs

# Install labgrid-tools, note python3-pip above
RUN git clone https://github.com/deif-wpt/labgrid.git /opt/labgrid \
 && pip3 install -e /opt/labgrid
