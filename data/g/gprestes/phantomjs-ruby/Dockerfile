FROM ruby:2.7.0

MAINTAINER Guilherme Heuser Prestes <guilherme.prestes@gmail.com>

RUN apt-get -qq update && apt-get -qqy install \
    build-essential \
    chrpath \
    libssl-dev \
    libxft-dev \
    libfreetype6-dev \
    libfreetype6 \
    libfontconfig1-dev \
    libfontconfig1 && rm -rf /var/lib/apt/lists/*
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/
RUN ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/
