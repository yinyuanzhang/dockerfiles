FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.3.0

RUN gem install cui8tracks --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["cui8tracks"]
CMD ["--help"]
