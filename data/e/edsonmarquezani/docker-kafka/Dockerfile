FROM anapsix/alpine-java

ENV KAFKA_VERSION 1.1.0
ENV SCALA_VERSION 2.11
ENV KAFKA_HOME /opt/kafka
ENV PATH ${PATH}:${KAFKA_HOME}/bin

RUN apk add --update curl coreutils bash

RUN curl -sL http://www-us.apache.org/dist/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -o /tmp/kafka.tgz && \
  tar xzvf /tmp/kafka.tgz -C /opt && \
  rm /tmp/kafka.tgz && \
  mv /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION} ${KAFKA_HOME}

WORKDIR $KAFKA_HOME

ADD generate-conf.sh ${KAFKA_HOME}/bin/generate-conf.sh
ADD wrapper.sh ${KAFKA_HOME}/bin/wrapper.sh

CMD "${KAFKA_HOME}/bin/wrapper.sh"
