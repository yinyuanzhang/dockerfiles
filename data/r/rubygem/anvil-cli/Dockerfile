FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.9.3

RUN gem install anvil-cli --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["anvil"]
CMD ["--help"]
