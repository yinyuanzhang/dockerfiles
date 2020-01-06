FROM alpine:latest

RUN \
    apk add --no-cache lynx newsboat vim \
    && addgroup -S newsboat \
    && adduser -S newsboat -D newsboat -G newsboat \
    && apk del --quiet --no-cache --purge \
    && mkdir -p /home/newsboat/.newsboat \
    && chown newsboat:newsboat -R /home/newsboat/.newsboat \
    && rm -rf /var/cache/apk/*

USER newsboat:newsboat
VOLUME /home/newsboat/.newsboat

CMD newsboat
