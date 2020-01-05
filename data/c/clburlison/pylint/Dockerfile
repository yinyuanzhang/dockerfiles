FROM python:2-alpine
MAINTAINER "Clayton Burlison" <git@clburlison.com>

RUN apk add --no-cache \
    git \
    openssh-client \
    && pip install flake8 flake8-docstrings pylint
