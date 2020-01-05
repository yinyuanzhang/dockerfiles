FROM alpine:3.6

RUN apk add --update curl

RUN cd /usr/local/bin \
    && curl -O https://storage.googleapis.com/kubernetes-release/release/v1.7.14/bin/linux/amd64/kubectl \
    && chmod 755 /usr/local/bin/kubectl

ENTRYPOINT ["kubectl"]
