FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.0.1

RUN gem install download_files --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["download_files"]
CMD ["--help"]
