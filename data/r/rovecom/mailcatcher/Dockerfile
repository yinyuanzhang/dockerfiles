FROM ruby:2.4-alpine3.6

MAINTAINER Dennis de Vaal <ddevaal@rovecom.nl>

RUN set -xe \
    && apk add --no-cache \
        libstdc++ \
        sqlite-libs \
    && apk add --no-cache --virtual .build-deps \
        build-base \
        sqlite-dev \
    && gem install mailcatcher -v 0.7.0.beta1 --no-ri --no-rdoc \
    && apk del .build-deps

EXPOSE 1025
EXPOSE 1080

CMD ["mailcatcher", "--foreground", "--ip=0.0.0.0", "--http-path=/mail"]