FROM parrotsec/parrot:latest
MAINTAINER Christopher Leuthardt <mail@christopher-leuthardt.de>

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm-256color

RUN rm -rf /etc/apt/sources.list.d/*
RUN echo "deb https://ftp.halifax.rwth-aachen.de/parrotsec/ parrot main contrib non-free" >> /etc/apt/sources.list.d/parrot.list && \
    echo "deb-src https://ftp.halifax.rwth-aachen.de/parrotsec/ parrot main contrib non-free" >> /etc/apt/sources.list.d/parrot.list

RUN apt update -q -y && apt dist-upgrade -q -y && apt autoremove -q -y && apt clean all && \
    apt install -y cron

RUN echo "0  2    * * *   root    apt update -q -y && apt dist-upgrade -q -y && apt autoremove -q -y && apt clean all" >> /etc/crontab && \
    update-rc.d cron defaults
RUN /etc/init.d/cron restart
