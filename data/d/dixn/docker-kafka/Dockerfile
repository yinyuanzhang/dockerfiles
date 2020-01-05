# Kafka and Zookeeper

FROM openjdk:11-jre-slim

ENV DEBIAN_FRONTEND noninteractive

# Install Kafka, Zookeeper and other needed things
RUN apt-get update && \
    apt-get install -y zookeeper curl supervisor dnsutils && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

ENV SCALA_VERSION 2.12
ENV KAFKA_VERSION 2.0.0
ENV KAFKA_HOME "/opt/kafka_$SCALA_VERSION-$KAFKA_VERSION"

RUN curl -L "https://www.apache.org/dyn/mirrors/mirrors.cgi?action=download&filename=/kafka/$KAFKA_VERSION/kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz" | tar xfz - -C /opt

ADD scripts/start-kafka.sh /usr/bin/start-kafka.sh

# Supervisor config
ADD supervisor/kafka.conf supervisor/zookeeper.conf /etc/supervisor/conf.d/

# 2181 is zookeeper, 9092 is kafka
EXPOSE 2181 9092

ENV AUTO_CREATE_TOPICS=true

CMD ["supervisord", "-n"]
