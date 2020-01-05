# Derived from https://gist.github.com/mikebryant/f5b25f9b14e5d6275ff0d3e934f73f12
FROM alpine:3.5

RUN apk add --no-cache curl jq \
  && curl -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.6.1/bin/linux/amd64/kubectl \
  && chmod +x /usr/local/bin/kubectl

COPY rmpeers /usr/local/bin/

CMD ["/usr/local/bin/rmpeers"]
