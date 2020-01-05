FROM linuxkit/ca-certificates:v0.6 AS ca-certificates

FROM    golang:1.12rc1-alpine AS build
ENV     CGO_ENABLED 0
RUN     apk add --no-cache git
ADD     . /code
WORKDIR /code
RUN     go install

FROM alpine:3.9
COPY --from=build /go/bin/gcs-helper /usr/bin/gcs-helper
COPY --from=ca-certificates / /
ENTRYPOINT ["/usr/bin/gcs-helper"]
