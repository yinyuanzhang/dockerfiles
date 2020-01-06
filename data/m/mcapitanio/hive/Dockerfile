FROM mcapitanio/hadoop

MAINTAINER Matteo Capitanio <matteo.capitanio@gmail.com>

USER root

ENV HIVE_VER 2.1.1

ENV HIVE_HOME /opt/hive
ENV HIVE_CONF_DIR $HIVE_HOME/conf
ENV HADOOP_HOME /opt/hadoop
ENV HADOOP_CONF_DIR /opt/hadoop/etc/hadoop
ENV HCAT_LOG_DIR /opt/hive/logs
ENV HCAT_PID_DIR /opt/hive/logs
ENV WEBHCAT_LOG_DIR /opt/hive/logs
ENV WEBHCAT_PID_DIR /opt/hive/logs

ENV PATH $HIVE_HOME/bin:$PATH

# Install needed packages
RUN yum clean all; \
    yum update -y; \
    yum install -y python-setuptools postgresql; \
    yum clean all
RUN easy_install supervisor

WORKDIR /opt/docker

# Apache Hive
RUN wget http://apache.panu.it/hive/hive-$HIVE_VER/apache-hive-$HIVE_VER-bin.tar.gz
RUN tar -xvf apache-hive-$HIVE_VER-bin.tar.gz -C ..; \
    mv ../apache-hive-$HIVE_VER-bin $HIVE_HOME
RUN wget https://jdbc.postgresql.org/download/postgresql-9.4.1209.jre7.jar -O $HIVE_HOME/lib/postgresql-9.4.1209.jre7.jar
COPY hive/ $HIVE_HOME/
COPY ./etc /etc

RUN chmod +x $HIVE_HOME/bin/*.sh

RUN useradd -p $(echo "hive" | openssl passwd -1 -stdin) hive; \
    usermod -a -G supergroup hive; \
    usermod -a -G hdfs hive;

EXPOSE 9083 10000 10002 50111

VOLUME ["/opt/hive/conf", "/opt/hive/logs"]

ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
