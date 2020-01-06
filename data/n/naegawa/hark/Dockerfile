FROM ubuntu:18.04
MAINTAINER Kojima <kojima.ryosuke.8e@kyoto-u.ac.jp>
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y wget bzip2 curl git lsb-release gnupg sudo
RUN mkdir -p ~/usr/hark
WORKDIR /usr/hark

RUN echo "deb http://archive.hark.jp/harkrepos $(lsb_release -cs) non-free\ndeb-src http://archive.hark.jp/harkrepos $(lsb_release -cs) non-free" > /etc/apt/sources.list.d/hark.list
RUN wget -q -O - http://archive.hark.jp/harkrepos/public.gpg | apt-key add -
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update && \
    apt-get install -y nodejs hark-base harkmw hark-core hark-designer harktool5 harktool5-gui kaldidecoder-hark python3-pip nginx
ADD default /etc/nginx/sites-available/default
ADD setup.sh /usr/hark/setup.sh
ENTRYPOINT bash /usr/hark/setup.sh && tail -f /dev/null
