FROM python:3.6.1

LABEL maintainer="Castalia Developers <developers@castalia.co.jp>"

# install mysql client
# デフォルトだと mysql-client-5.5 がインストールされるため 5.7 にする
ENV MYSQL_MAJOR_VERSION 5.7
ENV MYSQL_APT_CONFIG_PACKAGE mysql-apt-config_0.8.10-1_all.deb
RUN \
  apt-get update && apt-get install lsb-release && \
  wget https://dev.mysql.com/get/${MYSQL_APT_CONFIG_PACKAGE} && \
  echo mysql-apt-config	mysql-apt-config/select-server	select	mysql-${MYSQL_MAJOR_VERSION} | debconf-set-selections && \
  DEBIAN_FRONTEND=noninteractive dpkg -i ${MYSQL_APT_CONFIG_PACKAGE} && \
  apt-get update && \
  apt-get install -y mysql-client

RUN pip install --upgrade pip
RUN pip install wheel

ENV ANSIBLE_VERSION 2.6.3
RUN pip install ansible==${ANSIBLE_VERSION}

ENTRYPOINT /bin/bash
