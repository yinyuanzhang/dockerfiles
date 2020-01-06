# Apache Kafka

FROM openjdk:8-jre-alpine

MAINTAINER ogergardt

RUN \
  apk update
RUN \
  apk add --no-cache \
  wget \
  bash \
  curl \
  jq 

ARG ZOOKEEPER_VERSION=3.4.10

LABEL name="zookeeper" version=${ZOOKEEPER_VERSION}

ENV ZOOKEEPER_HOME /opt/zookeeper-${ZOOKEEPER_VERSION}
ENV PATH ${PATH}:${ZOOKEEPER_HOME}/bin

ADD start.sh ${ZOOKEEPER_HOME}/bin/start.sh
RUN chmod +x ${ZOOKEEPER_HOME}/bin/start.sh

ADD download.sh /tmp/download.sh
RUN chmod a+x /tmp/download.sh \
  && sync && /tmp/download.sh \
  && tar xfz /tmp/zookeeper-${ZOOKEEPER_VERSION}.tar.gz -C /opt \
  && rm /tmp/zookeeper-${ZOOKEEPER_VERSION}.tar.gz \
  && chown -R root:root $ZOOKEEPER_HOME
RUN mv $ZOOKEEPER_HOME/conf/zoo_sample.cfg $ZOOKEEPER_HOME/conf/zoo.cfg \
  && sed  -i "s|/tmp/zookeeper|$ZOOKEEPER_HOME/data|g" $ZOOKEEPER_HOME/conf/zoo.cfg; mkdir $ZOOKEEPER_HOME/data

EXPOSE 2181 2888 3888

RUN mkdir /var/lib/zookeeper && mkdir /var/log/zookeeper 

EXPOSE 2181 2888 3888

VOLUME ["/var/lib/zookeeper", "/var/log/zookeeper"]

ENTRYPOINT ["start.sh"]
