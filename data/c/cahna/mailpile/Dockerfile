
FROM debian:jessie
MAINTAINER Conor Heine <conor.heine@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV export LANGUAGE=en_US.UTF-8
ENV export LC_ALL=en_US.UTF-8
ENV export LANG=en_US.UTF-8
ENV export LC_TYPE=en_US.UTF-8

RUN apt-get update
RUN apt-get -y install git python-dev libxml2-dev libxslt-dev libz-dev python-pip
RUN git clone --recursive https://github.com/mailpile/Mailpile.git /mailpile

WORKDIR /mailpile

RUN pip install -r requirements.txt
RUN ./mp setup

EXPOSE 33411
CMD ./mp --www=0.0.0.0:33411 --wait

VOLUME /root/.local/share/Mailpile
VOLUME /root/.gnupg

