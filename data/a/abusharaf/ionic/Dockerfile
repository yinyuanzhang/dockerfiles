FROM alpine:3.8

LABEL maintainer="Mohammad Sharaf Hijjeh sharaf.hijjeh@outlook.com"

ENV IONIC_VERSION 4.5.0
ENV CORDOVA_VERSION 8.0.0

RUN apk upgrade && apk update \
    && apk add --no-cache npm \
    && npm i -g --unsafe-perm cordova@${CORDOVA_VERSION} \
    && npm i -g --unsafe-perm ionic@${IONIC_VERSION} \
    && npm i -g --unsafe-perm git


EXPOSE 8100 8200

STOPSIGNAL SIGTERM

CMD ["node"]
