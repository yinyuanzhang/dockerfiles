FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.9.1

RUN gem install cide --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["cide"]
CMD ["--help"]
