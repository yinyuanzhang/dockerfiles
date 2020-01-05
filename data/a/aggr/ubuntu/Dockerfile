FROM ubuntu:trusty
MAINTAINER Mikhail Baykov <mike@baikov.com>

RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \
 && echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \
 && apt-get -qq update \
 && DEBIAN_FRONTEND=noninteractive apt-get -qqy upgrade && apt-get -qqy install locales wget sudo net-tools ca-certificates unzip mc \
 && rm -rf /var/lib/apt/lists/* \
 && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8
