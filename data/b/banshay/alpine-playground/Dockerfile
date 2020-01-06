FROM alpine:latest

RUN apk update && apk add --update \
  curl \
  tar \
  bash \
  nano \
  unzip

CMD exec /bin/bash -c "while sleep 3600; do :; done"
