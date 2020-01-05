FROM docker.elastic.co/elasticsearch/elasticsearch:7.1.1
MAINTAINER Nathan Rzepecki <nathan@lionslair.net.au>

COPY --chown=elasticsearch:elasticsearch config/elasticsearch.yml /usr/share/elasticsearch/config/
COPY --chown=elasticsearch:elasticsearch config/jvm.options /usr/share/elasticsearch/config/
