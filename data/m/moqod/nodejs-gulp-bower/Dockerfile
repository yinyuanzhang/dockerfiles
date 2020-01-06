FROM monostream/nodejs-gulp-bower

MAINTAINER Artyom Nosov <chip@unixstyle.ru>

RUN apk add --quiet --no-cache make g++ python && \
    yarn cache clean && \
    rm -rf /var/cache/* /tmp/*
