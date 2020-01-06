FROM alpine:latest

# Based on https://github.com/monostream/docker-rancher-compose/blob/master/Dockerfile

ARG RANCHER_COMPOSE_VERSION=0.12.5

RUN apk add --quiet --no-cache ca-certificates curl unzip bash && \
	curl -sSL "https://github.com/rancher/rancher-compose/releases/download/v${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-amd64-v${RANCHER_COMPOSE_VERSION}.tar.gz" | tar -xzp -C /usr/local/bin/ --strip-components=2 && \
rm -rf /var/cache/*
