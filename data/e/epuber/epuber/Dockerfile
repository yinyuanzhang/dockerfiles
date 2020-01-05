FROM ruby:2.5-alpine
LABEL maintainer="roman@kriz.io"

ENV EPUBER_VERSION="0.5.7"

RUN apk --no-cache add imagemagick6 nodejs zip && \
    apk --no-cache add --virtual .build-deps g++ musl-dev make imagemagick6-dev && \
    gem update --system && \
    gem install epuber --version $EPUBER_VERSION && \
    apk del .build-deps
