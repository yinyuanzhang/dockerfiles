FROM alpine
MAINTAINER ErAzOr2k

ENV COMMAND="sync"
ENV OPTIONS="--verbose"
ENV CRONJOB="0 * * * *"
ENV SOURCE=
ENV TARGET=

VOLUME ["/config"]

RUN apk --no-cache add \
    alpine-sdk \
    ca-certificates \
    fuse \
    git \
    go \
  && go get -u -v github.com/ncw/rclone \
  && cp /root/go/bin/rclone /usr/bin/ \
  && apk del \
    alpine-sdk \
    git \
    go \
  && rm -rf \
    /root/go/ \
    /tmp/* \
    /var/cache/apk/* \
    /var/lib/apk/lists/*

COPY start.sh /
COPY rclone.sh /
RUN chmod +x /start.sh
RUN chmod +x /rclone.sh

CMD ["/start.sh"]
