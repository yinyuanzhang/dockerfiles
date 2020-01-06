FROM debian:jessie-slim

ADD https://github.com/k14s/ytt/releases/download/v0.14.0/ytt-linux-amd64 /usr/bin/ytt

RUN chmod +x /usr/bin/ytt && mkdir /workspace

WORKDIR /workspace

ENTRYPOINT ["/usr/bin/ytt"]
