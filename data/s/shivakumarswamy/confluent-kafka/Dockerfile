FROM python:3.6-alpine3.7

LABEL maintainer="Shivakumar Swamy B G <shivsks.1994@gmail.com>"

ARG CONFLUENT_KAFKA_VERSION="0.11.0"
ARG LIBRDKAFKA_VERSION="0.11.1-r1"

RUN \
    apk add \
    --no-cache \
    librdkafka=$LIBRDKAFKA_VERSION \
    && apk add \
    --no-cache \
    --virtual install-dependencies \
    g++ \
    librdkafka-dev=$LIBRDKAFKA_VERSION \
    \
    && pip3 install confluent-kafka==$CONFLUENT_KAFKA_VERSION \
    && apk del install-dependencies
