FROM centos
RUN mkdir -p /opt/kafka \
  && cd /opt/kafka \
  && yum -y install java-1.8.0-openjdk-headless tar \
  && curl -s https://archive.apache.org/dist/kafka/0.11.0.1/kafka_2.12-0.11.0.1.tgz | tar -xz --strip-components=1 \
  && yum clean all
RUN chmod -R a=u /opt/kafka
WORKDIR /opt/kafka
VOLUME /tmp/kafka-logs /tmp/zookeeper
EXPOSE 2181 2888 3888 9092
