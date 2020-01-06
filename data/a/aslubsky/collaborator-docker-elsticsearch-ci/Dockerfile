FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.14

#ENV bootstrap.memory_lock=true
ENV xpack.security.enabled=false
ENV indices.query.bool.max_clause_count=10000

RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu
