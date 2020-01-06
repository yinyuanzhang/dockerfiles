FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.2.2

RUN gem install erb-process --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["erb-process"]
CMD ["--help"]
