FROM alpine:edge

RUN apk upgrade --update \
  && apk add curl wget ca-certificates openssl \
  && apk upgrade \
  && rm -rf /var/cache/apk/*

CMD []
