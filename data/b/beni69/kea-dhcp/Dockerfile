#FROM alpine:latest as builder
#FROM alpine:latest
FROM alpine:3.7

ARG KEA_DHCP_VERSION=1.7.0
ARG LOG4_CPLUS_VERSION=2.0.2

RUN apk add --no-cache --virtual .build-deps \
        alpine-sdk \
        bash \
        boost-dev \
        bzip2-dev \
        file \
        libressl-dev \
        mariadb-dev \
        mariadb \
        mariadb-client \
        mariadb-client-libs \
        libc6-compat \
        pwgen \
        zlib-dev && \
    cd /tmp && \
    curl -sL https://sourceforge.net/projects/log4cplus/files/log4cplus-stable/${LOG4_CPLUS_VERSION}/log4cplus-${LOG4_CPLUS_VERSION}.tar.gz | tar -zx -C /tmp && \
    cd /tmp/log4cplus* && \
    ./configure && \
#    make -s -j$(nproc) && \
    make && \
    make install && \
    curl -sL https://ftp.isc.org/isc/kea/${KEA_DHCP_VERSION}/kea-${KEA_DHCP_VERSION}.tar.gz | tar -zx -C /tmp && \
    cd /tmp/kea-${KEA_DHCP_VERSION} && \
    ./configure \
        --enable-shell \
        --with-mysql=/usr/bin/mysql_config && \
#    make -s -j$(nproc) && \
    make && \
    make install-strip && \
#    make install && \
#    apk del --purge .build-deps && \
    rm -rf /tmp/*

#FROM alpine:3.7
#LABEL maintainer "beni <beni.removeme@alkel.com>"

#RUN apk --no-cache add \
#        bash \
#        boost \
#        bzip2 \
#        libressl \
#        mariadb-client-libs \
#        zlib

#COPY --from=builder /usr/local /usr/local/
COPY docker_entry.sh docker_entry.sh
RUN  chmod +x docker_entry.sh

RUN  mkdir -p /var/log/supervisord /usr/local/etc/supervisord
COPY supervisord/supervisord.conf /usr/local/etc/supervisord/supervisord.conf
COPY supervisord/supervisord supervisord
RUN  chmod +x supervisord

#ENTRYPOINT ["/supervisord"]
#CMD ["-c", "/usr/local/etc/supervisord/supervisord.conf"]
CMD ./docker_entry.sh
