FROM ubuntu:16.04

MAINTAINER Szabolcs Hegedus <szabolcs.hegedus@gmail.com>

RUN dpkg --add-architecture i386

RUN apt-get update && apt-get install --no-install-recommends --yes \
    mc \
    htop \
    nload \
    fail2ban \
    nano \
    curl\
    wget\
    file\
    bzip2\
    gzip\
    unzip\
    bsdmainutils\
    python\
    util-linux\
    ca-certificates\
    binutils\
    bc\
    tmux\
    lib32gcc1\
    libstdc++6\
    libstdc++6:i386\
    libstdc++5:i386\
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/share/doc/* \
    && rm -rf /var/cache/debconf/*


RUN useradd -ms /bin/bash cod4server
RUN echo "cod4server:cod2server" | chpasswd
WORKDIR /home/cod4server
RUN su - cod4server
RUN wget https://linuxgsm.sh
RUN mv index.html linuxgsm.sh && chmod +x linuxgsm.sh
RUN su cod4server  /home/cod4server/linuxgsm.sh cod4server
RUN su cod4server -s /bin/bash -c " echo -e '\nY\nY\n' | /home/cod4server/cod4server install"
RUN chown -R cod4server:cod4server /home/*

EXPOSE 28960:28960/udp
