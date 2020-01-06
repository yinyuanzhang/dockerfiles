FROM debian:jessie
MAINTAINER Jérémy Bethmont <jeremy.bethmont@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Install netcat
RUN rm -rf /var/lib/apt/lists/* && \
  apt-get update -q && apt-get install -qy --no-install-recommends \
  netcat-openbsd \
  && rm -rf /var/lib/apt/lists/*
