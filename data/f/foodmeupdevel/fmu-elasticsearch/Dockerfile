FROM docker.elastic.co/elasticsearch/elasticsearch:6.7.1

MAINTAINER Julien Guittard <julien.guittard@foodmeup.io>

RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu && \
    /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-phonetic
