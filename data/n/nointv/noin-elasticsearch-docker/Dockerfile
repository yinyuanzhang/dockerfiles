FROM elasticsearch:5.6.3

RUN elasticsearch-plugin install analysis-kuromoji
RUN elasticsearch-plugin install analysis-icu

COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

