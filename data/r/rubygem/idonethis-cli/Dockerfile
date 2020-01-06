FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.9.0

RUN gem install idonethis-cli --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["idonethis"]
CMD ["--help"]
