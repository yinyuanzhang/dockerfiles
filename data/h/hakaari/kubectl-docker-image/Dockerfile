FROM alpine

RUN apk add --update ca-certificates \
    && apk add --update -t deps curl \
    && curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl \
    && chmod +x ./kubectl \
    && mv ./kubectl /usr/local/bin/kubectl \
    && apk del --purge deps \
    && rm /var/cache/apk/*
