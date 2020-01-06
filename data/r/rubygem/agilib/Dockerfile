FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.1.9

RUN gem install agilib --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["agilib"]
CMD ["--help"]
