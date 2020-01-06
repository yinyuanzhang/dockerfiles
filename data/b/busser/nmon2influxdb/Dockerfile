FROM golang:alpine as builder
RUN apk add --no-cache git mercurial
RUN go get -u -v github.com/adejoux/nmon2influxdb

FROM alpine as runner
COPY --from=builder /go/bin/nmon2influxdb /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/nmon2influxdb"]
