FROM ubuntu:16.04

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get dist-upgrade -y \
    && apt-get install -y \
      aptitude \
      curl \
      dnsutils \
      dsniff \
      git \
      htop \
      iputils-ping \
      links \
      locales \
      lynx \
      mc \
      mtr \
      nano \
      net-tools \
      openssl \
      pwgen \
      python-pip \
      python-setuptools \
      python-software-properties \
      rsync \
      software-properties-common \
      strace \
      tcpdump \
      tcpflow \
      telnet \
      traceroute \
      unzip \
      wget \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && echo "en_US UTF-8" >/etc/locale.gen \
    && echo "en_US.UTF-8 UTF-8" >>/etc/locale.gen \
    && locale-gen

COPY etc /etc

ENV TZ=UTC LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8
