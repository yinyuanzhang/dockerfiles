FROM klustera/java8

# Basado en el ZooKeeper Docker de 47deg
MAINTAINER Adolfo De Unánue <adolfo@klustera.com>

ENV ZK_VERSION=3.4.8

RUN wget -q -O - http://mirror.vorboss.net/apache/zookeeper/zookeeper-${ZK_VERSION}/zookeeper-${ZK_VERSION}.tar.gz | tar -xzf - -C /opt
RUN mv /opt/zookeeper-${ZK_VERSION}/conf/zoo_sample.cfg /opt/zookeeper-${ZK_VERSION}/conf/zoo.cfg
RUN ln -s /opt/zookeeper-${ZK_VERSION} /opt/zookeeper

ENV JAVA_HOME /usr/jdk1.8.0_31
ENV ZK_HOME /opt/zookeeper
RUN sed  -i "s|/tmp/zookeeper|$ZK_HOME/data|g" $ZK_HOME/conf/zoo.cfg; mkdir $ZK_HOME/data

EXPOSE 2181 2888 3888

WORKDIR /opt/zookeeper
VOLUME ["/opt/zookeeper/conf", "/opt/zookeeper/data"]

ENTRYPOINT ["/opt/zookeeper/bin/zkServer.sh"]

CMD ["start-foreground"]
