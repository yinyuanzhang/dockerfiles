FROM java:openjdk-8-jre-alpine

ENV SCALA_VERSION 2.12
ENV KAFKA_VERSION 2.0.0
ENV KAFKA_HOME /opt/kafka

RUN apk --update add tar curl bash \
  && mkdir -p $KAFKA_HOME-$KAFKA_VERSION \
  && curl -L http://www.gtlib.gatech.edu/pub/apache/kafka/$KAFKA_VERSION/kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz | tar xvz --strip 1 -C $KAFKA_HOME-$KAFKA_VERSION \
  && ln -s $KAFKA_HOME-$KAFKA_VERSION $KAFKA_HOME \
  && rm -f $KAFKA_HOME/config/server.properties

ADD server.properties /opt/kafka/config/server.properties

EXPOSE 9092

CMD ["/opt/kafka/bin/kafka-server-start.sh", "/opt/kafka/config/server.properties"]
