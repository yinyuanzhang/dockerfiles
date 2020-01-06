FROM elasticsearch:5

RUN touch /usr/share/elasticsearch/config/elasticsearch.yml && \
    echo -n > /usr/share/elasticsearch/config/elasticsearch.yml && \
    echo "cluster.name: 'docker-cluster'" >> /usr/share/elasticsearch/config/elasticsearch.yml && \
    echo "network.host: 0.0.0.0" >> /usr/share/elasticsearch/config/elasticsearch.yml && \
    echo "discovery.type: 'single-node'" >> /usr/share/elasticsearch/config/elasticsearch.yml && \
    echo "discovery.zen.minimum_master_nodes: 1" >> /usr/share/elasticsearch/config/elasticsearch.yml && \
    echo "http.cors.enabled: true" >> /usr/share/elasticsearch/config/elasticsearch.yml && \
    echo "http.cors.allow-origin: '*'" >> /usr/share/elasticsearch/config/elasticsearch.yml && \
    echo "http.cors.allow-headers: X-Requested-With,X-Auth-Token,Content-Type,Content-Length,Authorization" >> /usr/share/elasticsearch/config/elasticsearch.yml && \
    echo "http.cors.allow-credentials: true" >> /usr/share/elasticsearch/config/elasticsearch.yml
