FROM docker:stable-dind

RUN apk add --no-cache curl git && \
 L=/usr/local/bin/flynn && curl -sSL -A "`uname -sp`" https://dl.flynn.io/cli | zcat >$L && chmod +x $L
