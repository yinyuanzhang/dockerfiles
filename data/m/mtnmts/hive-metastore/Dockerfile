FROM debian:latest 

USER root

ENV HIVE_VER 2.3.5
ENV CONNECTOR_VERSION 2.4.1
ENV HIVE_HOME /opt/hive
ENV HIVE_CONF_DIR $HIVE_HOME/conf
ENV HIVE_SERVER2_THRIFT_BIND_HOST "0.0.0.0"

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends  openjdk-8-jre-headless ca-certificates-java \
    && rm -rf /var/lib/apt/lists/*
    
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends net-tools curl

ENV HADOOP_VERSION 2.7.2
ENV HADOOP_URL https://archive.apache.org/dist/hadoop/core/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz

RUN set -x \
    && curl -fSL "$HADOOP_URL" -o /tmp/hadoop.tar.gz \
    && curl -fSL "$HADOOP_URL.asc" -o /tmp/hadoop.tar.gz.asc \
    && tar -xvf /tmp/hadoop.tar.gz -C /opt/ \
    && rm /tmp/hadoop.tar.gz*
    
RUN ln -s /opt/hadoop-$HADOOP_VERSION/etc/hadoop /etc/hadoop
RUN cp /etc/hadoop/mapred-site.xml.template /etc/hadoop/mapred-site.xml
RUN mkdir /opt/hadoop-$HADOOP_VERSION/logs

RUN mkdir /hadoop-data

ENV HADOOP_PREFIX=/opt/hadoop-$HADOOP_VERSION
ENV HADOOP_CONF_DIR=/etc/hadoop
ENV MULTIHOMED_NETWORK=1

ENV USER=root
ENV PATH $HADOOP_PREFIX/bin/:$PATH

RUN apt-get update
RUN apt-get install -y --no-install-recommends wget postgresql 
RUN wget https://www-us.apache.org/dist/hive/hive-$HIVE_VER/apache-hive-$HIVE_VER-bin.tar.gz 
RUN tar -xvf apache-hive-$HIVE_VER-bin.tar.gz; mv apache-hive-$HIVE_VER-bin $HIVE_HOME
RUN wget https://downloads.mariadb.com/Connectors/java/connector-java-$CONNECTOR_VERSION/mariadb-java-client-$CONNECTOR_VERSION.jar -O /opt/hive/jdbc/mariadb-jdbc.jar
RUN cp /opt/hive/jdbc/mariadb-jdbc.jar /opt/hive/lib/
ENV HADOOP_HOME $HADOOP_PREFIX
ENV HADOOP_HEAPSIZE=4096

RUN curl https://downloads.alluxio.io/downloads/files/1.8.1/alluxio-1.8.1-hadoop-2.9-bin.tar.gz -o /tmp/presto.tar.gz
RUN cd /tmp && tar -xzf /tmp/presto.tar.gz
RUN ls -laR /tmp/
RUN cp /tmp/alluxio-1.8.1-hadoop-2.9/client/alluxio-1.8.1-client.jar /opt/hive/lib/


ENTRYPOINT ["/opt/hive/bin/hive", "--service","metastore"]

