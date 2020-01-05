FROM alpine:latest

LABEL maintainer="Saimir Balleshi saimir.balleshi@gmail.com"

ENV REDIS_VERSION=5.0.3
ENV TWEMPROXY_DIR=0.4.1
ENV TWEMPROXY_VERSION=v${TWEMPROXY_DIR}


EXPOSE 5001
EXPOSE 5002

RUN apk update && apk add ca-certificates \
  && rm -rf /var/cache/apk/* /tmp/* \
  && apk add wget nano
RUN apk add --update bash alpine-sdk autoconf automake libtool \
  && rm -rf /var/cache/apk/* /tmp/*
RUN wget https://github.com/twitter/twemproxy/archive/${TWEMPROXY_VERSION}.tar.gz \
	&& tar -xzf ${TWEMPROXY_VERSION}.tar.gz
RUN cd twemproxy-${TWEMPROXY_DIR} && autoreconf -fvi && ./configure --enable-debug=log && make && mv src/nutcracker /usr/local/bin/nutcracker
RUN cd / && rm -rf twemproxy-${TWEMPROXY_DIR} && rm -rf ${TWEMPROXY_VERSION}.tar.gz
COPY ./nutcracker.yml /etc/twemproxy/nutcracker.yml

ENV REDIS_VERSION=5.0.3
ENV GOSU_VERSION=1.11

RUN set -exo pipefail \
  && apk add --no-cache --virtual .build-deps \
    build-base \
    linux-headers \
    openssl \
  && wget -O /usr/local/bin/gosu https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64 \
  && chmod +x /usr/local/bin/gosu \
  && cd /tmp \
  && wget https://github.com/antirez/redis/archive/${REDIS_VERSION}.tar.gz \
  && tar xzf ${REDIS_VERSION}.tar.gz \
  && cd /tmp/redis-${REDIS_VERSION} \
  && make \
  && make install \
  && cp redis.conf /etc/redis.conf \
  && cp redis.conf /etc/redis2.conf \
  && cp redis.conf /etc/redis3.conf \
  && cp redis.conf /etc/redis4.conf \
  && sed -i -e 's/bind 127.0.0.1/bind 0.0.0.0/' /etc/redis.conf \
  && sed -i -e 's/bind 127.0.0.1/bind 0.0.0.0/' /etc/redis2.conf \
  && sed -i -e 's/bind 127.0.0.1/bind 0.0.0.0/' /etc/redis3.conf \
  && sed -i -e 's/bind 127.0.0.1/bind 0.0.0.0/' /etc/redis4.conf \
  && sed -i -e 's/pidfile \/var\/run\/redis_6379.pid/pidfile \/var\/run\/redis.pid/' /etc/redis.conf \
  && sed -i -e 's/pidfile \/var\/run\/redis_6379.pid/pidfile \/var\/run\/redis2.pid/' /etc/redis2.conf \
  && sed -i -e 's/pidfile \/var\/run\/redis_6379.pid/pidfile \/var\/run\/redis3.pid/' /etc/redis3.conf \
  && sed -i -e 's/pidfile \/var\/run\/redis_6379.pid/pidfile \/var\/run\/redis4.pid/' /etc/redis4.conf \
  && sed -i -e 's/dir .\//dir \/var\/lib\/redis/' /etc/redis.conf \
  && sed -i -e 's/dir .\//dir \/var\/lib\/redis2/' /etc/redis2.conf \
  && sed -i -e 's/dir .\//dir \/var\/lib\/redis3/' /etc/redis3.conf \
  && sed -i -e 's/dir .\//dir \/var\/lib\/redis4/' /etc/redis4.conf \
  && sed -i -e 's/logfile ""/logfile \/var\/log\/redis\/redis.log/' /etc/redis.conf \
  && sed -i -e 's/logfile ""/logfile \/var\/log\/redis\/redis2.log/' /etc/redis2.conf \
  && sed -i -e 's/logfile ""/logfile \/var\/log\/redis\/redis3.log/' /etc/redis3.conf \
  && sed -i -e 's/logfile ""/logfile \/var\/log\/redis\/redis4.log/' /etc/redis4.conf \
  && sed -i -e 's/\# replicaof <masterip> <masterport>/replicaof 0.0.0.0 6379/' /etc/redis2.conf \
  && sed -i -e 's/\# replicaof <masterip> <masterport>/replicaof 0.0.0.0 6379/' /etc/redis3.conf \
  && sed -i -e 's/\# replicaof <masterip> <masterport>/replicaof 0.0.0.0 6379/' /etc/redis4.conf \
  && mkdir -p /var/lib/redis \
  && mkdir -p /var/lib/redis2 \
  && mkdir -p /var/lib/redis3 \
  && mkdir -p /var/lib/redis4 \
  && mkdir -p /var/log/redis \
  && chmod +x /var/log/redis \
  && adduser -D redis \
  && apk del .build-deps \
  && rm -rf /tmp/* \
  && chown -R redis.redis /var/lib/redis \
  && chown -R redis.redis /var/lib/redis2 \
  && chown -R redis.redis /var/lib/redis3 \
  && chown -R redis.redis /var/lib/redis4 \
  && chown -R redis.root /etc/redis.conf \
  && chown -R redis.root /etc/redis2.conf \
  && chown -R redis.root /etc/redis3.conf \
  && chown -R redis.root /etc/redis4.conf
 
RUN sed -i -e 's/port 6379/port 6380/g' /etc/redis2.conf \
  && sed -i -e 's/port 6379/port 6381/g' /etc/redis3.conf \
  && sed -i -e 's/port 6379/port 6382/g' /etc/redis4.conf

COPY ./entrypoint.sh /home/entrypoint.sh
RUN chmod +x /home/entrypoint.sh


CMD /home/entrypoint.sh && /bin/bash