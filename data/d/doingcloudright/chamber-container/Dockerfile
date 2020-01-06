FROM alpine:3.8

# Chamber installation
ARG CHAMBER_VERSION=2.2.0
ARG CHAMBER_SHA256SUM=1a19044ec21cc7e9c9e155c89c3da222640b5002b135c893daaba892863cc062

RUN mkdir /shared

RUN apk update && apk upgrade && apk add  --no-cache ca-certificates wget && update-ca-certificates \
    && wget https://github.com//segmentio/chamber/releases/download/v${CHAMBER_VERSION}/chamber-v${CHAMBER_VERSION}-linux-amd64 -O /shared/chamber \
    && chmod +x /shared/chamber \
    && echo "${CHAMBER_SHA256SUM}  /shared/chamber" > /shared/chamber_SHA256SUMS \
    && sha256sum -c /shared/chamber_SHA256SUMS \
    && rm -rf /var/cache/apk/* \
    && rm /shared/chamber_SHA256SUMS
