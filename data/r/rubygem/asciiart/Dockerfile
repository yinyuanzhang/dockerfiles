FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.0.9

RUN gem install asciiart --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["asciiart"]
CMD ["--help"]
