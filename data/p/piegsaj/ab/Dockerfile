FROM alpine

MAINTAINER Jens Piegsa <piegsa@gmail.com>

ENV RUNTIME_PACKAGES apache2-utils

RUN apk add --no-cache $RUNTIME_PACKAGES

USER daemon:daemon

ENTRYPOINT ["/usr/bin/ab"]

CMD ["--help"]
