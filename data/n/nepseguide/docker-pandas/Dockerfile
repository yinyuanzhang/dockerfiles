FROM python:3.7-alpine3.10
MAINTAINER devops@nepseguide.com

WORKDIR "/app"

RUN apk add --no-cache --virtual .build-deps \
        gcc \
        make \
        g++ && \
        apk add --no-cache --virtual .run-deps \
        postgresql-dev \
    libpq \
        git openssh-client\
        libev-dev

ENV LC_ALL=en_US.UTF-8

# copy the generic requirement
COPY requirements.txt /tmp

RUN pip install --no-cache-dir --requirement /tmp/requirements.txt && apk del .build-deps

CMD ["pip","--version"]

