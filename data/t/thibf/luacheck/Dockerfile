FROM registry.hub.docker.com/library/alpine:edge

RUN \
    apk add --no-cache \
        dumb-init \
        luacheck \
    && \
    rm -rf "/var/cache/apk/"* 
