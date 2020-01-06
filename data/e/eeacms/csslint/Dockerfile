FROM alpine:3.3
MAINTAINER "EEA: IDM2 A-Team" <eea-edw-a-team-alerts@googlegroups.com>

ENV CSSLINT_VERSION=1.0.5

RUN apk add --no-cache --virtual .run-deps nodejs git \
 && npm install -g csslint@$CSSLINT_VERSION \
 && mkdir -p /code

COPY docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["csslint"]
