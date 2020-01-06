FROM hegand/jdk:openjdk8

ENV HADOOP_VERSION 3.1.2
ENV HADOOP_MAJOR_VERSION 3.1
ENV HADOOP_FULL_VERSION hadoop-${HADOOP_VERSION}
ENV HADOOP_HOME /usr/local/hadoop
ENV HADOOP_CONF_DIR ${HADOOP_HOME}/conf
ENV HADOOP_OPTS	-Djava.library.path=$HADOOP_HOME/lib/native
ENV PATH $PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

RUN apk add --update --no-cache bash

RUN adduser -D -s /bin/bash -u 1100 hadoop

RUN set -x \
        && mkdir -p /usr/local \
        && cd /tmp \
        && wget http://archive.apache.org/dist/hadoop/core/${HADOOP_FULL_VERSION}/${HADOOP_FULL_VERSION}.tar.gz  -O - | tar -xz \
        && mv ${HADOOP_FULL_VERSION} /usr/local \
        && ln -s /usr/local/${HADOOP_FULL_VERSION} ${HADOOP_HOME} \
        && rm -rf ${HADOOP_HOME}/share/doc \
        && chown -R hadoop:hadoop  ${HADOOP_HOME}/
        
RUN mkdir -p /data \
    && chown -R hadoop:hadoop /data

WORKDIR ${HADOOP_HOME}
