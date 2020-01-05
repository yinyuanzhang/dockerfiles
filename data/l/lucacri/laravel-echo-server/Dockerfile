FROM lucacri/alpine-base:latest
LABEL maintainer="lucacri@gmail.com"

ARG CACHEBUST=20191028

ARG UID=501
ARG GID=501

### Install Laravel Echo Server and dependencies
RUN apk upgrade --update-cache && \
    apk add curl ca-certificates && \
    echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    echo "@edge http://nl.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && \
    apk update && \
    apk add sqlite openssl \
    nano \
    nodejs \
    npm \
    bash \
    && apk add --virtual .build-deps \
    binutils-gold \
    curl \
    g++ \
    gcc \
    gnupg \
    libgcc \
    linux-headers \
    make \
    python \
    yarn && \
    /usr/bin/yarn global add --prod --no-lockfile laravel-echo-server \
    && /usr/bin/yarn cache clean \
    && apk del .build-deps \
    && rm -rf /var/cache/apk/*

COPY root/ /

ENV LARAVEL_ECHO_AUTH_HOST=http://localhost
ENV LARAVEL_ECHO_SERVER_DB=redis
ENV LARAVEL_ECHO_REDIS_HOST=redis
ENV LARAVEL_ECHO_REDIS_PORT=6379
ENV LARAVEL_ECHO_SERVER_DEBUG="false"
ENV LARAVEL_ECHO_REDIS_DB_BACKEND=0
ENV LARAVEL_ECHO_SERVER_PORT=6001

WORKDIR /app
VOLUME /app

EXPOSE 6001