FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.1.0

RUN gem install adlint-postfilter --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["adlint_flt"]
CMD ["--help"]
