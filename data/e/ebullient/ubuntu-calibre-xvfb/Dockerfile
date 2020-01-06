FROM ubuntu:xenial

LABEL maintainer="Erin Schnabel <schnabel@us.ibm.com> (@ebullientworks)"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
  && apt-get -qq upgrade -y \
  && apt-get install -y \
    build-essential \
     curl \
     libxcomposite1 \
     python2.7 \
     python-pip \
     python-pyqt5 \
     wget \
     x11-common \
     xvfb \
  && python2 -m pip install --upgrade pip \
  && curl -sL https://deb.nodesource.com/setup_8.x | /bin/bash - \
  && apt-get install -y nodejs \
  && apt-get -qq clean \
  && rm -rf /tmp/* /var/lib/apt/lists/* \
  && wget -q https://download.calibre-ebook.com/3.26.0/calibre-3.26.0-x86_64.txz \
  && mkdir /calibre-bin && tar xvf calibre-3.26.0-x86_64.txz -C /calibre-bin \
  && /calibre-bin/calibre_postinstall \
  && rm calibre-3.26.0-x86_64.txz
