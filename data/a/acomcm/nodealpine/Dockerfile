FROM mhart/alpine-node:6
MAINTAINER Ivan <ivan.petrus@acommerce.asia>

RUN apk add --no-cache git build-base python fontconfig

RUN echo Node 6.9.2 && \
    npm install -g bower gulp phantomjs-prebuilt eslint node-gyp && \
    npm cache clean && \
    bower --allow-root cache clean

WORKDIR /app
