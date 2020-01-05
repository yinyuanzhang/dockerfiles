FROM node:5
MAINTAINER Alessio Caiazza <nolith@abisso.org>

ENV DEBIAN_FRONTEND noninteractive

ENV MIX_ENV prod
ENV LC_ALL C.UTF-8
ENV GOSU_VERSION 1.2
ENV ERLANG_VERSION 1.0


RUN apt-get update &&\
  apt-get install wget ca-certificates -y --no-install-recommends &&\
  gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 &&\
  wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture)" &&\
  wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture).asc" &&\
  gpg --verify /usr/local/bin/gosu.asc && rm /usr/local/bin/gosu.asc &&\
  chmod +x /usr/local/bin/gosu &&\
  wget https://packages.erlang-solutions.com/erlang-solutions_${ERLANG_VERSION}_all.deb &&\
  dpkg -i erlang-solutions_${ERLANG_VERSION}_all.deb &&\
  rm erlang-solutions_${ERLANG_VERSION}_all.deb &&\
  apt-get update &&\
  apt-get install -y esl-erlang elixir --no-install-recommends &&\
  rm -rf /var/lib/apt/lists/*

CMD iex
