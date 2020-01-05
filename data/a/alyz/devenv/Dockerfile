#
# Dockerfile for alyz/workenv
#

# Pull base image.
FROM alyz/devenv:stretch

# Install.
RUN \
    apt-get update \
    && apt-get -y dist-upgrade \
    && echo "Done"

RUN \
    apt-get install -y pypy \
    && apt-get install -y python-dev \
    && apt-get install -y python-memcache python3-memcache \
    && apt-get install -y python-pexpect python3-pexpect \
    && apt-get install -y python-docutils python3-docutils \
    && apt-get install -y python-netifaces python3-netifaces \
    && apt-get install -y python-dnspython python3-dnspython \
    && apt-get install -y python-cheetah \
    && apt-get install -y python-lxml python3-lxml \
    && apt-get install -y python-pastescript python-flup python-xmpp

RUN \
    apt-get install -y gnupg telnet imagemagick memcached \
    && apt-get install -y host whois less screen netcat socat \
    && apt-get install -y gcc g++ gfortran make mercurial git subversion cvs ccrypt \
    && apt-get install -y opensp w3c-sgml-lib \
    && apt-get install -y swig libxml2-utils

RUN apt-get install -y python-pip python3-pip python-virtualenv python3-virtualenv

RUN apt-get install -y libblas-dev liblapack-dev

# setup locales
RUN apt-get install -y locales \
    && echo "en_US ISO-8859-1" > /etc/locale.gen \
    && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && /usr/sbin/locale-gen

RUN apt-get install -y openssh-server \
    && mkdir -p /var/run/sshd
