FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.4

RUN gem install cutcsv --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["cutcsv"]
CMD ["--help"]
