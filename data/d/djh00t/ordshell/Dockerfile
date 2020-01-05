FROM alpine:latest
MAINTAINER David Hooton <david.hooton@ordnance.co>
LABEL version="20180923"
LABEL name="ordshell"
RUN echo "@testing http://mirror.aarnet.edu.au/pub/alpine/edge/testing" >> /etc/apk/repositories
RUN apk --update --no-cache add \
  openssh-client \
  bind-tools \
  netcat-openbsd \
  net-tools \
  nmap \
  curl \
  tcpdump \
  htop \
  mtr \
  iotop \
  iftop \
  iputils \
  speedtest-cli py-setuptools \
  bash \
  bash-completion \
  dstat@testing
