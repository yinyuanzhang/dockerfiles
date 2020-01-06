FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.0.3

RUN gem install atc-tools --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["fpv"]
CMD ["--help"]
