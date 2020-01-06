FROM dezinger/ubuntu-14:latest

MAINTAINER dezinger@gmail.com

ENV DEBIAN_FRONTEND noninteractive
ENV MEMCACHED_USER=memcache

COPY files/ /

RUN \ 
# add our user and group first to make sure their IDs get assigned consistently, 
# regardless of whatever dependencies get added
    groupadd -r $MEMCACHED_USER && useradd -r -g $MEMCACHED_USER $MEMCACHED_USER && \
# install
    apt-get -y update && \
    apt-get install --no-install-recommends -y memcached && \
# clean
    apt-get -y autoremove && apt-get -y clean && apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 11211