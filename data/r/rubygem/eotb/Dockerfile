FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.5.9

RUN gem install eotb --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["eotb"]
CMD ["--help"]
