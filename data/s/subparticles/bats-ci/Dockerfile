FROM alpine:3.5

RUN apk --no-cache add \
        bash \
        curl \
        zip \
        unzip \
        tar \
        gzip

ENV BATS_VERSION "1.1.0"
RUN curl -sSL https://github.com/bats-core/bats-core/archive/v$BATS_VERSION.tar.gz -o /tmp/bats.tgz \
    && tar -zxf /tmp/bats.tgz -C /tmp \
    && /bin/bash /tmp/bats-core-$BATS_VERSION/install.sh /usr/local

RUN rm -rf /tmp/*

