FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.1.2

RUN gem install comedy --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["comedy"]
CMD ["--help"]
