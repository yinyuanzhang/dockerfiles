FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=2.0.0

RUN gem install about_pos --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["test"]
CMD ["--help"]
