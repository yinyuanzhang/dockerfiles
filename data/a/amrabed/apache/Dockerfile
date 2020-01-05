# Creates an image with Apache Hadoop 2.6.0, Hive 0.14.0, and Giraph 1.2.0 installed on Ubuntu 14.10

FROM amrabed/hadoop

MAINTAINER Amr Abed

USER root

WORKDIR /usr/local

# Install pre-requisites
RUN apt-get install -y git maven

# Install Hive
RUN curl -s http://www.us.apache.org/dist/hive/stable/apache-hive-0.14.0-bin.tar.gz | tar -xz && \
    mv apache-hive-0.14.0-bin hive

# Install & build Giraph 1.2.0 (unreleased)
RUN git clone -b trunk https://github.com/apache/giraph.git && \
    cd giraph && mvn -U -Phadoop_2 package -DskipTests

# Install Zookeeper
RUN curl -s http://www.us.apache.org/dist/zookeeper/stable/zookeeper-3.4.6.tar.gz | tar -xz && \
    mv zookeeper-3.4.6 zookeeper

# Set Environment variables
ENV PATH $PATH:/usr/local/hive/bin:/usr/local/giraph/bin:/usr/local/zookeeper/bin

WORKDIR /
