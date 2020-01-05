FROM python:3.6-alpine3.7

ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    gcc \
    make \
    libc-dev \
    git \
    postgresql-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    jpeg-dev \
    libjpeg-turbo \
    freetype-dev \
    linux-headers
