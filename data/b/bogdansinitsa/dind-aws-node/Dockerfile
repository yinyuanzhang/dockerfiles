FROM docker:latest

ENV BUILD_DEPS="gettext"  \
    RUNTIME_DEPS="libintl"

RUN set -x && \
    apk add --update $RUNTIME_DEPS && \
    apk add --virtual build_deps $BUILD_DEPS &&  \
    cp /usr/bin/envsubst /usr/local/bin/envsubst && \
    apk del build_deps

RUN apk add --no-cache --update python py-pip;
RUN pip install awscli

RUN apk add --update nodejs nodejs-npm
RUN apk add --update zip
RUN apk add --update curl

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.9/main' >> /etc/apk/repositories
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.9/community' >> /etc/apk/repositories
RUN apk update
# mongodb installation throws an error, but seems to work, so ignoring the exit status.
RUN apk add mongodb=4.0.5-r0 || true
# this is required by mongodb-memory-server to avoid trying to download the mongod file.
ENV MONGOMS_SYSTEM_BINARY=/usr/bin/mongod
