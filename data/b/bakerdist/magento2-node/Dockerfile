FROM node:12-alpine

ENV NODE_ENV=production

RUN addgroup -S magento -g 82 \
    && adduser -S -G magento -u 82 magento \
    && apk add --no-cache \
        g++ \
        gcc \
        make \
        python2


USER magento