FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.7.3

RUN gem install idiom --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["idiom"]
CMD ["--help"]
