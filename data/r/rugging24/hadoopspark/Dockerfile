FROM debian:stretch
ARG RSYNC_PASSWORD='root'
RUN apt-get update && apt-get install -y apt-utils build-essential \
    checkinstall default-jdk default-jre wget sudo vim openssh-server \
    libreadline-gplv2-dev libncursesw5-dev libssl-dev tar sshpass \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev \
    rsync

RUN wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz && tar xzf /Python-3.7.4.tgz

RUN cd /Python-3.7.4 && ./configure --prefix=/usr/local/python-37 --enable-optimizations \
    && make altinstall && cd && rm -rf /Python-3.7.4 && rm /Python-3.7.4.tgz

RUN ln -s /usr/local/python-37/bin/python3.7 /usr/bin/python && \
    ln -s /usr/local/python-37/bin/pip3.7 /usr/bin/pip

RUN  groupadd -g 1020 hadoop && useradd -g 1020 -u 1020 -d /home/hadoop -s /bin/bash  -m -p hadoop hadoop

RUN adduser hadoop sudo

RUN su hadoop -c 'ssh-keygen -t rsa -N "" -f /home/hadoop/.ssh/id_rsa -q'
RUN cat /home/hadoop/.ssh/id_rsa.pub >> /home/hadoop/.ssh/authorized_keys

RUN chown -R hadoop:hadoop /home/hadoop/.ssh && chmod 600 /home/hadoop/.ssh/*

RUN wget http://apache.lauf-forum.at/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz
RUN tar -xzf /hadoop-3.1.2.tar.gz && rm /hadoop-3.1.2.tar.gz
RUN mv /hadoop-3.1.2 /home/hadoop/hadoop

RUN wget http://apache.lauf-forum.at/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz
RUN tar -xzf /spark-2.4.3-bin-hadoop2.7.tgz && rm /spark-2.4.3-bin-hadoop2.7.tgz
RUN mv /spark-2.4.3-bin-hadoop2.7 /home/hadoop/spark


ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre

RUN touch /home/hadoop/.profile
RUN echo PATH=/home/hadoop/hadoop/bin:/home/hadoop/hadoop/sbin:/home/hadoop/spark/bin:${PATH} > /home/hadoop/.profile
RUN echo JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre >> /home/hadoop/.profile
RUN chown hadoop:hadoop /home/hadoop/.profile
RUN echo "export JAVA_HOME=${JAVA_HOME}" >> /home/hadoop/hadoop/etc/hadoop/hadoop-env.sh
ADD *.xml /home/hadoop/hadoop/etc/hadoop/

RUN chown -R hadoop:hadoop /home/hadoop/hadoop
RUN chown -R hadoop:hadoop /home/hadoop/hadoop/*
RUN chown -R hadoop:hadoop /home/hadoop/spark
RUN chown -R hadoop:hadoop /home/hadoop/spark/*
RUN mkdir /root/.ssh

RUN echo "PermitRootLogin   yes" >> /etc/ssh/sshd_config
RUN echo "PasswordAuthentication  no" >> /etc/ssh/sshd_config
RUN echo "StrictModes  no" >> /etc/ssh/sshd_config
RUN echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config

RUN echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf

ENV HDFS_NAMENODE_USER="hadoop"
ENV HDFS_DATANODE_USER="hadoop"
ENV HDFS_SECONDARYNAMENODE_USER="hadoop"
ENV YARN_RESOURCEMANAGER_USER="hadoop"
ENV YARN_NODEMANAGER_USER="hadoop"

ENV HADOOP_CONF_DIR="/home/hadoop/hadoop/etc/hadoop"
ENV SPARK_HOME="/home/hadoop/spark"
ENV LD_LIBRARY_PATH="/home/hadoop/hadoop/lib/native:${LD_LIBRARY_PATH}"

RUN mv "${SPARK_HOME}"/conf/spark-defaults.conf.template "${SPARK_HOME}"/conf/spark-defaults.conf
RUN echo "spark.master    yarn" >> "${SPARK_HOME}"/conf/spark-defaults.conf
RUN echo "spark.driver.memory    512m" >> "${SPARK_HOME}"/conf/spark-defaults.conf
RUN echo "spark.executor.memory      512m" >> "${SPARK_HOME}"/conf/spark-defaults.conf
# spark.yarn.am.memory    512m
ADD run_master.sh /run_master.sh
RUN chmod a+x /run_master.sh

EXPOSE 9000 50070 50470 8020 50075 9870 22

ENTRYPOINT [ "/run_master.sh" ]
