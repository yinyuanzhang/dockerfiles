FROM alpine:3.7
MAINTAINER Jesper Jeeninga <jesper.jeeninga@trimm.nl>
RUN \
  apk add bash --no-cache && \
  apk add curl --no-cache && \
  apk add mysql-client --no-cache && \
  apk add jq --no-cache
ENTRYPOINT ["bash", "-c"]
