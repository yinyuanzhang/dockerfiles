FROM node:8-alpine
LABEL Author="Kristoffer Andersen <ka@ptype.dk>"

COPY . /goaccServer
WORKDIR /goaccServer

ARG build_deps="git build-base ncurses-dev autoconf automake git gettext-dev"
ARG runtime_deps="tini ncurses libintl gettext "
ARG repo="https://github.com/allinurl/goaccess.git"
EXPOSE 8080

RUN apk update && \
    apk add -u $runtime_deps $build_deps

RUN git clone $repo goaccess && cd goaccess && pwd && \
    autoreconf -fiv && \
    ./configure --enable-utf8 && \
    make && \
    make install && \
    apk del $build_deps && \
    rm -rf /var/cache/apk/* /tmp/goaccess/* /goaccess && \
    cd ..

RUN pwd && ls && npm install
CMD npm run serve