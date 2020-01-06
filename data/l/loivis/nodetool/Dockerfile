FROM alpine

ENV CASSANDRA_VERSION=3.11.0

RUN apk add --no-cache wget openjdk8-jre

RUN mkdir /opt && cd /opt \
 && wget -q http://archive.apache.org/dist/cassandra/${CASSANDRA_VERSION}/apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz \
 && tar zxf apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz \
 && mv -v apache-cassandra-${CASSANDRA_VERSION} cassandra \
 && rm -fv apache-cassandra-${CASSANDRA_VERSION}-bin.tar.gz

ENV PATH="/opt/cassandra/bin:${PATH}"

ENTRYPOINT ["nodetool"]
