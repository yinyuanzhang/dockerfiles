FROM elasticsearch:2.4

COPY ./elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

RUN /usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head
RUN /usr/share/elasticsearch/bin/plugin install lmenezes/elasticsearch-kopf
RUN /usr/share/elasticsearch/bin/plugin install analysis-icu
