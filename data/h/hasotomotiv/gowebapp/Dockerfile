FROM alpine:latest

MAINTAINER "Levent SAGIROGLU" <LSagiroglu@gmail.com>

VOLUME /srv

COPY srv /srv
COPY bin /bin

ENV APPNAME "gosrv"

EXPOSE 80
ENTRYPOINT ["/bin/entrypoint.sh"]
