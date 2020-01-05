FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.16

RUN bin/elasticsearch-plugin install analysis-icu
RUN bin/elasticsearch-plugin remove x-pack
RUN bin/elasticsearch-plugin install x-pack

COPY config /usr/share/elasticsearch/config
COPY backup /usr/share/elasticsearch/backup

USER root
RUN chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/config
RUN chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/backup
USER elasticsearch
