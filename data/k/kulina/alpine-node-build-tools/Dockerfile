FROM kulina/alpine-node:latest
MAINTAINER Didiet Noor <dnoor@kulina.id> (@lynxluna)

ENV TERM=dumb \
    BUILD_DEPS="git tar curl python gcc g++ make binutils-gold linux-headers paxctl" \
    RUNTIME_DEPS="libgcc libstdc++"

RUN apk add --update ${BUILD_DEPS} ${RUNTIME_DEPS} && curl -L https://www.npmjs.org/install.sh | sh && \
    apk del ${BUILD_DEPS} && \
    rm -rf /tmp/* /var/cache/apk/*

