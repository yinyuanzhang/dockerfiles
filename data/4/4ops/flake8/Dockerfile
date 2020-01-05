FROM python:3.7-alpine

RUN set -ex \
  ; FLAKE8_VERSION="3.7.8" \
  ; apk add --no-cache --virtual=.build-dependencies gcc linux-headers musl-dev \
  ; pip install --no-cache-dir --disable-pip-version-check flake8==$FLAKE8_VERSION flake8-mypy \
  ; apk del .build-dependencies \
  ; flake8 --version
