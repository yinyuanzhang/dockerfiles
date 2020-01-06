FROM debian:wheezy
MAINTAINER apribase

# apt
ADD etc/apt/sources.list     /etc/apt/sources.list
ADD etc/apt/apt.conf.d/local /etc/apt/apt.conf.d/local
RUN apt-get update
ENV DEBIAN_FRONTEND noninteractive

# wget
RUN apt-get install -y apt-transport-https wget ca-certificates

# locale
RUN apt-get install -y locales
ADD etc/locale.gen     /etc/locale.gen
ADD etc/default/locale /etc/default/locale
RUN /usr/sbin/locale-gen && /usr/sbin/update-locale
ENV LANG ja_JP.UTF-8

# timezone
ADD etc/timezone /etc/timezone
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# clean
RUN apt-get clean
