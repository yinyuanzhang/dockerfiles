FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.4.0

RUN gem install bagit --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["bagit"]
CMD ["--help"]
