FROM alpine
MAINTAINER Channel IT Services, LLC

ENV	HADOOP_VER=3.1.1
ENV HADOOP_HOME=/home/hadoop/hadoop
ENV HADOOP_INSTALL=$HADOOP_HOME
ENV HADOOP_MAPRED_HOME=$HADOOP_HOME
ENV HADOOP_COMMON_HOME=$HADOOP_HOME
ENV HADOOP_HDFS_HOME=$HADOOP_HOME
ENV YARN_HOME=$HADOOP_HOME
ENV HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
ENV PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
ENV	HADOOP_OPTS=-Djava. &&\library.path=/home/hadoop/lib/native
ENV JAVA_HOME=/usr/lib/jvm/default-jvm


RUN\
	apk -U update && \
	apk add bash curl openssh-client wget openssl openjdk8-jre supervisor && \
	addgroup hadoop &&\
	adduser --ingroup hadoop hadoop &&\
	usermod -aG sudo hadoop &&\
	su - hadoop &&\
	ssh-keygen -t rsa -f /root/.ssh/id_rsa &&\
	cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys &&\
	chmod 0600 ~/.ssh/authorized_keys &&\
	cd ~ &&\
	wget http://apache.cs.utah.edu/hadoop/common/hadoop-$HADOOP_VER/hadoop-$HADOOP_VER.tar.gz &&\
	tar xzvf hadoop-$HADOOP_VER.tar.gz &&\
	mv hadoop-$HADOOP_VER $HADOOP_HOME &&\
	rm hadoop-$HADOOP_VER.tar.gz

RUN\
    mkdir -p /home/hadoop/logs &&\
	wget -q https://raw.githubusercontent.com/channelit/docker-images/master/hadoop/core-site.xml -O $HADOOP_HOME/etc/hadoop/core-site.xml &&\
	wget -q https://raw.githubusercontent.com/channelit/docker-images/master/hadoop/hdfs-site.xml -O $HADOOP_HOME/etc/hadoop/hdfs-site.xml &&\
	wget -q https://raw.githubusercontent.com/channelit/docker-images/master/hadoop/mapred-site.xml -O $HADOOP_HOME/etc/hadoop/mapred-site.xml &&\
	wget -q https://raw.githubusercontent.com/channelit/docker-images/master/hadoop/yarn-site.xml -O $HADOOP_HOME/etc/hadoop/yarn-site.xml &&\
	wget -q https://raw.githubusercontent.com/channelit/docker-images/master/hadoop/start.sh -O $HADOOP_HOME/start.sh &&\
	chmod 755 $HADOOP_HOME/start.sh &&\
	sed -i '/^export JAVA_HOME/ s:.*:export JAVA_HOME=/usr/lib/jvm/default-java\nexport HADOOP_HOME=/home/hadoop/hadoop\n:' $HADOOP_HOME/etc/hadoop/hadoop-env.sh &&\
	sed -i '/^export HADOOP_CONF_DIR/ s:.*:export HADOOP_CONF_DIR=/home/hadoop/hadoop/etc/hadoop/:' $HADOOP_HOME/etc/hadoop/hadoop-env.sh &&\
	sed -i '/^export HADOOP_OPTS/ s:.*:export HADOOP_OPTS=-Djava.net.preferIPv4Stack=true:' $HADOOP_HOME/etc/hadoop/hadoop-env.sh &&\
	mkdir -p /data/dfs/data /data/dfs/name /data/dfs/namesecondary &&\
	chown -R .hadoop /data &&\
    hdfs namenode -format
VOLUME /data

EXPOSE 9000 50070 50010 50020 50075 50090 8088
#CMD ["./home/hadoop/hadoop/start.sh"]
