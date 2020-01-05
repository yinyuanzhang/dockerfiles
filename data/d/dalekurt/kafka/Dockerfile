FROM stackbrew/ubuntu:14.04

MAINTAINER Dale-Kurt Murray "dalekurt.murray@gmail.com"

ENV KAFKA_VERSION="0.8.2.1" SCALA_VERSION="2.10"

RUN apt-get update && apt-get install -y unzip openjdk-6-jdk wget curl git docker.io jq

ADD scripts/download-kafka.sh /tmp/download-kafka.sh
RUN /tmp/download-kafka.sh
RUN tar xf /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt

VOLUME ["/kafka"]

ENV KAFKA_HOME /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION}
ADD scripts/start-kafka.sh /usr/bin/start-kafka.sh
ADD scripts/broker-list.sh /usr/bin/broker-list.sh
CMD start-kafka.sh
