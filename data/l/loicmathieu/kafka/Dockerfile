#############################################################################################
# This dockerfile will install kafka 0.9.0.1 from CDH 5.5.2 repo
#
############################################################################################
FROM loicmathieu/openjdk

MAINTAINER Loic Mathieu <loicmathieu@free.fr>

ENV SCALA_VERSION 2.11
ENV KAFKA_VERSION 0.10.1.0
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"

#copy cloudera CDH repo because zookeeper is in none of the default yum repos
COPY cloudera-cdh-5.5.2.repo /etc/yum.repos.d

#Install epel repo because supervisor isn't in the base repo
RUN yum -y install epel-release && rm -rf /var/cache/yum/*

#Install wget, zookeeper and supervisor
RUN yum -y install supervisor  zookeeper wget &&  rm -rf /var/cache/yum/*

#Install kafka
RUN wget -q http://apache.mirrors.spacedump.net/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \
    tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt && \
    rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
 
#add kafka start script 
COPY start-kafka.sh /usr/bin/start-kafka.sh
RUN chmod +x /usr/bin/start-kafka.sh

# Supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# 2181 is zookeeper, 9092 is kafka
EXPOSE 2181 9092

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
