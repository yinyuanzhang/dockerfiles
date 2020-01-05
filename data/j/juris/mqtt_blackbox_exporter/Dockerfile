FROM golang:1.11.1-alpine3.8

COPY . /go/src/mqtt_blackbox_exporter

RUN apk add --no-cache git upx \
    && go get github.com/pwaller/goupx \
    && cd /go/src/mqtt_blackbox_exporter \
    && go build -ldflags="-s -w" \
    && goupx mqtt_blackbox_exporter

FROM alpine:3.8

RUN apk --no-cache add ca-certificates && update-ca-certificates
COPY --from=0 /go/src/mqtt_blackbox_exporter/mqtt_blackbox_exporter /bin/mqtt_blackbox_exporter

ENTRYPOINT ["/bin/mqtt_blackbox_exporter"]
CMD ["-config.file /data/config.yaml"]
