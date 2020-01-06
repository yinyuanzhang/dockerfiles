FROM ubuntu:19.10
LABEL maintainer="maya2250.dev@gmail.com"

ARG USER="guest"
ARG LINUXBREW_DEPENDENCIES="build-essential curl file git ruby"
ARG BUILD_DEPENDENCIES="language-pack-en sudo python3 python3-pip ansible"

ENV DEBIAN_FRONTEND noninteractive

RUN set -ux && \
        useradd -m -s /bin/bash ${USER} && \
        echo "${USER}:password" | chpasswd && \
        apt-get update -qq && \
        apt-get install -qq ${LINUXBREW_DEPENDENCIES} ${BUILD_DEPENDENCIES} && \
        echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER ${USER}
ENV USER ${USER}
WORKDIR /home/${USER}
