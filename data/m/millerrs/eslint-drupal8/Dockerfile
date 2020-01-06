FROM node:alpine

ENV PKG eslint-config-airbnb

RUN apk add --no-cache \
    curl \
    && npm install -g eslint \
    	eslint-plugin-prettier \
    	eslint-config-prettier \
    	prettier \
    && npm info "$PKG@latest" peerDependencies --json \
    | command sed 's/[\{\},]//g ; s/: /@/g' \
    | xargs npm install -g "$PKG@latest"

ENV DRUPAL_VERSION 8.7

RUN curl --silent --show-error -o ~/.eslintrc.json "http://cgit.drupalcode.org/drupal/plain/core/.eslintrc.json?id=${DRUPAL_VERSION}.x"

WORKDIR /app

USER node

CMD ["eslint", "."]