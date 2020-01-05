FROM ubuntu:14.04
MAINTAINER Shota Kawabuchi <shota.kawabuchi+github@gmail.com>

RUN set -x && \
  apt-get update && \
  apt-get install --no-install-recommends -y \
    gfortran=4:4.8.2-1ubuntu6 \
    libatlas-dev=3.10.1-4 \
    libatlas-base-dev=3.10.1-4 \
    eatmydata=26-2 \
    cython3-dbg=0.20.1+git90-g0e6e38e-1ubuntu2 \
    python3-dbg=3.4.0-0ubuntu2 \
    python3-dev=3.4.0-0ubuntu2 \
    python3-nose=1.3.1-2 \
    python3-setuptools=3.3-1ubuntu2 \
    git=1:1.9.1-1ubuntu0.3 \
    build-essential=11.6ubuntu6 \
    vim=2:7.4.052-1ubuntu3 && \
  apt-get clean && \
  easy_install3 pip==8.1.2 && \
  pip install \
    ipython==5.1.0 \
    asv==0.1.1 && \
  ln -s /usr/bin/python3 /usr/bin/python

RUN mkdir /workspace
VOLUME /workspace

