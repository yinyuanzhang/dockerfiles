FROM phenompeople/oraclejre
ENV ONGDB_VERSION=3.4.9
EXPOSE 7474 7473 7687 5000
RUN wget -q -O /tmp/ongdb.tar.gz "https://cdn.graphfoundation.org/ongdb/dist/ongdb-enterprise-${ONGDB_VERSION}-unix.tar.gz" && \
    tar -xzf /tmp/ongdb.tar.gz -C /usr/local && \
    ln -sf /usr/local/ongdb-enterprise-${ONGDB_VERSION} /usr/local/ongdb

WORKDIR /usr/local/ongdb
ENV ONGDB_HOME=/usr/local/ongdb
ENV PATH=$ONGDB_HOME/bin:$PATH
ENTRYPOINT ["neo4j", "console"]