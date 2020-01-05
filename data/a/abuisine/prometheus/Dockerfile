ARG PROMETHEUS_VERSION=v2.0.0
FROM prom/prometheus:${PROMETHEUS_VERSION}
ARG PROMETHEUS_VERSION
LABEL maintainer="Alexandre Buisine <alexandrejabuisine@gmail.com>" version="${PROMETHEUS_VERSION}-1"

USER root
COPY resources/prometheus.yml /etc/prometheus/
COPY resources/docker-entrypoint.sh /usr/local/bin/
ADD https://github.com/kreuzwerker/envplate/releases/download/v0.0.8/ep-linux /usr/local/bin/ep
RUN chmod +x /usr/local/bin/ep /usr/local/bin/docker-entrypoint.sh \
 && chown nobody /etc/prometheus/prometheus.yml

ENV SCRAPE_INTERVAL=30s SCRAPE_TIMEOUT=10s \
 EVALUATION_INTERVAL=30s \
 SERVICE_DISCOVERY_FILE=/prom-rancher-sd-data/rancher.json \
 SERVICE_DISCOVERY_REFRESH_INTERVAL=2m

USER nobody
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD [ "--config.file=/etc/prometheus/prometheus.yml", \
 "--storage.tsdb.path=/prometheus", \
 "--web.console.libraries=/usr/share/prometheus/console_libraries", \
 "--web.console.templates=/usr/share/prometheus/consoles" ]