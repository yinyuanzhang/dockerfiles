FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive 

RUN sed -i 's/archive.ubuntu.com/au.archive.ubuntu.com/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/au.archive.ubuntu.com/g' /etc/apt/sources.list
RUN dpkg --add-architecture i386 && apt-get update && apt-get upgrade -y
RUN apt-get install -y \
    neovim \
    mailutils postfix curl wget file bzip2 gzip unzip bsdmainutils python util-linux ca-certificates binutils bc jq tmux lib32gcc1 libstdc++6 libstdc++6:i386 telnet expect

RUN wget https://linuxgsm.com/dl/linuxgsm.sh -O /usr/local/bin/linuxgsm.sh && chmod 755 /usr/local/bin/linuxgsm.sh

RUN adduser --uid 1337 --group --system --shell /bin/bash user 
USER user
WORKDIR /home/user
VOLUME /home/user
