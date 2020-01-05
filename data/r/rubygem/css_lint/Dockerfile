FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.9.9.1

RUN gem install css_lint --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["css_lint"]
CMD ["--help"]
