FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.0.8

RUN gem install jasmine_webos --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["jasmine_webos"]
CMD ["--help"]
