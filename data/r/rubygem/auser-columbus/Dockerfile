FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.0.6

RUN gem install auser-columbus --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["columbus"]
CMD ["--help"]
