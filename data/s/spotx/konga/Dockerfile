FROM node:6.12.3-alpine 

COPY . /app

WORKDIR /app

RUN apk upgrade --update \
    && apk add bash git ca-certificates \
    && npm install -g bower \
    && npm --unsafe-perm --production install \
    && apk del git \
    && rm -rf /var/cache/apk/* \
        /app/.git \
        /app/screenshots \
        /app/test

EXPOSE 1337

RUN chgrp -R 0 /app && chmod -R g+wrx /app

ENTRYPOINT ["/app/start.sh"]
