## Using elasticsearch 6.6.0 as base
## https://hub.docker.com/_/elasticsearch?tab=description
FROM docker.elastic.co/elasticsearch/elasticsearch:6.6.0
COPY --chown=elasticsearch:elasticsearch elasticsearch.yml /usr/share/elasticsearch/config/

## Performance Tweaks
RUN echo "* - nofile 65535" >> /etc/security/limits.conf && \
    echo "* - memlock unlimited" >> /etc/security/limits.conf && \
    echo vm.max_map_count=262144 > /etc/sysctl.d/max_map_count.conf && \
    echo vm.swappiness=0 > /etc/sysctl.d/swappiness.conf

## Install Plugins

# NLPChina
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install \
    https://github.com/NLPchina/elasticsearch-analysis-ansj/releases/download/v6.6.0/elasticsearch-analysis-ansj-6.6.0.0-release.zip \
    --batch
