FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.0.5

RUN gem install inko --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["inko"]
CMD ["--help"]
