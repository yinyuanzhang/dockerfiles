FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.1.3

RUN gem install capistrano-campout --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["campout"]
CMD ["--help"]
