FROM alpine:3.8

WORKDIR /root

ADD https://github.com/prometheus/prometheus/releases/download/v2.6.0/prometheus-2.6.0.linux-armv7.tar.gz /root/
RUN tar -xzvf prometheus-*.tar.gz -C ./ --strip-components=1

RUN mkdir -p /usr/share/prometheus
RUN mkdir -p /etc/prometheus

RUN cp prometheus                             /bin/prometheus
RUN cp promtool                               /bin/promtool
RUN cp prometheus.yml  /etc/prometheus/prometheus.yml


EXPOSE     9090
VOLUME     [ "/prometheus" ]
WORKDIR    /prometheus
ENTRYPOINT [ "/bin/prometheus" ]
CMD [ "--config.file=/etc/prometheus/prometheus.yml"]
