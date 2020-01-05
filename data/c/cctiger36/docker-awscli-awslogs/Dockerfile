FROM alpine:latest

RUN apk add --no-cache \
    jq \
    python3 \
 && rm -rf /var/cache/apk/* \
 && pip3 install awscli awslogs
