FROM docker:dind

LABEL maintainer="benjamin@corelight.com"

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apk update && \
    apk add bash python3 gcc libressl-dev postgresql-dev libffi-dev musl-dev python3-dev  && \
    pip3 install --upgrade pip && \
    pip3 install molecule docker