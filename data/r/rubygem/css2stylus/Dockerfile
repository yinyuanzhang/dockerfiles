FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.0.4

RUN gem install css2stylus --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["css2stylus"]
CMD ["--help"]
