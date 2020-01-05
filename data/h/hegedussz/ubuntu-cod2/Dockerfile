FROM ubuntu:18.04

MAINTAINER Szabolcs Hegedus <szabolcs.hegedus@gmail.com>

RUN dpkg --add-architecture i386

RUN apt-get update && apt-get install --no-install-recommends --yes \
    mc \
    htop \
    nload \
    fail2ban \
    nano \
    curl \
    wget \
    file \
    bzip2 \
    gzip \
    unzip \ 
    tzdata \
    mailutils \
    file \
    tar \
    bsdmainutils \
    python \
    util-linux \
    ca-certificates \
    binutils \
    bc \
    jq \
    tmux \
    lib32gcc1 \
    libstdc++6 \
    libstdc++6:i386 \
    libstdc++5:i386 \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/share/doc/* \
    && rm -rf /var/cache/debconf/*

RUN ln -snf /usr/share/zoneinfo/Europe/Budapest /etc/localtime && echo Europe/Budapest > /etc/timezone
RUN useradd -ms /bin/bash cod2server
RUN echo "cod2server:cod2server" | chpasswd
WORKDIR /home/cod2server
RUN su - cod2server
RUN wget -O linuxgsm.sh https://linuxgsm.sh 
RUN chmod +x linuxgsm.sh
RUN su cod2server  /home/cod2server/linuxgsm.sh cod2server
RUN su cod2server -s /bin/bash -c " echo -e '\nY\nY\n' | /home/cod2server/cod2server install"
COPY docker/ /
RUN chown -R cod2server:cod2server /home/*

EXPOSE 28960:28960/udp
