FROM lsiobase/alpine:amd64-32234c97-ls2

# Package version
ARG ROON-EXTENSION-HARMONY_VER="2018-10-18"

WORKDIR /app

RUN apk add --no-cache \
            nodejs \
            nodejs-npm

# Add local files
COPY rootfs/ /

WORKDIR /app

RUN apk add --no-cache --virtual=build-dependencies \
            tar \
            git \
 && apk add --no-cache \
            curl \
 && curl -L https://github.com/docbobo/roon-extension-harmony/archive/master.tar.gz | tar xz --strip-components=1 -C /app \
 && npm install \

# Cleanup
 && apk del --purge build-dependencies \
 && rm -rf /tmp/* \
           /root/.npm
