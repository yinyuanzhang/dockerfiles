FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.3.3

RUN gem install csscss --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["csscss"]
CMD ["--help"]
