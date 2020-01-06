FROM openjdk:8-jre-alpine

RUN apk add --no-cache --update \
	linux-headers \
	python \
	curl

## Import crontab file
COPY default_crontabs /var/spool/cron/crontabs/root

## Add, make exec, run "init" on start
ADD init /init
RUN chmod 755  /init

## Volume for configuration files
VOLUME /config


CMD ["/init"]
