FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=3.2.4

RUN gem install inline_forms --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["inline_forms"]
CMD ["--help"]
