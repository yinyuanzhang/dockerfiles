FROM python:3.7-alpine3.8

ENV LANG=en_US.UTF-8 LIBRARY_PATH=/lib:/usr/lib

RUN apk --no-cache add \
  bash \
  build-base \
  ca-certificates \
  cmake \
  curl \
  ffmpeg-dev \
  freetype-dev \
  gettext \
  lcms2-dev \
  libffi-dev \
  libjpeg-turbo-dev \
  libwebp-dev \
  musl \
  openjpeg-dev \
  libressl \
  libressl-dev \
  postgresql \
  postgresql-dev \
  tiff-dev \
  zlib-dev

RUN pip install --no-cache-dir cryptography pynacl pillow
