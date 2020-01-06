FROM alpine:3.8
MAINTAINER Sebastian Schneider <mail@sesc.eu>

RUN apk --no-cache add bash minidlna tini

VOLUME ["/var/lib/minidlna"]

COPY entrypoint.sh /
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]
