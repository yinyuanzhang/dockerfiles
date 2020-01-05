FROM docker.elastic.co/elasticsearch/elasticsearch:6.4.3

LABEL maintainer="Ingo Kempf" description="Elasticsearch for Openshift"

# Override config
ADD config /usr/share/elasticsearch/config

# Set environment variables defaults
ENV ES_JAVA_OPTS="-Xms512m -Xmx512m" \
    NODE_NAME=default_node \
    MEMORY_LOCK=false \
    DISCOVERY_SERVICE=elasticsearch-discovery \
    CLUSTER_NAME=elasticsearch-default \
    NODE_MASTER=true \
    NODE_DATA=true \
    NODE_INGEST=true \
    HTTP_ENABLE=true \
    NETWORK_HOST=_site_ \
    HTTP_CORS_ENABLE=true \
    HTTP_CORS_ALLOW_ORIGIN=* \
    NUMBER_OF_MASTERS=1 \
    MAX_LOCAL_STORAGE_NODES=1 \
    SHARD_ALLOCATION_AWARENESS="" \
    SHARD_ALLOCATION_AWARENESS_ATTR="" \
    MEMORY_LOCK=false \
    REPO_LOCATIONS=""