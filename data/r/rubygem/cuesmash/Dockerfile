FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.6.0

RUN gem install cuesmash --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["cuesmash"]
CMD ["--help"]
