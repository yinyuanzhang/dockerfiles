FROM ruby:alpine

RUN apk --update add --virtual build_deps \
    build-base \
    libc-dev \
    linux-headers \
    cmake \
    && apk --no-cache add icu-dev \
    && gem install github-linguist \
    && apk del build_deps

CMD ["linguist"]