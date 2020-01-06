FROM openjdk:8-jdk

ENV JANUS_VERSION=0.4.0

RUN curl -fSL https://github.com/JanusGraph/janusgraph/releases/download/v${JANUS_VERSION}/janusgraph-${JANUS_VERSION}-hadoop2.zip -o janusgraph.zip && \
    unzip janusgraph.zip && \
    mv janusgraph-${JANUS_VERSION}-hadoop2 /opt/janusgraph && \
    rm janusgraph.zip

EXPOSE 8182

COPY gremlin-server.yaml /opt/janusgraph/conf/gremlin-server.yaml
COPY janusgraph-server-empty.properties /opt/janusgraph/conf/janusgraph-server-empty.properties
COPY generate-graphs.groovy /opt/janusgraph/generate-graphs.groovy

ENTRYPOINT [ "/opt/janusgraph/bin/gremlin-server.sh" ]
CMD ["/opt/janusgraph/conf/gremlin-server.yaml"]