FROM ubuntu:18.04

LABEL maintainer="Lexin Gong <gonglexin@gmail.com>"

WORKDIR /opt/build

# Use aliyun source in China
COPY docker/aliyun.sources.list /etc/apt/sources.list

RUN \
  apt-get update -y && \
  apt-get install -y \
    git\
    gnupg \
    libsctp1 \
    libwxbase3.0-dev \
    libwxgtk3.0-dev \
    locales \
    wget && \
  sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
  locale-gen && \
  rm -rf /var/lib/apt/lists/*

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash"]
