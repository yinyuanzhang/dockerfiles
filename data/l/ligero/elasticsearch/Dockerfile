FROM elasticsearch:6.5.1


RUN echo "cluster.routing.allocation.disk.threshold_enabled: false" >> /usr/share/elasticsearch/config/elasticsearch.yml \
    && elasticsearch-plugin install --batch ingest-attachment \
    && sed -i 's/%marker/\[%node_name\]%marker /' /usr/share/elasticsearch/config/log4j2.properties