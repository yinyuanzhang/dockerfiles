#
# Spark and Hadoop Standalone Container
# Apache Spark 2.4.4, Hadoop 2.6
#
# Runs a small Spark standalone cluster and a pseudo distributed Hadoop cluster in a container
# Suitable for building test/development containers for Spark apps interacting with HDFS
#
# Takes some time to start HDFS, in scripts you can use sleep 30
#
# Usage:
# $ docker build -t mgabr/sparklet-hdfs:2.4.4 .
# $ docker run -p 8080:8080 -p 50070:50070 -it mgabr/sparklet-hdfs:2.4.4

FROM uncharted/sparklet:2.4.4
LABEL author="Markus Gabriel"

# hadoop web admin ports
EXPOSE 50070

RUN \
  # generate host keys
  ssh-keygen -A && \
  curl https://archive.apache.org/dist/hadoop/common/hadoop-2.6.5/hadoop-2.6.5.tar.gz > hadoop.tar.gz && \
  # extract hadoop
  tar -xzf hadoop.tar.gz && \
  # cleanup hadoop tarball
  rm hadoop.tar.gz

# add ssh config to disable host key checking
ADD config/ssh-config /root/.ssh/config

# add hadoop config
ADD config/core-site.xml /opt/hadoop-2.6.5/etc/hadoop/core-site.xml
ADD config/hdfs-site.xml /opt/hadoop-2.6.5/etc/hadoop/hdfs-site.xml

# fix JAVA_HOME not found in hadoop
RUN echo "export JAVA_HOME="$JAVA_HOME >> /opt/hadoop-2.6.5/etc/hadoop/hadoop-env.sh

# upload init scripts
ADD services/hadoop-init /etc/cont-init.d/hadoop
ADD services/spark-slave3-run /etc/services.d/spark-slave3/run
ADD services/spark-slave4-run /etc/services.d/spark-slave4/run

ENV HADOOP_CONF_DIR /opt/hadoop-2.6.5/etc/hadoop
ENV PATH /opt/hadoop-2.6.5/bin:/opt/hadoop-2.6.5/sbin:$PATH

ENTRYPOINT [ "/init" ]

CMD ["spark-shell"]