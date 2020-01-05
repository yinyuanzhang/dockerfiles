FROM ubuntu

MAINTAINER Jimmy Zöger <jimmy.zoger@erlang-solutions.com>

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update && apt-get install -y wget

WORKDIR /tmp

RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && \
    dpkg -i erlang-solutions_1.0_all.deb

RUN apt-get update && apt-get install -y erlang            \
                                         erlang-base-hipe  \
                                         build-essential   \
                                         rebar
