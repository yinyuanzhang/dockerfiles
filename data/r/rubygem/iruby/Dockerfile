FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.2.9

RUN gem install iruby --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["iruby"]
CMD ["--help"]
