FROM grafana/grafana:5.2.1

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

COPY provisioning/ /etc/grafana/provisioning
COPY dashboards/  /var/lib/grafana/dashboards
COPY grafana.ini /etc/grafana/grafana.ini
