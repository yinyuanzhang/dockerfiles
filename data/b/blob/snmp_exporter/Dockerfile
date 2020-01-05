FROM golang:1.9 as build

COPY . /go/src/github.com/prometheus/snmp_exporter
WORKDIR /go/src/github.com/prometheus/snmp_exporter

ENV CGO_ENABLED=0

RUN go build -a -ldflags '-extldflags "-static"' . && strip snmp_exporter

FROM        quay.io/prometheus/busybox:latest
MAINTAINER  The Prometheus Authors <prometheus-developers@googlegroups.com>

COPY --from=build /go/src/github.com/prometheus/snmp_exporter/snmp_exporter /bin/snmp_exporter
COPY snmp.yml       /etc/snmp_exporter/snmp.yml

EXPOSE      9116
ENTRYPOINT  [ "/bin/snmp_exporter" ]
CMD         [ "--config.file=/etc/snmp_exporter/snmp.yml" ]
