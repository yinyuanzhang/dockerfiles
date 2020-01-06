FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.1.3

RUN gem install adhd --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["adhd"]
CMD ["--help"]
