FROM linuxserver/deluge

LABEL maintainer="si0972"

RUN \
  sed -i -- 's/#deb-src/deb-src/g' /etc/apt/sources.list && sed -i -- 's/# deb-src/deb-src/g' /etc/apt/sources.list && \
    #Installing packages
  apt-get update && \
  apt-get install -y \
  ffmpeg \
  git \
  python-pip \
  openssl \
  python-dev \
  libffi-dev \
  libssl-dev \
  libxml2-dev \
  libxslt1-dev \
  zlib1g-dev \
  libfdk-aac-dev \
  build-essential  && \
    #installing PythonPackages
  pip install --upgrade pip==9.0.3 && \
  pip install requests \
  requests[security] \
  requests-cache \
  babelfish \
  'guessit<2' \
  'subliminal<2' \
  stevedore==1.19.1 \
  python-dateutil \
  qtfaststart && \
    #Cleanup
  rm -rf \
  /tmp/* \
  /var/lib/apt/lists/* \
  /var/tmp/*
COPY /root /

VOLUME /SickBeard