FROM mesosphere/mesos-slave:1.7.1
LABEL maintainer="support@arukas.io"

ENV HADOOP_VERSION 2.8.5
ENV JAVA_HOME /usr
ENV HADOOP_HOME /usr/hadoop-${HADOOP_VERSION}
ENV HADOOP_CLASSPATH /usr/hadoop-${HADOOP_VERSION}/share/hadoop/tools/lib/*

RUN mkdir ${HADOOP_HOME} && \
    apt-get update -qq && \
    # Hadoop does not support Java 9+ or later.
    apt-get install -y openjdk-8-jre-headless && \
    apt-get remove -y openjdk-9-jre-headless && \
    ln -sf /usr/lib/jvm/java-8-openjdk-amd64/bin/java /etc/alternatives/java && \
    rm -rf /var/lib/apt/lists/* && \
    curl -o /tmp/hadoop.tar.gz http://ftp.riken.jp/net/apache/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    /bin/bash -c 'tar xvf /tmp/hadoop.tar.gz --directory ${JAVA_HOME} hadoop-${HADOOP_VERSION}/{bin,etc,include,lib,libexec,share/hadoop/common,share/hadoop/tools/lib}' && \
    rm /tmp/hadoop.tar.gz

ENTRYPOINT ["mesos-slave"]
