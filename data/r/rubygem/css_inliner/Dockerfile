FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.3.2

RUN gem install css_inliner --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["css-inliner"]
CMD ["--help"]
