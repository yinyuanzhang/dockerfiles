FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.5.0

RUN gem install asdf --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["asdf"]
CMD ["--help"]
