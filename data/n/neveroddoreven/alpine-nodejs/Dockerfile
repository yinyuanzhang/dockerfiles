FROM node:8.9-alpine

RUN apk update && apk add --no-cache make git zip bash curl fontconfig
RUN npm install jspm -g
RUN npm install gulp-cli -g
RUN npm install gulp -D
RUN npm install -g bower

# Install Phantom JS for Alpine
#   The only thing that you should install is 'fontconfig' for configuration that comes with Phantom JS.
RUN cd /usr/share \
    && curl -L https://github.com/Overbryd/docker-phantomjs-alpine/releases/download/2.11/phantomjs-alpine-x86_64.tar.bz2 | tar xj \
    && ln -s /usr/share/phantomjs/phantomjs /usr/bin/phantomjs \
    && phantomjs --version

# Set location of phantomjs
ENV PHANTOMJS_BIN /usr/bin/phantomjs
