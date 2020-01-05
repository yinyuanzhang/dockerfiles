FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=6.1.0

RUN gem install inochi --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["inochi"]
CMD ["--help"]
