FROM grafana/grafana:6.4.3
# https://hub.docker.com/r/grafana/grafana/tags/

COPY datasources /etc/grafana/provisioning/datasources/
COPY swarmprom_dashboards.yml /etc/grafana/provisioning/dashboards/
COPY dashboards /etc/grafana/dashboards/

ENV GF_SECURITY_ADMIN_PASSWORD=admin \
    GF_SECURITY_ADMIN_USER=admin \
    GF_PATHS_PROVISIONING=/etc/grafana/provisioning/

# install https://grafana.com/plugins/grafana-piechart-panel/installation
# actually can't do it here, need to use GF_INSTALL_PLUGINS=grafana-piechart-panel
#RUN grafana-cli plugins install grafana-piechart-panel

