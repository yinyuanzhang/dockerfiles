FROM alpine

LABEL maintainer="Konstantin Yakushev (https://github.com/kojoru)"


RUN apk update && \
  apk add --no-cache openssl && \
  rm -rf /var/cache/apk/*

ENTRYPOINT ["openssl"]
