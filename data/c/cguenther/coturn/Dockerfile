FROM alpine:latest
MAINTAINER Christian Günther <cguenther.tu.chemnitz@gmail.com>

# Install coturn.
VOLUME /etc/coturn/
RUN apk update && apk upgrade && apk add coturn openssl && rm -rf /var/cache/apk/*

CMD ["turnserver", "-c /etc/coturn/turnserver.conf"]
