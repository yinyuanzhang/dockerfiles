FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.2.2

RUN gem install athena --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["athena"]
CMD ["--help"]
