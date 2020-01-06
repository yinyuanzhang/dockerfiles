FROM ubuntu:18.04
LABEL description="Cryptocurrency CPU Miner" \
      maintainer="Djerfy <djerfy@gmail.com>"

RUN apt-get update && \
    apt-get -y install git automake build-essential libcurl4-openssl-dev libncurses5-dev pkg-config yasm

RUN cd /opt && \
    git clone https://github.com/pooler/cpuminer.git

WORKDIR /opt/cpuminer

RUN set -xe && \
    ./autogen.sh && \
    CFLAGS="-march=native" ./configure && \
    make && \
    make install
