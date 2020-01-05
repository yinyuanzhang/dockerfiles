FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.0.4

RUN gem install erb2haml_cli --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["erb2haml"]
CMD ["--help"]
