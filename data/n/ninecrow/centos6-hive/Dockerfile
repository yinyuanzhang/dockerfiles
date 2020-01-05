FROM ninecrow/centos6-hadoop-cluster:1.0.0
MAINTAINER ninecrow <ninecrow@yeah.net>

ENV HIVE_HOME=/opt/hive
ARG MYSQL_CONNECT_VERSION=5.1.39

USER root
RUN sudo echo "export HIVE_HOME=${HIVE_HOME}" >> /etc/profile

USER hadoop
#COPY apache-hive-1.2.2-bin.tar.gz /tmp/hive.tar.gz
RUN sudo wget http://mirror.bit.edu.cn/apache/hive/hive-1.2.2/apache-hive-1.2.2-bin.tar.gz -O /tmp/hive.tar.gz \
	&& sudo wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_CONNECT_VERSION}.tar.gz -O /tmp/mysql-connector-java-${MYSQL_CONNECT_VERSION}.tar.gz \
	&& sudo mkdir -p ${HIVE_HOME} \
	&& sudo tar -xvf /tmp/hive.tar.gz -C ${HIVE_HOME} --strip-components=1  \
	&& sudo tar -xvf /tmp/mysql-connector-java-${MYSQL_CONNECT_VERSION}.tar.gz -C ${HIVE_HOME}/lib --strip-components=1  mysql-connector-java-${MYSQL_CONNECT_VERSION}/mysql-connector-java-${MYSQL_CONNECT_VERSION}-bin.jar \
	&& sudo rm /tmp/hive.tar.gz \
	&& sudo chown -R hadoop:root ${HIVE_HOME} 

RUN sudo cp ${HIVE_HOME}/conf/hive-env.sh.template ${HIVE_HOME}/conf/hive-env.sh \
	&& sudo cp ${HIVE_HOME}/conf/beeline-log4j.properties.template ${HIVE_HOME}/conf/beeline-log4j.properties \
	&& sudo cp ${HIVE_HOME}/conf/hive-exec-log4j.properties.template ${HIVE_HOME}/conf/hive-exec-log4j.properties \
	&& sudo cp ${HIVE_HOME}/conf/hive-log4j.properties.template ${HIVE_HOME}/conf/hive-log4j.properties

ADD hive-site.xml ${HIVE_HOME}/conf/hive-site.xml

ADD entrypoint.sh /entrypoint.sh
RUN sudo chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
