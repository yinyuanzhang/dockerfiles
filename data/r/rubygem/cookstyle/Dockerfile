FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.3.0

RUN gem install cookstyle --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["cookstyle"]
CMD ["--help"]
