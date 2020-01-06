
# Elasticsearch 5.6.16

# This image re-bundles the Docker image from the upstream provider, Elastic.
FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.16
ENV ZDB_VERSION 5.6.16-1.0.18

# Install zombodb
RUN set -eux ; \
    echo "Install Zombodb" ; \
    wget --no-check-certificate --quiet -O /tmp/zombodb.zip https://www.zombodb.com/releases/v${ZDB_VERSION}/zombodb-es-plugin-${ZDB_VERSION}.zip ; \
    /usr/share/elasticsearch/bin/elasticsearch-plugin install --silent file:///tmp/zombodb.zip ; \
    rm -Rf /tmp/zombodb.*
