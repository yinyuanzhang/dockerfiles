FROM sainiajay/oraclejdk

MAINTAINER Ajay Saini <saini.ajay172@gmail.com>

USER root

ARG HADOOP_HOME=/usr/local/hadoop
ARG HADOOP_VER=2.9.1

# Install Hadoop
ENV HADOOP_HOME=$HADOOP_HOME \
    HADOOP_COMMON_HOME=$HADOOP_HOME \
    HADOOP_HDFS_HOME=$HADOOP_HOME \
    HADOOP_MAPRED_HOME=$HADOOP_HOME \
    HADOOP_YARN_HOME=$HADOOP_HOME \
    HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop \
    HDFS_NAMENODE_USER=root \
    HDFS_DATANODE_USER=root \
    HDFS_SECONDARYNAMENODE_USER=root \
    YARN_RESOURCEMANAGER_USER=root \
    YARN_NODEMANAGER_USER=root \
    PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

ADD https://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VER/hadoop-$HADOOP_VER.tar.gz /tmp
RUN tar -xzf /tmp/hadoop-$HADOOP_VER.tar.gz -C /usr/local/ \
&&  ln -s /usr/local/hadoop-$HADOOP_VER $HADOOP_HOME \
&&  mkdir $HADOOP_HOME/logs \
&&  rm -rf /tmp

#Passwordless SSH
RUN apk add --no-cache openssl openssh \
&&  ssh-keygen -qAN "" \
&&  ssh-keygen -qN "" -t rsa -f /root/.ssh/id_rsa \
&&  cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys \
&&  printf "\nStrictHostKeyChecking no\nUserKnownHostsFile /dev/null\nLogLevel QUIET\n" >> /etc/ssh/ssh_config

WORKDIR /home
