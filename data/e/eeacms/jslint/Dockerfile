FROM alpine:3.3
MAINTAINER "EEA: IDM2 A-Team" <eea-edw-a-team-alerts@googlegroups.com>

ENV JSLINT_VERSION=0.9.6

RUN apk add --no-cache --virtual .run-deps nodejs \
 && npm install -g jslint@$JSLINT_VERSION

ENTRYPOINT ["jslint"]
CMD ["/code/**/*.js"]
