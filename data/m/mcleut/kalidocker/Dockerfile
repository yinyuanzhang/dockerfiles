FROM kalilinux/kali-linux-docker:latest
MAINTAINER Christopher Leuthardt <mail@christopher-leuthardt.de>

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm-256color

RUN rm -rf /etc/apt/sources.list*
RUN echo "deb http://http.kali.org/kali kali-bleeding-edge main non-free contrib" >> /etc/apt/sources.list && \
    echo "deb-src http://http.kali.org/kali kali-bleeding-edge main non-free contrib" >> /etc/apt/sources.list && \
    echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list

RUN apt update -q -y && apt dist-upgrade -q -y && apt autoremove -q -y && apt clean all && \
    apt install -y kali-linux-all && apt clean all && \
    apt update -y && apt dist-upgrade -y && apt autoremove -y && apt clean all && \
    apt install cron

RUN echo "0  2    * * *   root    apt update -q -y && apt dist-upgrade -q -y && apt autoremove -q -y && apt clean all" >> /etc/crontab
RUN update-rc.d cron defaults && \
    /etc/init.d/cron restart
