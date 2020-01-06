FROM golang

RUN \
  go get -v -u github.com/prometheus/memcached_exporter

ENTRYPOINT [ "memcached_exporter" ]
