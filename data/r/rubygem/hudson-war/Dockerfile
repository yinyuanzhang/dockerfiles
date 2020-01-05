FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.395

RUN gem install hudson-war --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["hudson.war"]
CMD ["--help"]
