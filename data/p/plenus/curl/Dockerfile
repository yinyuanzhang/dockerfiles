FROM alpine:3.8

# derived from https://raw.githubusercontent.com/appropriate/docker-curl/master/latest/entrypoint.sh
MAINTAINER Massimiliano Ferrero <m.ferrero@cognitio.it>

RUN apk add --update curl && rm -rf /var/cache/apk/*
COPY entrypoint.sh /
RUN chmod 755 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["curl"]
