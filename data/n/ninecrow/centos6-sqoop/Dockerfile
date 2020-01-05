FROM ninecrow/centos6-hadoop-cluster:1.0.0
MAINTAINER ninecrow <ninecrow@yeah.net>

ENV SQOOP_HOME=/opt/sqoop
ARG MYSQL_CONNECT_VERSION=5.1.39
#ARG SQOOP_VERSION=1.4.7

USER root
RUN sudo echo "export SQOOP_SERVER_EXTRA_LIB=${SQOOP_HOME}/lib" >> /etc/profile

USER hadoop
#COPY sqoop-1.99.7-bin-hadoop200.tar.gz /tmp/sqoop.tar.gz
#COPY mysql-connector-java-5.1.39-bin.jar /tmp/mysql-connector-java-5.1.39-bin.jar
RUN sudo wget https://mirrors.tuna.tsinghua.edu.cn/apache/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz -O /tmp/sqoop.tar.gz \
	&& sudo wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_CONNECT_VERSION}.tar.gz -O /tmp/mysql-connector-java-${MYSQL_CONNECT_VERSION}.tar.gz \
	## tar 提取jar文件
	&& sudo mkdir -p ${SQOOP_HOME} \
	&& sudo tar -xvf /tmp/sqoop.tar.gz -C ${SQOOP_HOME} --strip-components=1  \
	&& sudo rm /tmp/sqoop.tar.gz \
 	&& sudo tar -xvf /tmp/mysql-connector-java-${MYSQL_CONNECT_VERSION}.tar.gz -C ${SQOOP_HOME}/lib --strip-components=1  mysql-connector-java-${MYSQL_CONNECT_VERSION}/mysql-connector-java-${MYSQL_CONNECT_VERSION}-bin.jar \
	#WORKDIR $SQOOP_HOME
	#修改hadoop的配置文件权限，因为sqoop2_tools verify 因为权限不足报错
	&& sudo chown -R hadoop:root ${SQOOP_HOME} \
	&& sudo chmod 775 ${HADOOP_HOME}/etc/hadoop 


#以下配置是sqoop2的 ，暂时隐去;
#替换sqoop.sh文件中的hadoop相关环境变量设置值;
#example sed -i 's:^.*HADOOP_YARN_HOME=.*$:  HADOOP_YARN_HOME=${HADOOP_HOME}/share/hadoop/common:' $SQOOP_HOME/bin/sqoop.sh
#RUN sed -i 's:^.*HADOOP_COMMON_HOME=.*$:  HADOOP_COMMON_HOME=${HADOOP_HOME}/share/hadoop/common:' ${SQOOP_HOME}/bin/sqoop.sh \
#	&& sed -i 's:^.*HADOOP_HDFS_HOME=.*$:  HADOOP_HDFS_HOME=${HADOOP_HOME}/share/hadoop/hdfs:' ${SQOOP_HOME}/bin/sqoop.sh \
#	&& sed -i 's:^.*HADOOP_MAPRED_HOME=.*$:  HADOOP_MAPRED_HOME=${HADOOP_HOME}/share/hadoop/mapreduce:' ${SQOOP_HOME}/bin/sqoop.sh \
#	&& sed -i 's:^.*HADOOP_YARN_HOME=.*$:  HADOOP_YARN_HOME=${HADOOP_HOME}/share/hadoop/yarn\n:' ${SQOOP_HOME}/bin/sqoop.sh \
	#替换container-executor.cfg文件内容，hadoop集群相关设置也需要更新；
#	&& sed -i '/^allowed.system.user=/ s:.*:allowed.system.users=root,hadoop\n:' ${HADOOP_HOME}/etc/hadoop/container-executor.cfg \
	#修改Hadoop配置文件
#	&& sed -i '/^org.apache.sqoop.submission.engine.mapreduce.configuration.directory=/ s:.*:org.apache.sqoop.submission.engine.mapreduce.configuration.directory=/opt/hadoop-2.7.6/etc/hadoop\n:' ${SQOOP_HOME}/conf/sqoop.properties
#EXPOSE 12000 9000

ADD entrypoint.sh /entrypoint.sh
RUN sudo chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
