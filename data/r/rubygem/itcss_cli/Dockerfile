FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.1.9

RUN gem install itcss_cli --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["itcss"]
CMD ["--help"]
