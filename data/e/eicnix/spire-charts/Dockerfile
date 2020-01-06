FROM alpine:3.8
LABEL maintainer="Lukas Eichler <lukas@eichler.io>"

ARG SPIRE_VERSION=0.6.0
ARG SPIRE_TGZ=https://github.com/spiffe/spire/releases/download/${SPIRE_VERSION}/spire-${SPIRE_VERSION}-linux-x86_64-glibc.tar.gz

RUN apk add --no-cache --virtual .build-deps curl tar gzip ca-certificates 

RUN curl --silent --location $SPIRE_TGZ | tar --directory /tmp -xzf - \
    && mv /tmp/spire-${SPIRE_VERSION} /tmp/spire \
    && ls -lah /tmp/spire 

FROM debian:8.11-slim
COPY --from=0 /tmp/spire/spire-agent /spire-agent
COPY --from=0 /tmp/spire/spire-server /spire-server
RUN apt-get update && apt-get install -y ca-certificates
ENTRYPOINT [ "/bin/bash" ]