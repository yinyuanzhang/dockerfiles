FROM solr
COPY ./scripts/export_solrthost.sh /docker-entrypoint-initdb.d/
COPY ./scripts/set_solrhost.sh /docker-entrypoint-initdb.d/
COPY ./solr /opt/solr/server/solr_orig
USER root
RUN chmod +x /docker-entrypoint-initdb.d/*.sh
RUN chown -R solr /opt/solr/server/solr 
USER solr
