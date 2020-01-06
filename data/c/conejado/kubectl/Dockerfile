FROM alpine

ENV VERSION=v1.16.2

RUN apk add --no-cache git && \
    wget -O /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/${VERSION}/bin/linux/amd64/kubectl && \
    chmod +x /usr/local/bin/kubectl

WORKDIR /

CMD ["kubectl"]
