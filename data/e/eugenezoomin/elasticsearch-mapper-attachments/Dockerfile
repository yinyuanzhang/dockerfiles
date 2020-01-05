FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.11

RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install --batch mapper-attachments

ENV discovery.type=single-node
ENV xpack.security.enabled=false
ENV ES_JAVA_OPTS="-Xms512m -Xmx512m"
