# An image for wget, user context
#
# e.g.:  `docker run mwendler/wget google.com`

FROM        alpine

MAINTAINER  Kilian Marjew

RUN apk add --update --no-cache openssl wget

RUN addgroup -g 1000 wget \
  && adduser -u 1000 -G wget -s /bin/sh -D wget

USER wget
WORKDIR /home/wget

ENTRYPOINT  ["wget"]
