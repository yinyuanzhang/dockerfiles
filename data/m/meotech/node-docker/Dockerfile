####################################
# NodeJS from Source on Alpine Linux
####################################

# base
FROM alpine:3.2

# maintainer
MAINTAINER Marcus Schuh <mschuh@meo-tech.de>

# change to /tmp
WORKDIR /tmp

# environment
ENV NODE_VER v4.2.4
ENV NODE_DIR node-${NODE_VER}

# install essentials
RUN apk --update add wget build-base python linux-headers binutils-gold

# NodeJS source
RUN wget --no-check-certificate https://nodejs.org/dist/${NODE_VER}/${NODE_DIR}.tar.gz && \
	tar -zxvf ${NODE_DIR}.tar.gz && \
	cd ${NODE_DIR} && \
	./configure --without-snapshot && \
	make && \
	make install && \
    rm -rf /tmp/${NODE_DIR} && \
    rm -rf /var/cache/apk/* && \
    mkdir /app 

WORKDIR /app

VOLUME /app

EXPOSE 3000
