FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.1.3.3

RUN gem install aml --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["aml"]
CMD ["--help"]
