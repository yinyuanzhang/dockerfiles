FROM neo4j:3.5.11

ENV APOC_VERSION 3.5.0.5
ENV GRAPH_ALGORITHMS_VERSION 3.5.3.4
ENV APOC_URI 			 https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/${APOC_VERSION}/apoc-${APOC_VERSION}-all.jar
ENV GRAPH_ALGORITHMS_URI https://github.com/neo4j-contrib/neo4j-graph-algorithms/releases/download/${GRAPH_ALGORITHMS_VERSION}/graph-algorithms-algo-${GRAPH_ALGORITHMS_VERSION}.jar

RUN apt-get update
RUN apt-get -y install wget

RUN wget $APOC_URI && mv apoc-${APOC_VERSION}-all.jar plugins/apoc-${APOC_VERSION}-all.jar
RUN wget $GRAPH_ALGORITHMS_URI && mv graph-algorithms-algo-${GRAPH_ALGORITHMS_VERSION}.jar plugins/graph-algorithms-algo-${GRAPH_ALGORITHMS_VERSION}.jar

EXPOSE 7474 7473 7687

CMD ["neo4j"]
