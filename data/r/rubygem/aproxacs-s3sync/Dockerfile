FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.3.6

RUN gem install aproxacs-s3sync --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["s3sync"]
CMD ["--help"]
