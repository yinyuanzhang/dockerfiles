FROM ruby:2.5

RUN gem install razor-client

ENV RAZOR_API=http://razor-server:8080/api
ENTRYPOINT ["/usr/local/bundle/bin/razor"]
