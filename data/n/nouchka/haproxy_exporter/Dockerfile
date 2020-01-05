FROM golang
COPY . /usr/local/go/src/github.com/prometheus/haproxy_exporter/
RUN cd /usr/local/go/src/github.com/prometheus/haproxy_exporter/ && make build
RUN ls -al /usr/local/go/src/github.com/prometheus/haproxy_exporter/

FROM        quay.io/prometheus/busybox:latest
MAINTAINER  The Prometheus Authors <prometheus-developers@googlegroups.com>

COPY --from=0 /usr/local/go/src/github.com/prometheus/haproxy_exporter/haproxy_exporter /bin/haproxy_exporter

ENTRYPOINT ["/bin/haproxy_exporter"]
EXPOSE     9101
