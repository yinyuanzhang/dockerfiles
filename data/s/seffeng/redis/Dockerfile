FROM seffeng/alpine:latest

MAINTAINER  seffeng "seffeng@sina.cn"

ARG BASE_DIR="/opt/websrv"

ENV REDIS_VERSION=redis-5.0.7\
 CONFIG_DIR="${BASE_DIR}/config/redis"\
 INSTALL_DIR="${BASE_DIR}/program/redis"\
 BASE_PACKAGE="gcc g++ make linux-headers tzdata coreutils musl-dev lua-turbo"

ENV REDIS_URL="http://download.redis.io/releases/${REDIS_VERSION}.tar.gz"

WORKDIR /tmp
COPY    conf ./conf

RUN apk update && apk add --no-cache ${BASE_PACKAGE} &&\
 wget ${REDIS_URL} &&\
 tar -zxf ${REDIS_VERSION}.tar.gz &&\
 mkdir -p ${BASE_DIR}/logs ${BASE_DIR}/tmp ${CONFIG_DIR} ${INSTALL_DIR} ${BASE_DIR}/data/redis &&\
 rm -rf ${INSTALL_DIR} &&\
 cd ${REDIS_VERSION} &&\
 make &&\
 make install &&\
 cp -Rf /tmp/conf/* ${CONFIG_DIR} &&\
 mv src ${INSTALL_DIR} &&\
 rm -rf /usr/local/bin/redis-* &&\
 ln -s ${INSTALL_DIR}/redis-benchmark /usr/local/bin/redis-benchmark &&\
 ln -s ${INSTALL_DIR}/redis-check-aof /usr/local/bin/redis-check-aof &&\
 ln -s ${INSTALL_DIR}/redis-check-rdb /usr/local/bin/redis-check-rdb &&\
 ln -s ${INSTALL_DIR}/redis-cli /usr/local/bin/redis-cli &&\
 ln -s ${INSTALL_DIR}/redis-sentinel /usr/local/bin/redis-sentinel &&\
 ln -s ${INSTALL_DIR}/redis-server /usr/local/bin/redis-server &&\
 echo -e "#/bin/sh/\n${INSTALL_DIR}/redis-server ${CONFIG_DIR}/redis.conf" > ${CONFIG_DIR}/start.sh &&\
 echo -e "#/bin/sh/\nredis-cli shutdown > /dev/null" > ${CONFIG_DIR}/stop.sh &&\
 chmod +x ${CONFIG_DIR}/start.sh ${CONFIG_DIR}/stop.sh &&\
 apk del ${BASE_PACKAGE} &&\
 rm -rf /var/cache/apk/* &&\
 rm -rf /tmp/*

VOLUME ["${BASE_DIR}/tmp", "${BASE_DIR}/data/redis"]

EXPOSE 6379

CMD ["redis-server", "/opt/websrv/config/redis/redis.conf"]