FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.4

RUN gem install dokku_client --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["dokku"]
CMD ["--help"]
