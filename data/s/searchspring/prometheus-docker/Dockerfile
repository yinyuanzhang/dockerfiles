FROM prom/prometheus

COPY prometheus/* /etc/prometheus/

EXPOSE 9090

CMD [ \
  "-config.file=/etc/prometheus/prometheus.yml", \
  "-storage.local.path=/prometheus", \
  "-alertmanager.url=http://alertmanager.prometheus:9093" ]