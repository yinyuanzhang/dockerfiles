FROM node:10-alpine

ARG NPM_TOKEN=f22a1c0a-fb11-41cd-8fa5-95ed198ff99d

WORKDIR /var/www

COPY package*.json /var/www/

RUN apk update && \
    apk add --no-cache --virtual .build-deps git make g++ python && \
    echo "//registry.npmjs.org/:_authToken=${NPM_TOKEN}" > .npmrc && \
    npm ci --only=production && \
    apk del .build-deps

COPY ./ /var/www/

CMD ["node","--max-old-space-size=1600","index.js"]

