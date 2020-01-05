FROM alpine:3.3

RUN apk update && \
    apk upgrade && \
    apk add protobuf && \
    rm -rf /var/cache/apk/*

VOLUME /mnt

WORKDIR /mnt

ENTRYPOINT ["protoc"]
