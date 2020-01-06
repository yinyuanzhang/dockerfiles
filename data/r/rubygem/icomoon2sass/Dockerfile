FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.0.7

RUN gem install icomoon2sass --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["icomoon2sass"]
CMD ["--help"]
