FROM debian:wheezy
MAINTAINER Matthieu Keromen <sharoomsorg@gmail.com>
ENV REFRESHED_AT 2015-05-25

ENV TIMEZONE America/Montreal

RUN apt-get update && apt-get install -y \
    git \
    curl && \
    curl -sL https://deb.nodesource.com/setup | bash - && \
    apt-get install -y nodejs && \
    npm install --global gulp && \
    echo $TIMEZONE > /etc/timezone && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    rm -rf /var/lib/apt/lists/*

ENV WORKSPACE /var/www
ENV TASKS default
ENV USER root
ENV MODULES event-stream

ADD ./init.sh /init.sh
RUN chmod 0755 /init.sh

ENTRYPOINT ["/init.sh"]
