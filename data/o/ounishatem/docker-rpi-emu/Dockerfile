FROM ubuntu

MAINTAINER Hatem Ounis
LABEL Description="Qemu based emulation for raspberry pi using loopback images"

# Update package repository
RUN apt-get update

# Install required packages
RUN apt-get install -y --allow-unauthenticated \
    qemu \
    qemu-user-static \
    binfmt-support \
    parted \
    vim \
    sudo \
    wget \
    cron \
    gnupg2 \
    apt-utils \
    curl \
    python \
    python-pip \
    python3 \
    python3-pip \
    net-tools

# Clean up after apt
RUN apt-get clean
RUN rm -rf /var/lib/apt

# Setup working directory
RUN mkdir -p /usr/rpi
WORKDIR /usr/rpi

# Setup home directory
RUN mkdir -p /home/pi

COPY scripts/* /usr/rpi/
