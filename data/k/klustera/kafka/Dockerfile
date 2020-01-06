FROM klustera/java8

## Basado en Kafka Docker de Wurstmeister
MAINTAINER Adolfo De Unánue <adolfo@klustera.com>

RUN apt-get install docker jq  # Lo ocupa el script start-kafka.sh

ENV KAFKA_VERSION="0.9.0.1"
ENV SCALA_VERSION="2.11"

## Descarga Kafka
ADD ./scripts/download.sh /tmp/download.sh

RUN \
    /tmp/download.sh \
    && tar xfz /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt \
    && rm /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz

RUN ln -s /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION} /opt/kafka

ENV KAFKA_HOME /opt/kafka

VOLUME ["/kafka"]

ADD ./scripts/start-kafka.sh /usr/bin/start-kafka.sh
ADD ./scripts/broker-list.sh /usr/bin/broker-list.sh
ADD ./scripts/create-topics.sh /usr/bin/create-topics.sh

CMD ["start-kafka.sh"]
