FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=3.1.3

RUN gem install heel --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["heel"]
CMD ["--help"]
