ARG NODE_VERSION=lts-alpine
FROM node:${NODE_VERSION}

RUN echo @edge http://nl.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories \
    && echo @edge http://nl.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories \
    && apk --no-cache update \
    && apk --no-cache add \
    libstdc++@edge \
    chromium@edge \
    nss@edge \
    freetype@edge \
    harfbuzz@edge \
    ttf-freefont@edge \
    && rm -rf /var/cache/apk/* /tmp/*

ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROME_PATH=/usr/lib/chromium/
