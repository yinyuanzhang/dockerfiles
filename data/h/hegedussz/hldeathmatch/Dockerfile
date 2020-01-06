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
    jq \
    lib32gcc1\
    libstdc++6\
    libstdc++6:i386\
    libstdc++5:i386\
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/share/doc/* \
    && rm -rf /var/cache/debconf/*


RUN useradd -ms /bin/bash hldmserver 
RUN echo "hldmserver:hldmserver" | chpasswd
WORKDIR /home/hldmserver
RUN su - hldmserver
RUN wget -O linuxgsm.sh https://linuxgsm.sh && chmod +x linuxgsm.sh
RUN su hldmserver  /home/hldmserver/linuxgsm.sh hldmserver
RUN su hldmserver -s /bin/bash -c " echo -e '\nY\nY\n' | /home/hldmserver/hldmserver install"
RUN chown -R hldmserver:hldmserver /home/hldmserver

EXPOSE 27005:27005/udp
EXPOSE 27005:27005/tcp
EXPOSE 27015:27015/tcp
EXPOSE 27015:27015/udp

