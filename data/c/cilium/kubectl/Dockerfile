FROM alpine:3.8

RUN apk add --update ca-certificates \
 && apk add --update -t deps curl \
 && curl -L https://storage.googleapis.com/kubernetes-release/release/v1.12.1/bin/linux/amd64/kubectl -o /usr/bin/kubectl \
 && chmod +x /usr/bin/kubectl \
 && apk del --purge deps \
 && rm /var/cache/apk/*
