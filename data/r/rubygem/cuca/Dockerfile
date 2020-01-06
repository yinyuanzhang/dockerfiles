FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.07

RUN gem install cuca --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["cuca"]
CMD ["--help"]
