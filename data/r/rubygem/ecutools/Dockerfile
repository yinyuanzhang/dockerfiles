FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.0.4

RUN gem install ecutools --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["ecutools"]
CMD ["--help"]
