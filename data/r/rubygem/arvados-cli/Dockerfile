FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.1.pre.20130710100340

RUN gem install arvados-cli --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["arv"]
CMD ["--help"]
