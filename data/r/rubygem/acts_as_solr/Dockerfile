FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.3.3

RUN gem install acts_as_solr --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["acts_as_solr"]
CMD ["--help"]
