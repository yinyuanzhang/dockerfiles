FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.0.2

RUN gem install css2less --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["css2less"]
CMD ["--help"]
