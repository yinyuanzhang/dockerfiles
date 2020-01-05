FROM python:3.7-alpine
LABEL maintainer="Clément <plopoyop@gmail.com>"

RUN apk add --no-cache \
        openssl \
        su-exec

RUN set -e; \
    apk add --no-cache --virtual .build-deps \
        gcc \
        libc-dev \
        linux-headers \
        libffi-dev \
        make \
        openssl-dev \
        python3-dev \
        ; \
    pip install mycli \
        paramiko; \
    apk del .build-deps;

RUN pip install mycli

RUN adduser user -D

COPY entrypoint.sh /entrypoint.sh

CMD ["mycli", "--help"]
ENTRYPOINT ["/entrypoint.sh"]
