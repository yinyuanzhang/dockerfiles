FROM ubuntu:17.10
MAINTAINER RazzDazz
# Using instructions from
# https://www.digitalocean.com/community/tutorials/how-to-install-prometheus-on-ubuntu-16-04
# https://www.robustperception.io/snmp-monitoring-with-prometheus

# 
ENV REFRESHED_AT 2019-01-06
ENV DEBIAN_FRONTEND noninteractive

#
# Preparations
#

# Update packages, install apache, free diskspace
RUN apt-get -yqq update && \
    apt-get -yqq upgrade && \
    apt-get -yqq install curl && \
    apt-get -yqq install supervisor && \
    rm -rf /var/lib/apt/lists/*
    
#
# Install Prometheus 
# 
ENV PROMETHEUS_VER v2.6.0
ENV PROMETHEUS_TAR prometheus-2.6.0.linux-amd64.tar.gz
ENV PROMETHEUS_TAR_FOLDER prometheus-2.6.0.linux-amd64

# Create Folders
RUN mkdir /etc/prometheus
RUN mkdir /var/lib/prometheus
RUN mkdir /opt/prometheus

# Download and extract prometheus sourcen
RUN mkdir -p /tmp/prometheus && \
    cd /tmp/prometheus/ && \
    curl -LO https://github.com/prometheus/prometheus/releases/download/${PROMETHEUS_VER}/${PROMETHEUS_TAR} && \
    tar xvf ${PROMETHEUS_TAR} && \
    cp ${PROMETHEUS_TAR_FOLDER}/prometheus /usr/local/bin/ && \
    cp ${PROMETHEUS_TAR_FOLDER}/promtool /usr/local/bin/ && \
    cp -r ${PROMETHEUS_TAR_FOLDER}/consoles /etc/prometheus && \
    cp -r ${PROMETHEUS_TAR_FOLDER}/console_libraries /etc/prometheus && \
    rm -rf /tmp/prometheus

#
# Install Node Exporter 
# 

ENV NODE_EXPORTER_VER v0.17.0
ENV NODE_EXPORTER_TAR node_exporter-0.17.0.linux-amd64.tar.gz
ENV NODE_EXPORTER_TAR_FOLDER node_exporter-0.17.0.linux-amd64

# Download and extract Node Exporter
RUN mkdir -p /tmp/nodeexporter && \
    cd /tmp/nodeexporter/ && \
    curl -LO https://github.com/prometheus/node_exporter/releases/download/${NODE_EXPORTER_VER}/${NODE_EXPORTER_TAR} && \
    tar xvf ${NODE_EXPORTER_TAR} && \
    cp ${NODE_EXPORTER_TAR_FOLDER}/node_exporter /usr/local/bin/ && \
    rm -rf /tmp/nodeexporter

#
# Install SNMP Exporter
#

ENV SNMP_EXPORTER_VER v0.14.0
ENV SNMP_EXPORTER_TAR snmp_exporter-0.14.0.linux-amd64.tar.gz
ENV SNMP_EXPORTER_TAR_FOLDER snmp_exporter-0.14.0.linux-amd64

RUN mkdir -p /tmp/snmpexporter && \
    cd /tmp/snmpexporter/ && \
    curl -LO https://github.com/prometheus/snmp_exporter/releases/download/${SNMP_EXPORTER_VER}/${SNMP_EXPORTER_TAR} && \
    tar xvf ${SNMP_EXPORTER_TAR} && \
    cp ${SNMP_EXPORTER_TAR_FOLDER}/snmp_exporter /usr/local/bin/ && \
    rm -rf /tmp/snmpexporter

#
# Finalize 
#

# Copy prometheus.yml into container
COPY prometheus.yml /tmp/prometheus.yml.sample

# Copy helper scripts into container
COPY docker-entrypoint.sh /tmp/
RUN chmod 777 /tmp/docker-entrypoint.sh
COPY supervisor_prometheus_bundle.conf /tmp/

#
EXPOSE 9090

VOLUME /var/log/supervisor
VOLUME /var/lib/prometheus
VOLUME /opt/prometheus
          
# Start prometheus using supervisor (useful later to start other apps like node exporter)
CMD ["/tmp/docker-entrypoint.sh"]          
