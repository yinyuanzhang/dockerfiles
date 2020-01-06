FROM ubuntu:16.04
LABEL maintainer="JohnTheBoss"

LABEL build_version="SiteDeploy with Node.js: 8x - build: 15"

# Update System #
RUN \
    echo "**** update system ****" && \
    apt-get update && \
    apt-get full-upgrade -y

# Update and Install #
RUN \
    echo "**** install packages ****" && \
    apt-get update && \
    apt-get install -y \
    git \
    lftp \
    curl \
    wget \
    build-essential \
    autoconf \
    automake \
    libtool \
    nasm \
    make \
    pkg-config \
    libpng-dev \
    rsync 

# Node.JS Install #
RUN \
    echo "**** Download && Install Node.js  ****" && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs && \
    echo "**** Node.js Verson: ****" && \
    node -v && \
    echo "**** Update NPM  ****" && \
    npm -g install npm && \
    echo "**** NPM Version:  ****" && \
    npm --version

CMD ["/bin/bash"]