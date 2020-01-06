FROM debian:7

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update
RUN apt-get -y install \
  git \
  curl \
  wget \
  unzip \
  tar \
  vim \
  sudo

ENV GOVERSION 1.7.2
ADD https://storage.googleapis.com/golang/go${GOVERSION}.linux-amd64.tar.gz /tmp/go${GOVERSION}.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf /tmp/go${GOVERSION}.linux-amd64.tar.gz \
  && rm /tmp/go${GOVERSION}.linux-amd64.tar.gz
ENV PATH $PATH:/usr/local/go/bin
