FROM elasticsearch:2.3.3

ENV JDBC_IMPORTER_VERSION 2.3.3.0
ENV JDBC_IMPORTER_URL http://xbib.org/repository/org/xbib/elasticsearch/importer/elasticsearch-jdbc/$JDBC_IMPORTER_VERSION/elasticsearch-jdbc-$JDBC_IMPORTER_VERSION-dist.zip

# Download and install the Elasticsearch-jdbc package
RUN wget -O /tmp/elasticsearch-jdbc-$JDBC_IMPORTER_VERSION.zip $JDBC_IMPORTER_URL \
    && unzip -d /opt /tmp/elasticsearch-jdbc-$JDBC_IMPORTER_VERSION.zip \
    && ln -s /opt/elasticsearch-jdbc-$JDBC_IMPORTER_VERSION /opt/elasticsearch-jdbc \
    && rm /tmp/elasticsearch-jdbc-$JDBC_IMPORTER_VERSION.zip
