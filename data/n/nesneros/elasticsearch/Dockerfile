FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.8

RUN elasticsearch-plugin install https://github.com/NLPchina/elasticsearch-sql/releases/download/5.6.8.0/elasticsearch-sql-5.6.8.0.zip

ENV PATH_DATA=/usr/share/elasticsearch/data

COPY elasticsearch.yml /usr/share/elasticsearch/config/
USER root
RUN chown elasticsearch:elasticsearch config/elasticsearch.yml
USER elasticsearch
