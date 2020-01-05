FROM python:3.6-alpine3.7 AS python-base

COPY requirements.txt /requirements.txt

RUN set -ex \
    && apk --no-cache add --virtual .build-deps \
        gcc \
        make \
        libc-dev \
        musl-dev \
        linux-headers \
        build-base \
        pcre-dev \
        postgresql-dev \
        zlib-dev \
        jpeg-dev \
    && apk --no-cache add \
        libffi-dev \
    && pip install -r /requirements.txt \
    && apk --no-cache del .build-deps

FROM python:3.6-alpine3.7

COPY --from=python-base /root/.cache /root/.cache

RUN addgroup -S petchalet && adduser -S -G petchalet -h /petchalet petchalet

COPY requirements.txt /requirements.txt

RUN set -ex \
    && apk --no-cache add \
        libpq \
        zlib-dev \
        jpeg-dev \
    && pip3 install -r requirements.txt \
    && rm -rf /root/.cache

RUN mkdir /src
WORKDIR /src

ADD . /src/

RUN chmod +x entrypoint.sh
RUN chmod +x wait-for-it.sh
EXPOSE 8000
