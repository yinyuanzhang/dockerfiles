FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.2

RUN gem install css_primer --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["css_primer"]
CMD ["--help"]
