FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.0.1

RUN gem install amqp-daemon-kit --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["daemon-kit"]
CMD ["--help"]
