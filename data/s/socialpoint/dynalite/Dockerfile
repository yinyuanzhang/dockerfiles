FROM node:8.2-alpine

LABEL maintainer "Backend Team <backend@socialpoint.es>"

ENV DYNALITE_VERSION=2.1.0
RUN apk add --no-cache --virtual .gyp \
        python \
        make \
        g++ \
    && npm --unsafe-perm install \
        -g dynalite@${DYNALITE_VERSION} \
    && npm --force cache clear \
    && rm -rf /tmp/* /var/tmp/* \
    && apk del .gyp

RUN mkdir -p /var/dynamodb

EXPOSE 8000
VOLUME /var/dynamodb

CMD ["dynalite", "--port=8000", "--createTableMs=10", "--deleteTableMs=10", "--updateTableMs=10", "--path=/var/dynamodb"]
