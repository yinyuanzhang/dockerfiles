FROM python:2.7.16-alpine3.9
RUN apk update && \
    apk add imagemagick && \
    apk add gcc automake musl-dev libffi-dev openssl-dev && \
    adduser -D -s /bin/sh -u 1000 admin && \
    pip install lektor==3.0.1 && \
    apk del --rdepends --purge gcc automake musl-dev libffi-dev openssl-dev && \
    rm -rf /var/cache/apk

ENTRYPOINT [ "lektor", "--project", "/app" ]
VOLUME /app
WORKDIR /app
USER admin
EXPOSE 5000
CMD [ "server", "-h", "0.0.0.0" ]
