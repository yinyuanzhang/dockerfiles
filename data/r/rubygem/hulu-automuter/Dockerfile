FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.1.0

RUN gem install hulu-automuter --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["hulu-automuter"]
CMD ["--help"]
