FROM python:3.7-alpine3.8

ENV PIP_VERSION=19.1.1
ENV PIPENV_VERSION=2018.11.26
ENV SCOUTSUITE_VERSION=5.2.0

RUN apk add --update -q --no-cache bash build-base curl git libffi-dev libressl-dev libc-dev make openldap-dev openssh-client rsync tzdata linux-headers
RUN pip install pip==${PYTHON_PIP_VERSION} && \
    pip install --upgrade pipenv==${PIPENV_VERSION}
RUN pip install scoutsuite==${SCOUTSUITE_VERSION}
