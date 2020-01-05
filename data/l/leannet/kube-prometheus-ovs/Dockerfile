FROM prom/prometheus:master

copy kube-prometheus-ovs.yml /etc/prometheus/prometheus.yml

EXPOSE     9090
VOLUME     [ "/prometheus" ]
WORKDIR    /prometheus
ENTRYPOINT [ "/bin/prometheus" ]
CMD        [ "--config.file=/etc/prometheus/prometheus.yml", \
             "--storage.tsdb.path=/prometheus", \
             "--web.enable-lifecycle", \
             "--web.console.libraries=/etc/prometheus/console_libraries", \
             "--web.console.templates=/etc/prometheus/consoles" ]

