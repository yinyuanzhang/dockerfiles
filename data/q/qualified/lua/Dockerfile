FROM alpine:3.8

RUN set -ex; \
    adduser -D codewarrior; \
    ln -s /home/codewarrior /workspace;

RUN set -ex; \
    apk add --no-cache lua5.3 lua5.3-busted; \
    ln -s /usr/bin/lua5.3 /usr/bin/lua; \
    ln -s /usr/bin/busted-5.3 /usr/bin/busted;

WORKDIR /workspace

COPY rootfs/opt/runner /opt/runner

USER codewarrior
ENV USER=codewarrior \
    HOME=/home/codewarrior
