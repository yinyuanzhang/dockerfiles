FROM ruby:2.4

MAINTAINER thinkbot@outlook.de

ENV VERSION=0.4.3

RUN gem install acts_as_icontact --version ${VERSION} --no-format-exec

WORKDIR /tmp

ENTRYPOINT ["icontact"]
CMD ["--help"]
