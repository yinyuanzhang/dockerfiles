FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.1.2

RUN gem install gync --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["gync"]
CMD ["--help"]
