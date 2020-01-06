# Use an official Ubuntu 16.04 as a parent image
# pstp/owamp_bwctl-syslog.conf 
# pstp/supervisor.conf
FROM ubuntu:16.04

# required to assume-yes for debconf
ARG DEBIAN_FRONTEND=noninteractive


RUN \
    apt-get update && \
    apt-get install -y apt-utils locales

ENV LC_ALL en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8

ENV HOME /root

RUN \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 && \
    apt-get install -y supervisor curl less rsyslog netcat-openbsd bind9-host net-tools iproute2 traceroute

# perfSONAR
RUN \
    curl -fsSL http://downloads.perfsonar.net/debian/perfsonar-release.list --output /etc/apt/sources.list.d/perfsonar-jessie-release.list && \
    curl -fsSL http://downloads.perfsonar.net/debian/perfsonar-debian-official.gpg.key | apt-key add - && \
    apt-get update ; apt-get install -y perfsonar-testpoint 

COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY owamp_bwctl-syslog.conf /etc/rsyslog.d/owamp_bwctl-syslog.conf

WORKDIR /var/log
CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf