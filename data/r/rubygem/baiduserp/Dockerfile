FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=2.5.5

RUN gem install baiduserp --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["baiduserp"]
CMD ["--help"]
