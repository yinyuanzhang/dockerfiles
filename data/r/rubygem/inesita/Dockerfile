FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.6.1

RUN gem install inesita --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["inesita"]
CMD ["--help"]
