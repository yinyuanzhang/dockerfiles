FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.2

RUN gem install cukecooker --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["cukecooker"]
CMD ["--help"]
