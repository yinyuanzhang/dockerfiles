FROM node:11-alpine
MAINTAINER Daniel Caiafa <dcaiafa [at] gmail.com>

RUN addgroup kinesalite && adduser -H -D -G kinesalite kinesalite

RUN apk add --update g++ make python \
    && npm install -g --unsafe-perm --build-from-source kinesalite@1.14.0 \
    && apk --purge -v del g++ make python \
    && rm -rf /var/cache/apk/*

USER kinesalite

EXPOSE 4567
ENTRYPOINT ["kinesalite"]
