FROM ubuntu:trusty
MAINTAINER François-Guillaume Ribreau <docker@fgribreau.com>

# Install InfluxDB
ENV INFLUXDB_VERSION 0.12.1-1
RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists && \
  curl -s -o /tmp/influxdb_latest_amd64.deb https://s3.amazonaws.com/influxdb/influxdb_${INFLUXDB_VERSION}_amd64.deb && \
  dpkg -i /tmp/influxdb_latest_amd64.deb && \
  rm /tmp/influxdb_latest_amd64.deb && \
  rm -rf /var/lib/apt/lists/*

ADD types.db /usr/share/collectd/types.db
ADD config.toml /config/config.toml
ADD run.sh /run.sh
RUN chmod +x /*.sh

ENV PRE_CREATE_DB **None**
ENV SSL_SUPPORT **False**
ENV SSL_CERT **None**

# Admin server WebUI
EXPOSE 8083

# HTTP API
EXPOSE 8086

# Graphite listener
EXPOSE 2003

# Raft port (for clustering, don't expose publicly!)
#EXPOSE 8090

# Protobuf port (for clustering, don't expose publicly!)
#EXPOSE 8099

VOLUME ["/data"]

CMD ["/run.sh"]
