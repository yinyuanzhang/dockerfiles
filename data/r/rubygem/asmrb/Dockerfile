FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.0.2.6.2.2

RUN gem install asmrb --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["asmrb"]
CMD ["--help"]
