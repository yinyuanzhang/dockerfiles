FROM solr:5.4
MAINTAINER LWB

RUN mkdir -p /opt/solr/server/solr/core-portal/data && \
    mkdir -p /opt/solr/server/solr/core-shop/data && \
    mkdir -p /opt/solr/server/solr/core-portal/conf && \
    mkdir -p /opt/solr/server/solr/core-shop/conf

RUN mkdir -p /opt/solr/server/solr/core-vdb/data && \
    mkdir -p /opt/solr/server/solr/core-vdb_vwg/data && \
    mkdir -p /opt/solr/server/solr/core-vdb/conf && \
    mkdir -p /opt/solr/server/solr/core-vdb_vwg/conf

COPY cores/portal/core.properties /opt/solr/server/solr/core-portal/
COPY cores/shop/core.properties /opt/solr/server/solr/core-shop/
COPY cores/portal/conf /opt/solr/server/solr/core-portal/conf
COPY cores/shop/conf /opt/solr/server/solr/core-shop/conf

COPY cores/vdb/core.properties /opt/solr/server/solr/core-vdb/
COPY cores/vdb_vwg/core.properties /opt/solr/server/solr/core-vdb_vwg/
COPY cores/vdb/conf /opt/solr/server/solr/core-vdb/conf
COPY cores/vdb_vwg/conf /opt/solr/server/solr/core-vdb_vwg/conf

USER root

RUN chown -R $SOLR_USER:$SOLR_USER /opt/solr/server/solr/core-portal && \
    chown -R $SOLR_USER:$SOLR_USER /opt/solr/server/solr/core-shop

RUN chown -R $SOLR_USER:$SOLR_USER /opt/solr/server/solr/core-vdb && \
		chown -R $SOLR_USER:$SOLR_USER /opt/solr/server/solr/core-vdb_vwg

VOLUME /opt/solr/server/solr/core-portal/data
VOLUME /opt/solr/server/solr/core-shop/data
VOLUME /opt/solr/server/solr/core-vdb/data
VOLUME /opt/solr/server/solr/core-vdb_vwg/data

CMD ["/opt/solr/bin/solr", "restart", "-f"]
