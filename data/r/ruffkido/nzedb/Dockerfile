FROM linuxserver/nginx

MAINTAINER ruffkido <ruffkido@gmail.com>

RUN \
  apk add --no-cache --upgrade \
# Install Prereq Software
    curl \
    git \
    man \
    unzip \
    wget \
    htop \
    mariadb-mytop \
    bwm-ng \
    vnstat \
    tmux \
    mediainfo \
    ffmpeg \
    unrar \
    lame \
    p7zip \
    composer \
    build-base \
  && \
# Build and install yydecode
    cd /tmp && \
    mkdir -p yydecode && \
    cd yydecode && \
    wget http://downloads.sourceforge.net/project/yydecode/yydecode/0.2.10/yydecode-0.2.10.tar.gz && \
    tar xf yydecode-0.2.10.tar.gz && \
    cd yydecode-0.2.10 && \
    ./configure && \
    make && \
    make install && \
    apk del build-base \
  && \
# Install and setup nZEDb
    git clone https://github.com/nZEDb/nZEDb.git /app/nZEDb && \
    cd /app/nZEDb && \
    composer install --prefer-source \
  && \
# Cleanup when done
  rm -rf /tmp/* /var/tmp/*

COPY root/ /

EXPOSE 8080 9000