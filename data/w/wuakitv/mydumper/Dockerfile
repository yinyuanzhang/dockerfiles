FROM debian:jessie
MAINTAINER Carles Amigó, carles.amigo@rakuten.com

ENV MYDUMPER_VERSION=0.9.1
ENV MYDUMPER_MAJOR_VERSION=0.9

RUN apt-get update && apt-get install -y \
      build-essential \
      cmake \
      curl \
      libglib2.0-0 \
      libglib2.0-dev \
      libmysqlclient-dev \
      libmysqlclient18 \
      libpcre3-dev \
      libssl-dev \
      zlib1g-dev \
      && \
    mkdir -p /src/mydumper && \
    cd /src/mydumper && \
    curl -L https://launchpad.net/mydumper/${MYDUMPER_MAJOR_VERSION}/${MYDUMPER_VERSION}/+download/mydumper-${MYDUMPER_VERSION}.tar.gz | tar xvz --strip=1 && \
    cmake -DBUILD_DOCS=OFF -DCMAKE_INSTALL_PREFIX=/usr . && \
    make && \
    strip mydumper myloader && \
    make install && \
    cd / && \
    rm -rf /src && \
    apt-get purge --auto-remove -y \
      build-essential \
      cmake \
      curl \
      libglib2.0-dev \
      libmysqlclient-dev \
      libpcre3-dev \
      libssl-dev \
      zlib1g-dev \
      && \
    rm -rf /usr/share/doc/* && \
    rm -rf /usr/share/info/* && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/*

RUN mkdir -p /mydumper
WORKDIR /mydumper
