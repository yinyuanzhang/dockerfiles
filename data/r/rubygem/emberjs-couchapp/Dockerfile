FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.0.7

RUN gem install emberjs-couchapp --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["emberjs-couchapp"]
CMD ["--help"]
