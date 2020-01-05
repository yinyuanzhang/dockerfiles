FROM ubuntu:latest

MAINTAINER Therosin


ENV DEBIAN_FRONTEND=noninteractive
ADD rootfs /
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y dos2unix libcompress-raw-zlib-perl wget tar curl gcc g++ lib32gcc1 lib32tinfo5 lib32z1 lib32stdc++6 libtinfo5:i386 libncurses5:i386 libcurl3-gnutls:i386 && \
    apt-get install -y perl-modules lsof libc6-i386 bzip2 && \
    apt-get install -y ca-certificates && \
    apt-get install -y software-properties-common && \
    apt-get install -y debconf-utils && \
    add-apt-repository multiverse -y && \
    apt-get update -y
RUN apt-get install sudo
RUN useradd -d /home/container -m container
RUN adduser container sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN groupadd -r steam && \
  useradd \
    -r -d /home/steam -g steam steam && \
  apt-get \
    update && \
  apt-get install -y \
    lib32gcc1 && \
  apt-get \
    clean && \
  mkdir -p \
    /home/steam && \
  curl \
    http://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz \
    | tar -C /home/steam -xzf - && \
  chown -R steam:steam \
    /home/steam && \
  steamcmd \
    +login anonymous +quit && \
  rm -f \
    /home/steam/Steam/logs/*

RUN curl -sL http://git.io/vtf5N | bash -s container && \
    chown container:container /etc/arkmanager -R && \
    mkdir -p /var/log/arktools && \
    chown container:container /var/log/arktools -R 
USER container
ENV  USER container
ENV  HOME /home/container

WORKDIR /home/container

COPY ./entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]
