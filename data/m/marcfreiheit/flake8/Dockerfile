FROM python:3-alpine

ARG FLAKE8_VERSION=3.7.7

WORKDIR /app

RUN pip install flake8==$FLAKE8_VERSION

ENTRYPOINT ["flake8"]
