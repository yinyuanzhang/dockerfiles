FROM buildpack-deps:stretch
MAINTAINER Olivier Tabone <olivier.tabone@ripplemotion.fr>

ENV C_INCLUDE_PATH /usr/include/gdal/
ENV CPLUS_INCLUDE_PATH /usr/include/gdal/
ENV PATH "/root/.pyenv/bin:${PATH}"
ENV ENV="/etc/profile"

RUN set -x \
    && apt-get update \
    && apt-get upgrade -y \
    && (curl -sL https://deb.nodesource.com/setup_10.x | bash) \
    && apt-get install -y \
        libgdal-dev \
        swig \
        postgresql-client \
        protobuf-compiler \
        libprotoc-dev \
        locales \
        osmosis \
        libgeoip-dev geoip-database-extra \
        nodejs \
        netcat \
    && (curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash)  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && (cd /usr/bin && ( [ -e node ] || ln -s nodejs node )) \
    && npm install -g yarn

RUN pyenv install 2.7.15
RUN pyenv install 2.7.16
RUN pyenv install 3.5.6
RUN pyenv install 3.6.6
RUN pyenv install 3.6.8
RUN pyenv install 3.7.0
RUN pyenv global 3.7.0 3.6.8 3.5.6 2.7.16

# RUN set -x && (echo '#!/bin/bash' > /etc/profile.d/pyenv.sh 2>&1)
RUN set -x && (echo 'export PATH="/root/.pyenv/bin:$PATH"' >> /etc/bash.bashrc 2>&1)
RUN set -x && (echo 'eval "$(pyenv init -)"' >> /etc/bash.bashrc 2>&1)
RUN set -x && /root/.pyenv/shims/pip2.7 install --upgrade pip virtualenv setuptools wheel tox
RUN set -x && /root/.pyenv/shims/pip3.5 install --upgrade pip virtualenv setuptools wheel tox
RUN set -x && /root/.pyenv/shims/pip3.6 install --upgrade pip virtualenv setuptools wheel tox
RUN set -x && /root/.pyenv/shims/pip3.7 install --upgrade pip virtualenv setuptools wheel tox

RUN set -x \
    && mkdir -p ~/.ssh \
    && ssh-keyscan -t rsa bitbucket.org > ~/.ssh/known_hosts \
    && chmod 644 ~/.ssh/known_hosts

RUN set -x \
    && apt-get update \
    && apt-get install -y curl libxrender1 libfontconfig libxtst6 libglu1 subversion git build-essential libx11-dev libxi-dev libsndfile1-dev libopenexr-dev libjpeg-dev libopenal-dev libalut-dev libglu1-mesa-dev libsdl-dev libfreetype6-dev libavdevice-dev libavformat-dev libavutil-dev libavcodec-dev libswscale-dev libx264-dev libmp3lame-dev libspnav-dev \
    && curl "https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.79/blender-2.79b-linux-glibc219-x86_64.tar.bz2" -L -o "blender.tar.bz2" \
    && tar xjf blender.tar.bz2 \
    && mkdir -p /usr/local/ripple/ \
    && mv blender-2.79b-linux-glibc219-x86_64 /usr/local/ripple/blender \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
