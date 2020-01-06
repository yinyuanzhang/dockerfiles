FROM golang:1.10-alpine as build

COPY . /go/src/github.com/minio/minio

WORKDIR /go/src/github.com/minio/minio

ENV CGO_ENABLED 0

RUN apk add --no-cache git
RUN go get -d github.com/minio/minio
RUN go install -ldflags "$(go run buildscripts/gen-ldflags.go)"

FROM alpine:3.7

ENV MINIO_UPDATE off
ENV MINIO_ACCESS_KEY_FILE=access_key
ENV MINIO_SECRET_KEY_FILE=secret_key

COPY --from=build /go/bin/minio /usr/bin/
COPY dockerscripts/docker-entrypoint.sh dockerscripts/healthcheck.sh /usr/bin/

RUN apk add --no-cache ca-certificates curl && \
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf

EXPOSE 9000

VOLUME ["/data"]

HEALTHCHECK --interval=30s --timeout=5s CMD /usr/bin/healthcheck.sh

ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]

CMD ["minio"]
