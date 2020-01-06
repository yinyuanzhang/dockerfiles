#FROM alpine:3.9
FROM ruby:2-alpine

LABEL maintainer="Sebastian Vilstrup <sev@tiatechnology.com>"

ENV MARKDOWN_VERSION=0.5.0

RUN apk add --no-cache ruby git && \
  gem install -v $MARKDOWN_VERSION mdl && \
  mkdir /data

WORKDIR /data

ENTRYPOINT ["mdl"]
CMD ["--help"]
