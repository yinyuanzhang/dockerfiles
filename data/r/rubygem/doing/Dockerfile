FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.0.8pre

RUN gem install doing --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["doing"]
CMD ["--help"]
