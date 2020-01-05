FROM ubuntu:latest
MAINTAINER Christopher Leuthardt <mail@christopher-leuthardt.de>

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm-256color

RUN rm -rf /etc/apt/sources.*
RUN echo "deb http://de.archive.ubuntu.com/ubuntu/ cosmic main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://de.archive.ubuntu.com/ubuntu/ cosmic main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://security.ubuntu.com/ubuntu cosmic-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://security.ubuntu.com/ubuntu cosmic-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://de.archive.ubuntu.com/ubuntu/ cosmic-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://de.archive.ubuntu.com/ubuntu/ cosmic-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://de.archive.ubuntu.com/ubuntu/ cosmic-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://de.archive.ubuntu.com/ubuntu/ cosmic-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://archive.canonical.com/ubuntu cosmic partner" >> /etc/apt/sources.list && \
    echo "deb-src http://archive.canonical.com/ubuntu cosmic partner" >> /etc/apt/sources.list
RUN apt update -q -y && apt dist-upgrade -q -y && apt autoremove -q -y && apt clean all && \
    apt install -y wget cron tzdata

RUN echo "0  2    * * *   root    apt update -q -y && apt dist-upgrade -q -y && apt autoremove -q -y && apt clean all" >> /etc/crontab
RUN update-rc.d cron defaults && \
    /etc/init.d/cron restart

RUN ln -fs /usr/share/Europe/Berlin /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata

RUN cd /tmp && \
    wget https://christopher-leuthardt.de/files/Nessus-8.0.1-ubuntu1110_amd64.deb && \
    dpkg -i /tmp/Nessus-8.0.1-ubuntu1110_amd64.deb
RUN /etc/init.d/nessusd start && \
    update-rc.d nessusd defaults
