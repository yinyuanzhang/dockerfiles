FROM alpine:3.6

LABEL maintainer "itiQiti SAS <opensource@itiqiti.com>"

ENV MODE=default

RUN ln -sf /dev/stdout /var/log/messages && \
    apk add --update --no-cache --virtual .build-deps curl && \
    curl -s -f -L https://github.com/itiqiti/dkconf/releases/download/0.2/dkconf-linux -o /usr/local/bin/dkconf && \
    chmod +x /usr/local/bin/dkconf && \
    apk del .build-deps && \
    apk add --no-cache rsyslog=8.26.0-r0

COPY ["templates", "/usr/local/etc/rsyslog/templates"]
COPY ["docker-entrypoint.sh", "/usr/local/bin/"]

VOLUME "/var/run/rsyslog"

CMD  ["/usr/local/bin/docker-entrypoint.sh"]

