FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.0.2.3

RUN gem install adhearsion-cw --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["ahn"]
CMD ["--help"]
