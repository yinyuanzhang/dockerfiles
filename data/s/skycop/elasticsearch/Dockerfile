FROM docker.elastic.co/elasticsearch/elasticsearch:6.2.4

RUN elasticsearch-plugin remove --purge x-pack && \
    sed -i -e 's/xpack.license.self_generated.type: basic//g' /usr/share/elasticsearch/config/elasticsearch.yml