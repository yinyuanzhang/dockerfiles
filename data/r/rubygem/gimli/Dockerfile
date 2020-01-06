FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.6.0.pre

RUN gem install gimli --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["gimli"]
CMD ["--help"]
