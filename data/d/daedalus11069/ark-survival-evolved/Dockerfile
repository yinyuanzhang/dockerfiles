# ----------------------------------
# Pterodactyl Core Dockerfile
# Environment: Source Engine
# Minimum Panel Version: 0.6.0
# ----------------------------------
FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
# Install Dependencies
RUN dpkg --add-architecture i386 \
    && apt-get upgrade -y \
    && apt-get update \
    && apt-get install -y tar zip unzip curl wget gcc g++ software-properties-common apt-transport-https expect gettext perl inotify-tools lib32gcc1 lib32tinfo5 lib32z1 lib32stdc++6 libtinfo5:i386 libncurses5:i386 libcurl3-gnutls:i386 iproute2 gdb libsdl1.2debian libfontconfig \
    && apt-get clean \
    && apt-get autoclean \
    && useradd -m -d /home/container container

USER container
ENV HOME /home/container
WORKDIR /home/container

COPY ./entrypoint.sh /entrypoint.sh
CMD ["/bin/bash", "/entrypoint.sh"]