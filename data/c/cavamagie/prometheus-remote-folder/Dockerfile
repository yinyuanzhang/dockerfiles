ARG ARCH="amd64"
ARG OS="linux"
ARG BASE_IMAGE=alpine:3.10
FROM ${BASE_IMAGE}
# test deploy to apline image
#FROM quay.io/prometheus/busybox-${OS}-${ARCH}:latest
LABEL maintainer="The Prometheus Authors <prometheus-developers@googlegroups.com>"

ARG ARCH="amd64"
ARG OS="linux"
COPY ${OS}-${ARCH}/prometheus        /bin/prometheus
COPY ${OS}-${ARCH}/promtool          /bin/promtool
RUN mkdir -p /prometheus/config
COPY documentation/examples/prometheus.yml  /prometheus/config/prometheus.yml
COPY console_libraries/                     /usr/share/prometheus/console_libraries/
COPY consoles/                              /usr/share/prometheus/consoles/

RUN ln -s /usr/share/prometheus/console_libraries /usr/share/prometheus/consoles/ /prometheus/config/
RUN chown -R nobody:nogroup  /prometheus

USER       nobody
EXPOSE     9090
VOLUME     [ "/prometheus" ]
WORKDIR    /prometheus
ENTRYPOINT [ "/bin/prometheus" ]
CMD        [ "--config.file=/prometheus/config/prometheus.yml", \
             "--storage.tsdb.path=/prometheus", \
             "--web.console.libraries=/usr/share/prometheus/console_libraries", \
             "--web.enable-lifecycle", \
             "--web.console.templates=/usr/share/prometheus/consoles" ]
