FROM keymetrics/pm2:10-alpine

RUN apk --update add --no-cache bash \
  && rm -rf /var/cache/apk/*

RUN npm i -g -s -f @adonisjs/cli yarn

ENV PYPY_VERSION 7.1.1
ENV PYPY_SHA256SUM 6a3ef876e3691a54f4cff045028ec3be94ab9beb2e99f051b83175302c1899a8

RUN set -ex; \
    wget -O pypy.tar.bz2 "https://bitbucket.org/pypy/pypy/downloads/pypy3.6-v${PYPY_VERSION}-src.tar.bz2"; \
    echo "$PYPY_SHA256SUM *pypy.tar.bz2" | sha256sum -c -; \
    mkdir -p /usr/src/pypy; \
    tar -xjC /usr/src/pypy --strip-components=1 -f pypy.tar.bz2; \
    rm pypy.tar.bz2
