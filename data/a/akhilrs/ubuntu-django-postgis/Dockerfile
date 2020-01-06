FROM ubuntu:16.04
MAINTAINER Akhil R S "https://akhil.rs"
# make sure the package repository is up to date and update ubuntu
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get -y install locales && \
  locale-gen en_US.UTF-8
RUN apt-get install -y curl git htop man software-properties-common \
    unzip vim wget python-pip libpq-dev python-dev libjpeg-dev supervisor \
    pgbouncer libxslt1-dev libxml2-dev postgis xvfb
RUN add-apt-repository ppa:ubuntugis/ubuntugis-unstable -y
RUN apt-get update

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV HOME /root

RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN tar xvJf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN cp wkhtmltox/bin/wkhtmlto* /usr/bin/
