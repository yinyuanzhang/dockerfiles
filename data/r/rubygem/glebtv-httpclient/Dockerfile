FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=3.2.8

RUN gem install glebtv-httpclient --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["httpclient"]
CMD ["--help"]
