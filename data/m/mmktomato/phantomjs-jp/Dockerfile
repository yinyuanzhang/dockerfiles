FROM debian:latest

ENV PAHNTOMJS_VERSION 2.1.1

RUN apt-get update \
    && apt-get install -y \
           curl \
           bzip2 \
           libfontconfig \
           locales \
           fonts-vlgothic \

    && curl -L -O https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PAHNTOMJS_VERSION}-linux-x86_64.tar.bz2 \
    && tar xvf phantomjs-${PAHNTOMJS_VERSION}-linux-x86_64.tar.bz2 \
    && ln -s $(pwd)/phantomjs-${PAHNTOMJS_VERSION}-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs \

    && echo "ja_JP.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen \

    && rm -rf phantomjs-${PAHNTOMJS_VERSION}-linux-x86_64.tar.bz2 \
    && apt-get purge -y curl bzip2 \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV LANG ja_JP.UTF-8

