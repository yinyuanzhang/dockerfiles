FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.6

RUN gem install cowl --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["cowl"]
CMD ["--help"]
