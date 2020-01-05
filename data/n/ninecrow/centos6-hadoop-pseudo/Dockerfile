FROM ninecrow/centos6-jdk8:1.0.0

USER root

RUN yum update -y; \
	yum install -y vim rsync net-tools

ARG HADOOP_VERSION=2.7.6 
ENV HADOOP_URL=https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz
ARG HADOOP_FILE_NAME=hadoop-${HADOOP_VERSION}.tar.gz
ARG HADOOP_SHA=F2327EA93F4BC5A5D7150DEE8E0EDE196D3A77FF8526A7DD05A48A09AAE25669

WORKDIR /tmp
#RUN wget "$HADOOP_URL" -O /tmp/hadoop.tar.gz
#调试时候使用本地文件copy到image
#COPY hadoop-2.7.6.tar.gz /tmp/${HADOOP_FILE_NAME}
RUN sudo wget http://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-${HADOOP_VERSION}/${HADOOP_FILE_NAME} \
	&& sudo echo "${HADOOP_SHA}  ${HADOOP_FILE_NAME}">/tmp/${HADOOP_FILE_NAME}.sha \
	&& sudo sha256sum -c /tmp/${HADOOP_FILE_NAME}.sha \
	&& tar -xzf /tmp/${HADOOP_FILE_NAME} -C /opt/ \
	&& rm -f /tmp/${HADOOP_FILE_NAME}* \
	&& mkdir /opt/hadoop-$HADOOP_VERSION/logs \
	&& mkdir /hadoop-data

ENV HADOOP_PREFIX /opt/hadoop-$HADOOP_VERSION
ENV HADOOP_HOME /opt/hadoop-$HADOOP_VERSION
ENV HADOOP_COMMON_HOME /opt/hadoop-$HADOOP_VERSION
ENV HADOOP_HDFS_HOME /opt/hadoop-$HADOOP_VERSION
ENV HADOOP_MAPRED_HOME /opt/hadoop-$HADOOP_VERSION
ENV HADOOP_YARN_HOME /opt/hadoop-$HADOOP_VERSION
ENV HADOOP_CONF_DIR /opt/hadoop-$HADOOP_VERSION/etc/hadoop
#ENV YARN_CONF_DIR $HADOOP_HOME/etc/hadoop

WORKDIR ${HADOOP_HOME}
#sed命令替换hadoop-env.sh中的环境变量的值
RUN sed -i '/^export JAVA_HOME/ s:.*:export JAVA_HOME=/opt/soft/java/jdk/jdk1.8.0_161\n:' $HADOOP_HOME/etc/hadoop/hadoop-env.sh \
	&& sed -i '/^export HADOOP_CONF_DIR/ s:.*:export HADOOP_CONF_DIR=/opt/hadoop-2.7.6/etc/hadoop\n:' $HADOOP_HOME/etc/hadoop/hadoop-env.sh
#添加用户配置，否则启动start-dfs.sh, start-yarn.sh 失败
#RUN sed -i '/^#.export HDFS_NAMENODE_USER/ s:.*:export HDFS_NAMENODE_USER=root\nexport HDFS_DATANODE_USER=root\nexport HDFS_SECONDARYNAMENODE_USER=root\nexport YARN_RESOURCEMANAGER_USER=root\nexport YARN_NODEMANAGER_USER=root\n:' $HADOOP_HOME/etc/hadoop/hadoop-env.sh

#复制配置文件
ADD core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
ADD hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml
ADD mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml
ADD yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml

# 初始namenode , this is locally step 1;
# RUN $HADOOP_HOME/bin/hdfs namenode -format

# If you cannot ssh to localhost without a passphrase, execute the following commands
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa \
	&& cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
	&& chmod 0600 ~/.ssh/authorized_keys



ADD bootstrap.sh /etc/bootstrap.sh
RUN chown root:root /etc/bootstrap.sh \
	&& chmod 700 /etc/bootstrap.sh

ENV BOOTSTRAP /etc/bootstrap.sh



CMD ["/etc/bootstrap.sh"]

# Hdfs ports
EXPOSE 50010 50020 50070 50075 50090 8020 9000
# Mapred ports
EXPOSE 10020 19888
#Yarn ports
EXPOSE 8030 8031 8032 8033 8040 8042 8088
#Other ports
EXPOSE 49707 22 
