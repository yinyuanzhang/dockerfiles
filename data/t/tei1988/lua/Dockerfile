FROM alpine:3.9

ENV LUA_VERSION 5.2.4

RUN apk --no-cache add \
      lua5.2 \
      ca-certificates && \
    ln -s /usr/bin/lua5.2 /usr/bin/lua && \
    ln -s /usr/bin/luac5.2 /usr/bin/luac && \
    addgroup lua && \
    adduser -S -G lua lua && \
    mkdir /lua && \
    chown lua. /lua
USER lua
WORKDIR /lua
