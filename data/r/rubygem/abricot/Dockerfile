FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.2

RUN gem install abricot --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["abricot"]
CMD ["--help"]
