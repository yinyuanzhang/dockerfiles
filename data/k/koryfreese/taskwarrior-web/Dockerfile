FROM alpine:3.5
MAINTAINER kory Freese

RUN apk add --no-cache ruby ruby-bundler ruby-dev build-base task
RUN gem install --no-ri --no-rdoc taskwarrior-web

COPY ./docker-entrypoint.sh /

# Configure container
VOLUME ["/root/.task"]

ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 5678
