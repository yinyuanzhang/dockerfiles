FROM openjdk:8-jdk

ENV HADOOP_VERSION=2.6.5

RUN curl http://apache.dattatec.com/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz | tar xz -C /usr/local

ENV PATH="${PATH}:/usr/local/hadoop-${HADOOP_VERSION}/bin"
