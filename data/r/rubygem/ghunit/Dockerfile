FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.0.6

RUN gem install ghunit --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["ghunit"]
CMD ["--help"]
