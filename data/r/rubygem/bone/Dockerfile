FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.2.4

RUN gem install bone --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["bone"]
CMD ["--help"]
