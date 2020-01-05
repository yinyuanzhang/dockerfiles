FROM python:3-alpine

LABEL maintainer="b.eyselein@gmail.com"

ARG WORKDIR=/data

RUN apk update && \
    apk upgrade && \
    apk add bash gcc musl-dev && \
    pip install -U pip jsonschema pylint typing_extensions

COPY .pylintrc $WORKDIR/

WORKDIR ${WORKDIR}