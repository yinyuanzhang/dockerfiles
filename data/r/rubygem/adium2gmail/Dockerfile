FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.1.3

RUN gem install adium2gmail --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["adium2gmail"]
CMD ["--help"]
