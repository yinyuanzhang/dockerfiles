FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.6.3.1286550476

RUN gem install jaf-s3 --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["s3sh"]
CMD ["--help"]
