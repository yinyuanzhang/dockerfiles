FROM alpine:3.3
MAINTAINER "EEA: IDM2 A-Team" <eea-edw-a-team-alerts@googlegroups.com>

ENV JSLINT_VERSION=1.4.4

RUN apk add --no-cache --virtual .run-deps openjdk7-jre git \
 && mkdir -p /code

COPY jslint4java-$JSLINT_VERSION.jar /jslint4java.jar
COPY docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["jslint"]
