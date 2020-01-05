FROM python:3.6-alpine 
MAINTAINER BY "Daniel Paes danspaes@gmail.com"

ENV SPARK_VERSION=2.3.1
ENV SPARK_HOME=/opt/spark-$SPARK_VERSION
ENV HADOOP_VERSION=2.7

ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

WORKDIR /opt

RUN apk add --no-cache bash && \
    wget "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
    tar xzf "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
    mv "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}" "spark-${SPARK_VERSION}" && \
    rm "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"


