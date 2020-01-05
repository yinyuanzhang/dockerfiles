FROM  prom/statsd-exporter:latest
LABEL maintainer="Paul Maddox <pmaddox@amazon.com>"

COPY        ./statsd_mapping.yml /tmp/statsd_mapping.yml
USER        nobody
EXPOSE      9102 8125 8125/udp
HEALTHCHECK CMD wget --spider -S "http://localhost:9102/metrics" -T 60 2>&1 || exit 1
ENTRYPOINT  [ "/bin/statsd_exporter", "--statsd.mapping-config=/tmp/statsd_mapping.yml" ]
