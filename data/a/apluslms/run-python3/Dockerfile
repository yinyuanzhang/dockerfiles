FROM debian:stretch-slim

ENV LANG=C.UTF-8

RUN apt-get update -qqy && DEBIAN_FRONTEND=noninteractive apt-get install -qqy --no-install-recommends \
    -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \
    apt-utils \
    ca-certificates \
    build-essential \
    git \
    python \
    python3 \
    python3-dev \
    python3-pip \
    python3-certifi \
    python3-virtualenv \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
  && pip3 install --no-cache-dir --disable-pip-version-check \
    setuptools \
    wheel \
  && rm -rf /root/.cache

