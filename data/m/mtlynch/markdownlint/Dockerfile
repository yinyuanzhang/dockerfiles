FROM ruby:2.6.5-alpine

MAINTAINER Mark Harrison <mark@mivok.net>

RUN apk add --no-cache ruby --version 2.6.5 && \
    gem install mdl --version 0.8.0 && \
    mkdir /data

WORKDIR /data

ENTRYPOINT ["mdl"]
CMD ["--help"]
