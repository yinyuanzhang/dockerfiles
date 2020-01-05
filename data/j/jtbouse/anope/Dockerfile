FROM alpine:latest AS builder

ARG VERSION=2.0.6
ARG RUN_DEPENDENCIES=""
ARG BUILD_DEPENDENCIES=""
ARG EXTRA_MODULES="extra/m_ssl_gnutls extra/m_mysql extra/m_sqlite"

WORKDIR /src

RUN apk upgrade --no-cache && \
    apk add --no-cache git gcc g++ make git cmake gnutls-dev sqlite-dev mariadb-dev $BUILD_DEPENDENCIES

RUN git clone https://github.com/anope/anope.git anope -b ${VERSION} && \
    cd anope && \
    for module in ${EXTRA_MODULES}; do ln -sf `pwd`/modules/$module.cpp modules/; done

RUN mkdir anope/build && \
    cd anope/build && \
    cmake  -DINSTDIR=/anope -DDEFUMASK=077 -DCMAKE_BUILD_TYPE=RELEASE .. && \
    make -j`getconf _NPROCESSORS_ONLN` install && \
    ln -sf /data/anope.db /anope/data/

COPY conf/ /anope/conf/


FROM alpine:latest

LABEL maintainer="Jeremy.Bouse@UnderGrid.net"

RUN adduser -D anope -s /bin/false anope && \
    apk upgrade --no-cache && \
    apk add --no-cache tini curl libgcc libstdc++ gnutls-utils sqlite-libs mariadb-connector-c $RUN_DEPENDENCIES

COPY --from=builder --chown=1000 /anope /anope

WORKDIR /anope

RUN mkdir -p /data && \
    touch /data/anope.db && \
    chown -R anope /data/

VOLUME /data

USER anope

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["/anope/bin/services", "-n"]
