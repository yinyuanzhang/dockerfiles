FROM ubuntu:16.04
LABEL MAINTAINER Paulo Salgado <pjosalgado@gmail.com>

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV LANG en_US.UTF-8

RUN apt update \
    && apt purge openjdk* \
    && echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections \
    && echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" > /etc/apt/sources.list.d/webupd8team-java-trusty.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \
    && apt update \
    && apt install -y oracle-java8-installer oracle-java8-set-default locales \
    && locale-gen en_US.UTF-8 \
    && apt install -y fontconfig-config libfontconfig1 \
