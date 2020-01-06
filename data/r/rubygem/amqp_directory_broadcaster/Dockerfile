FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.0.5

RUN gem install amqp_directory_broadcaster --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["broadcast_directory"]
CMD ["--help"]
