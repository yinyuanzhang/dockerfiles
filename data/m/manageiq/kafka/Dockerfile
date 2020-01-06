FROM centos
ENV WORKDIR /opt/kafka/
WORKDIR $WORKDIR
RUN mkdir -p $WORKDIR \
  && cd $WORKDIR \
  && yum -y install java-1.8.0-openjdk-headless tar \
  && curl -s https://www.mirrorservice.org/sites/ftp.apache.org/kafka/2.0.0/kafka_2.12-2.0.0.tgz | tar -xz --strip-components=1 \
  && yum clean all
RUN chmod -R a=u $WORKDIR
VOLUME /tmp/kafka-logs /tmp/zookeeper
EXPOSE 2181 2888 3888 9092
