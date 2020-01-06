# Dockerizing elasticsearch images for eXo platform
# 
# Build:    docker build -t exoplatform/elasticsearch .
#
# Run:      docker run -ti exoplatform/elasticsearch
FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.16

# Enforce underlying system package update
USER root
RUN yum update -y && yum clean all -y
USER elasticsearch

# Configure Elasticsearch for eXo Platform
ENV xpack.security.enabled=false
RUN cd /usr/share/elasticsearch \
    && bin/elasticsearch-plugin install -b -s ingest-attachment \
    && bin/elasticsearch-plugin install -b -s mapper-attachments
COPY jvm.options /usr/share/elasticsearch/config/
