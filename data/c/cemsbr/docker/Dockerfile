FROM python:3.6-alpine3.6

# musl-dev: limits.h
# linux-headers: types.h

RUN apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        linux-headers \
    && pip --no-cache-dir install mypy \
    && apk del --purge .build-deps

RUN apk add --no-cache git

CMD ["/bin/sh"]
