#
# Dockerfile for oho-reader
#

FROM mhart/alpine-node

WORKDIR /etc/git

RUN set -ex \
    && apk --update add --no-cache git \
    && git clone -b master --single-branch https://github.com/enowsh/oho-reader.git \
    && sed -i '/^app.listen(/{s/3001/PORT/}' /etc/git/oho-reader/dist/app.js \
    && cd oho-reader \
    && npm install \
    && npm run dist \
    && apk del git \
    && rm -rf /var/cache/apk

COPY docker-entrypoint.sh /entrypoint.sh

ENV PORT  3001

EXPOSE $PORT/tcp

ENTRYPOINT ["/entrypoint.sh"]

WORKDIR /etc/git/oho-reader/dist

CMD ["node", "app.js"]