FROM python:3.6.6-alpine3.8

RUN set -xe \
    && apk add --update --no-cache \
    ca-certificates \
    curl \
    iperf \
    bash \
    openssh-client \
    libmemcached-libs \
    libevent \
    libssl1.0 \
    musl \
    yaml \
    make \
    musl-dev \
    python3-dev \
    gcc \
    g++ \
    m4 \
    libmemcached-dev \
    zlib-dev \
    mariadb-connector-c-dev \
    linux-headers \
    libffi-dev \
    snappy-dev \
    libc-dev; \
    apk add --no-cache --repository "http://dl-cdn.alpinelinux.org/alpine/edge/testing" --allow-untrusted py3-pymysql; \
    pip3 install python-snappy; \
    pip3 install pymysql; \
    pip3 install kafka; \
    pip3 install pylibmc; \
    pip3 install configparser; \
    pip3 install flask ;\
    pip3 install connexion[swagger-ui]; \
    pip3 install python-jose; \
    apk del libmemcached-dev zlib-dev mariadb-connector-c-dev gcc linux-headers libc-dev g++


COPY configcreate.sh /configcreate.sh
COPY scripts /usr/local/bin
COPY api /usr/local/api

EXPOSE 9126 5000
ENTRYPOINT ["/configcreate.sh"]
