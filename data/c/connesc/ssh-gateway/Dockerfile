FROM alpine:3.8

LABEL maintainer="https://github.com/connesc"

RUN apk add --no-cache openssh

RUN sed -i 's/^\(root:.*:\)[^:]\+$/\1\/sbin\/nologin/' /etc/passwd

COPY entrypoint.sh /usr/local/bin/

EXPOSE 22

VOLUME /config

ENTRYPOINT ["entrypoint.sh"]
