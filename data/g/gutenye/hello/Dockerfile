FROM lsiobase/alpine.armhf:3.8

ARG FLOOD_VER=master

COPY qemu-arm-static /usr/bin/

RUN apk add --no-cache nodejs npm
#RUN apk add --no-cache --virtual=build-dependencies g++ argon2 gcc make git linux-headers python
RUN apk add --no-cache --virtual=build-dependencies alpine-sdk python2 argon2 
# python2
# RUN gcc -v
RUN npm install pdjs --loglevel silly
RUN npm install node-gyp --loglevel silly


# RUN mkdir /tmp/argon2 wget -qO- https://github.com/jfurrow/flood/archive/${FLOOD_VER}.tar.gz | tar xz --strip 1 \

#RUN git clone --recurse-submodules --depth 1 git@github.com:ranisalt/node-argon2.git /tmp/argon2 
#RUN mkdir /tmp/argon2 && cd /tmp/argon2 && wget -qO- https://github.com/ranisalt/node-argon2/archive/master.tar.gz | tar xz --strip 1
#RUN gcc -v && \
#  cd /tmp/argon2 && \
#  npm install && \
#  node-gyp rebuild --verbose

# node-gyp:  make gcc g++ python 
# simple: alpine-sdk python


