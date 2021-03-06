# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:0.9.19

MAINTAINER Derek Straka <derek@asterius.io>

# No Debian that's a bad Debian! We don't have an interactive prompt don't fail
ENV DEBIAN_FRONTEND noninteractive

# Use baseimage-docker's init
# https://blog.phusion.nl/2015/01/20/docker-and-the-pid-1-zombie-reaping-problem/
ENTRYPOINT ["/sbin/my_init", "--"]

# Where we build
RUN mkdir -p /var/build
WORKDIR /var/build

# Add the 32-bit arch for compat libraries
RUN dpkg --add-architecture i386

# Yocto's depends (plus sudo)
RUN apt-get --quiet --yes update && \
	apt-get --quiet --yes install gawk wget git-core diffstat unzip \
		texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev \
		xterm python sudo curl libssl-dev

# If you need to add more packages, just do additional RUN commands here
# I've intentionally done this so that the layers before this don't have
# to be regenerated and fetched since the above layer is big.
# RUN apt-get --quiet --yes install something
RUN apt-get --quiet --yes install tmux libncurses5-dev

# Add some debug utilities
RUN apt-get --quiet --yes install strace ltrace

# Add all the compat libraries needed to build imx-loader-native (It fails to build the libs itself)
RUN apt-get --quiet --yes install g++-multilib gcc-multilib lib32z1-dev \
        liblzo2-dev:i386 libusb-1.0-0-dev:i386 uuid-dev:i386

# Add more items for REALLY OLD yocto builds
RUN apt-get --quiet --yes install libsdl1.2-dev chrpath

# Set the default shell to bash instead of dash
RUN echo "dash dash/sh boolean false" | debconf-set-selections && dpkg-reconfigure dash

# clean up
RUN apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# utilize my_init from the baseimage to create the user for us
# the reason this is dynamic is so that the caller of the container
# gets the UID:GID they need/want made for them
RUN mkdir -p /etc/my_init.d
ADD create-user.sh /etc/my_init.d/create-user.sh

# bitbake wrapper to drop root perms
ADD bitbake.sh /usr/local/bin/bitbake
ADD bitbake.sh /usr/local/bin/bitbake-diffsigs
ADD bitbake.sh /usr/local/bin/bitbake-dumpsig
ADD bitbake.sh /usr/local/bin/bitbake-layers
ADD bitbake.sh /usr/local/bin/bitbake-prserv
ADD bitbake.sh /usr/local/bin/bitbake-selftest
ADD bitbake.sh /usr/local/bin/bitbake-worker
ADD bitbake.sh /usr/local/bin/bitdoc
ADD bitbake.sh /usr/local/bin/image-writer
ADD bitbake.sh /usr/local/bin/toaster
ADD bitbake.sh /usr/local/bin/toaster-eventreplay

ENV HOME /var/build

################################################################################
FROM alpine:3.4

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

# add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
RUN { \
        echo '#!/bin/sh'; \
        echo 'set -e'; \
        echo; \
        echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
    } > /usr/local/bin/docker-java \
    && chmod +x /usr/local/bin/docker-java

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:$JAVA_HOME/bin
ENV JAVA_VERSION 8u111
ENV JAVA_ALPINE_VERSION 8.111.14-r0

RUN set -x \
    && apk add --no-cache \
        openjdk8="$JAVA_ALPINE_VERSION" \
        libsodium \
        bash \
    && [ "$JAVA_HOME" = "$(docker-java)" ] \
    && ln -s /usr/lib/libsodium.so.18 /usr/lib/libsodium.so
