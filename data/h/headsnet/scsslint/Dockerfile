FROM ruby:2.5-alpine3.7

RUN apk --no-cache add \
    build-base && \
    gem install scss_lint && \
    apk del build-base

VOLUME ["/app"]

WORKDIR /app

ENTRYPOINT ["scss-lint"]
