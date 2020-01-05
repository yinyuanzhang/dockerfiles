FROM hikarushindo/golang:1.7.5

MAINTAINER Pascal Nitsche

RUN apk add --no-cache --virtual .build-deps git bzr && \
    go get github.com/mailhog/MailHog && \
    apk del .build-deps

EXPOSE 1025 8025

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

ENTRYPOINT ["/go/bin/MailHog"]
