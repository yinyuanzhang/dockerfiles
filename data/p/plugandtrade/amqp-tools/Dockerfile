FROM alpine:latest

RUN apk update && \
    apk add --update curl python && \
    curl https://raw.githubusercontent.com/rabbitmq/rabbitmq-management/v3.7.5/bin/rabbitmqadmin -o /usr/bin/rabbitmqadmin && \
    chmod +x /usr/bin/rabbitmqadmin && \
    mkdir -p /migrations

ENV RABBIT_HOST=rabbitmq \
    RABBIT_PORT=15672 \
    RABBIT_USER=guest \
    RABBIT_PWD=guest \
    RABBIT_VHOST=/

VOLUME /migrations
