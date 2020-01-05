# build stage
FROM golang:1.9-alpine AS build-env

WORKDIR /workspace

ADD . /workspace/

RUN export GOPATH=/workspace && go build -o /workspace/gcp-iap-auth

# final stage
FROM alpine:3.7

RUN apk add --no-cache --update \
      ca-certificates

COPY --from=build-env /workspace/gcp-iap-auth /usr/local/bin/

EXPOSE 80 443
ENTRYPOINT ["/usr/local/bin/gcp-iap-auth"]