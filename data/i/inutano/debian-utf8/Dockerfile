# Debian base image with utf-8
#
# VERSION 0.1

# Pull base image.
FROM debian:stable

# :)
MAINTAINER Tazro Inutano Ohta, inutano@gmail.com

# Install packages.
RUN apt-get update && \
    apt-get install -y locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8 && \
    rm -rf /var/lib/apt/lists/*

# Set LANG environment.
ENV LANG C.UTF-8

# Set default command.
CMD ["/bin/bash"]
