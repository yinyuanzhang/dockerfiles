FROM debian:wheezy
MAINTAINER Matthieu Keromen <sharoomsorg@gmail.com>
ENV REFRESHED_AT 2015-05-25

RUN apt-get update && apt-get install -y \
    git \
    curl

RUN curl -sL https://deb.nodesource.com/setup | bash - && \
    apt-get install -y nodejs && \
    npm install -g bower && \
    mkdir -p /usr/local/bin/bower && \
    rm -rf /var/lib/apt/lists/*

ENV WORKSPACE /var/www
ENV USER root

ADD ./init.sh /init.sh
RUN chmod 0755 /init.sh

ENTRYPOINT ["/init.sh"]
