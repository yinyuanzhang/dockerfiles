FROM python:3.7-alpine

# Sep 25, 2019 marker

LABEL maintainer="alex.khaerov@chainstack.com"
LABEL vendor="Chainstack"

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PIPENV_HIDE_EMOJIS=true \
  PIPENV_COLORBLIND=true \
  PIPENV_NOSPIN=true \
  PIPENV_DOTENV_LOCATION=config/.env

# System deps:

RUN apk --no-cache add \
     bash \
     build-base \
     curl \
     gcc \
     gettext \
     git \
     libffi-dev \
     linux-headers \
     musl-dev \
     mysql-dev \
     tini \
     py-pip \
     ca-certificates \
     && update-ca-certificates

RUN pip install pipenv dump-env poetry
