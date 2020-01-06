# Dockerfile

FROM alpine

RUN apk add --no-cache bash curl

ENV VERSION v0.38.0

RUN curl -sLO https://storage.googleapis.com/skaffold/releases/${VERSION}/skaffold-linux-amd64 && \
    chmod +x skaffold-linux-amd64 && mv skaffold-linux-amd64 /usr/local/bin/skaffold

ENTRYPOINT ["bash"]
