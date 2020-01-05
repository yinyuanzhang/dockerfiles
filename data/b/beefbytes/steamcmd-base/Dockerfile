FROM ubuntu:16.04
LABEL maintainer="contact@beefbytes.com"

RUN apt-get update
RUN apt-get -y install 
RUN apt-get update && apt-get install --no-install-recommends -y \
    ca-certificates \
    lib32gcc1 \
    net-tools \
    lib32stdc++6 \
    lib32z1 \
    lib32z1-dev \
    curl \
    wget \
    vim \
    bzip2 \
    mono-complete \
    lib32tinfo5

RUN mkdir -p /home/steam/steamcmd/ \
    && useradd -ms /bin/bash steam \
    && chown -R steam /home/steam \
    && chmod -R 744 /home/steam

USER steam

WORKDIR /home/steam/steamcmd/
RUN wget http://media.steampowered.com/client/steamcmd_linux.tar.gz \
    && tar -xvzf steamcmd_linux.tar.gz \
    && ./steamcmd.sh +login anonymous +quit

RUN mkdir -p ~/.steam/sdk32/ \
    && ln -s /home/steam/steamcmd/linux32/steamclient.so ~/.steam/sdk32/steamclient.so
