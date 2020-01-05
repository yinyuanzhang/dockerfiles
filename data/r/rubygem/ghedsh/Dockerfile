FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.1.9

RUN gem install ghedsh --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["ghedsh"]
CMD ["--help"]
