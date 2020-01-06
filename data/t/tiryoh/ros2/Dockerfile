FROM ubuntu:18.04
LABEL maintainer "Tiryoh <tiryoh@gmail.com>"
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -q && \
    apt-get upgrade -yq && \
    apt-get install -yq wget curl git build-essential vim sudo lsb-release locales bash-completion tzdata && \
    rm -rf /var/lib/apt/lists/*
RUN useradd -m -d /home/ubuntu ubuntu -p $(perl -e 'print crypt("ubuntu", "salt"),"\n"') && \
    echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN locale-gen en_US.UTF-8
USER ubuntu
WORKDIR /home/ubuntu
ENV HOME=/home/ubuntu
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8
RUN git clone https://github.com/Tiryoh/ros2_setup_scripts_ubuntu.git && \
	cd ros2_setup_scripts_ubuntu && \
	./run.sh && \
	sudo rm -rf /var/lib/apt/lists/*
