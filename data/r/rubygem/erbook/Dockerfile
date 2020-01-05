FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=9.2.1

RUN gem install erbook --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["erbook"]
CMD ["--help"]
