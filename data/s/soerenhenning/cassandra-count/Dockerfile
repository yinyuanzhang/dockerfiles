FROM openjdk:8-alpine

RUN wget https://github.com/brianmhess/cassandra-count/releases/download/v0.0.6/cassandra-count
RUN chmod +x cassandra-count

CMD ./cassandra-count -host $CASSANDRA_HOST -port $CASSANDRA_PORT -keyspace $KEYSPACE -table $TABLE | awk '{print $NF}'
