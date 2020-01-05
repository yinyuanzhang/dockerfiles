FROM tomcraftmc/log4cplus:latest
EXPOSE 67/udp
RUN apk update && \
    apk add procps alpine-sdk git autoconf automake openssl openssl-dev boost-dev libtool pkgconfig && \
    cd /tmp && \
    git clone https://gitlab.isc.org/isc-projects/kea.git && \
    cd kea && \
    autoreconf --install && \
    ./configure && \
    make && \
    make install && \
    cd / && \
    rm -rf /tmp/* && \
    apk del alpine-sdk git autoconf automake pkgconfig && \
    rm -rf /var/cache/apk/*
