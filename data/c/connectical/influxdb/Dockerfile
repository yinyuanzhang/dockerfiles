FROM alpine:3.10

COPY docker /tmp/docker

ADD https://github.com/influxdata/influxdb/archive/v1.7.9.tar.gz /tmp/build/influxdb.tar.gz

RUN /tmp/docker/build.sh

EXPOSE 8086

VOLUME [ "/etc/influxdb", "/var/lib/influxdb" ]

USER influxdb

ENTRYPOINT [ "/usr/bin/influxd" ]
