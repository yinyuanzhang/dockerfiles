FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=1.9.6

RUN gem install inploy --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["inploy"]
CMD ["--help"]
