FROM debezium/connect:0.10
ENV KAFKA_CONNECT_JDBC_DIR=$KAFKA_CONNECT_PLUGINS_DIR/kafka-connect-jdbc 

RUN cd /kafka/libs && curl -sO https://jdbc.postgresql.org/download/postgresql-42.2.6.jar

RUN mkdir $KAFKA_CONNECT_JDBC_DIR && cd $KAFKA_CONNECT_JDBC_DIR &&\
	curl -sO http://packages.confluent.io/maven/io/confluent/kafka-connect-jdbc/5.3.0/kafka-connect-jdbc-5.3.0.jar

