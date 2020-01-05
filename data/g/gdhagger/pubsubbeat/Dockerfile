FROM alpine:latest

ENV PUBSUBBEAT_VERSION 1.1.0

RUN apk add --no-cache ca-certificates

ADD https://github.com/GoogleCloudPlatform/pubsubbeat/releases/download/${PUBSUBBEAT_VERSION}/pubsubbeat-linux-amd64.tar.gz /tmp/pubsubbeat.tgz
RUN  mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \
 && tar xvzf /tmp/pubsubbeat.tgz \
 && rm -rf /tmp/pubsubbeat.tgz

ENTRYPOINT /pubsubbeat-linux-amd64/pubsubbeat
