FROM openjdk:8-jdk

ENV SPARK_VERSION=1.6.3
ENV HADOOP_VERSION=2.6

RUN curl https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz | tar xz -C /usr/local

ENV PATH="${PATH}:/usr/local/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/bin"

