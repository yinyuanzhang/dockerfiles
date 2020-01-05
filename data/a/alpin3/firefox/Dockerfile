FROM alpine:latest
MAINTAINER kost - https://github.com/kost

RUN apk --update add dbus ttf-dejavu firefox-esr && rm -f /var/cache/apk/* && \
 mkdir -p /work && adduser -D -s /bin/sh user user && chown -R user /work && \
 echo "Success"

USER user

WORKDIR /work

ENTRYPOINT ["firefox"]
