FROM node:8.1-alpine

# Install updates & dependencies
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
 && apk update && apk upgrade \
 && apk add git python make g++ wget tar curl gzip \
 && wget -P /yarn --quiet https://yarnpkg.com/latest.tar.gz; tar zxf /yarn/latest.tar.gz -C /yarn; rm /yarn/latest.tar.gz \
 && rm -rf /var/cache/apk/*

# Set path to yarn
ENV PATH /yarn/dist/bin:$PATH
