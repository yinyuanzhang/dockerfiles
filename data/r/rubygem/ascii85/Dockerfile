FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.0.2

RUN gem install Ascii85 --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["ascii85"]
CMD ["--help"]
