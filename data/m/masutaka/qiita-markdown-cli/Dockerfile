FROM ruby:2.5-alpine
LABEL maintainer "masutaka.net@gmail.com"

ENV BUILD_DEPENDENCIES="build-base cmake icu-dev libressl-dev"

RUN apk add --update --no-cache ${BUILD_DEPENDENCIES} icu-libs libressl python && \
    gem install -N qiita-markdown-cli && \
    apk del --purge ${BUILD_DEPENDENCIES}

ENTRYPOINT ["qmc"]
