FROM gettyimages/spark:2.3.1-hadoop-3.0
LABEL maintainer="EECS York University <eecs.lassonde.yorku.ca>"

RUN apt-get update
RUN apt-get -y install nano curl openssh-server openssh-client

RUN pip install requests



# passwordless ssh
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key
#RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys


ADD ssh_config /root/.ssh/config
RUN chmod 600 /root/.ssh/config
RUN chown root:root /root/.ssh/config



ENV JAVA_HOME /usr/java

ENV HADOOP_HOME /usr/hadoop-3.0.0
ENV HADOOP_COMMON_HOME /usr/hadoop-3.0.0
ENV HADOOP_HDFS_HOME /usr/hadoop-3.0.0
ENV HADOOP_MAPRED_HOME /usr/hadoop-3.0.0
ENV HADOOP_YARN_HOME /usr/hadoop-3.0.0
ENV HADOOP_CONF_DIR $HADOOP_HOME/etc/hadoop

ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV HDFS_SECONDARYNAMENODE_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root

ADD core-site.xml $HADOOP_CONF_DIR/core-site.xml
ADD hdfs-site.xml $HADOOP_CONF_DIR/hdfs-site.xml
ADD mapred-site.xml $HADOOP_CONF_DIR/mapred-site.xml
ADD yarn-site.xml $HADOOP_CONF_DIR/yarn-site.xml
RUN sed -i "s|# export JAVA_HOME=|export JAVA_HOME=/usr/java|g" $HADOOP_CONF_DIR/hadoop-env.sh

RUN $HADOOP_HOME/bin/hdfs namenode -format

# fix the 254 error code
RUN sed  -i "/^[^#]*UsePAM/ s/.*/#&/"  /etc/ssh/sshd_config
RUN echo "UsePAM no" >> /etc/ssh/sshd_config
RUN echo "Port 2122" >> /etc/ssh/sshd_config

RUN mkdir /app
WORKDIR /app

ENTRYPOINT service ssh start && /usr/hadoop-3.0.0/sbin/start-all.sh && bash


# Hdfs ports
EXPOSE 9820 9865 9866 9867 9868 9869 9870 9871 9000
# Mapred ports
EXPOSE 10020 19888
#Yarn ports
EXPOSE 8030 8031 8032 8033 8040 8042 8088
#Other ports
EXPOSE 49707 2122
