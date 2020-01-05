FROM debian:stretch-slim

ENV DEBIAN_FRONTEND noninteractive

# update and upgrade os
RUN \
  apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    less \
  && apt-get clean && apt-get autoremove && rm -Rf /var/lib/apt/lists/* && rm -Rf /var/cache/apt
