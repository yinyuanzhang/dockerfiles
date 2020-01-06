FROM ubuntu:xenial

MAINTAINER Emre <e@emre.pm>

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /tmp

RUN \
  apt-get update && \
  apt-get install -y automake bzip2 cmake make g++ gcc git openssl libssl-dev patch && \
  git clone https://github.com/sysown/proxysql.git && \
  cd proxysql && \
  make && \
  apt-get remove -y automake cmake make g++ gcc patch && \
  apt-get autoclean -y && \
  apt-get autoremove -y && \
  cp src/proxysql /usr/bin/proxysql && \
  rm -rf /tmp/* /var/lib/apt/lists/*

ENTRYPOINT ["proxysql", "-f", "-c", "/etc/proxysql.cnf", "--reload"]