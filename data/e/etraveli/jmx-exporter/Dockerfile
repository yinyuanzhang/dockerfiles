FROM openjdk:8u121-jre-alpine

MAINTAINER Nils Petzall <nils.petzall@gmail.com>

ARG JMX_EXPORTER_VERSION=0.9

ENV JMX_EXPORTER_VERSION=${JMX_EXPORTER_VERSION}
ENV DONWLOAD_URL="https://repository.sonatype.org/service/local/artifact/maven/redirect?r=central-proxy&g=io.prometheus.jmx&a=jmx_prometheus_httpserver&c=jar-with-dependencies&v=$JMX_EXPORTER_VERSION"

RUN apk --update add curl tzdata && \
    cp /usr/share/zoneinfo/Europe/Stockholm /etc/localtime && \
    echo 'Europe/Stockholm' > /etc/timezone && \
    adduser -S jmx_exporter && \
    mkdir -p /opt/jmx_exporter/lib /opt/jmx_exporter/config && \
    curl -L "${DONWLOAD_URL}" \
      -o /opt/jmx_exporter/lib/jmx_prometheus_httpserver-$JMX_EXPORTER_VERSION-jar-with-dependencies.jar && \
    chown -R jmx_exporter /opt/jmx_exporter && \
    apk del tzdata curl && \
    rm -rf /tmp/* /var/cache/apk/*

USER jmx_exporter

WORKDIR /opt/jmx_exporter

EXPOSE 9209

CMD ["sh", "-c", "java -jar lib/jmx_prometheus_httpserver-${JMX_EXPORTER_VERSION}-jar-with-dependencies.jar 9209 config/jmx_exporter.yml"]
