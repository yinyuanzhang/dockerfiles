FROM sumglobal/rpi-openjdk:8-jdk-azul

RUN [ "cross-build-start" ]

ENV DEBIAN_FRONTEND noninteractive
ENV SCALA_VERSION 2.11
ENV KAFKA_VERSION 0.10.2.1
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"

#------------------
# for rpi/ARM
#------------------
ENV KAFKA_HEAP_OPTS -Xmx256M\ -Xms256M
#-----------------------------------------------------------------------------------------------------------------
# Zulu embedded doesn't support the G1 compiler and other options set by default - These are a bit more reasonable
#-----------------------------------------------------------------------------------------------------------------
ENV KAFKA_JVM_PERFORMANCE_OPTS -server\ -XX:+DisableExplicitGC\ -Djava.awt.headless=true

# Install Kafka, Zookeeper and other needed things
RUN apt-get update && \
    apt-get install -y zookeeper wget vim supervisor dnsutils bash docker unzip curl jq coreutils net-tools && \ 
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean && \
    wget -q http://apache.mirrors.spacedump.net/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \
    tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt && \
    rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz

# server properties
ADD config/server.properties $KAFKA_HOME/config/server.properties

ADD scripts/start-kafka.sh /usr/bin/start-kafka.sh

# Supervisor config
ADD supervisor/kafka.conf supervisor/zookeeper.conf /etc/supervisor/conf.d/

# 2181 is zookeeper, 9092 is kafka
EXPOSE 2181 9092

CMD ["supervisord", "-n"]

RUN [ "cross-build-end" ] 
