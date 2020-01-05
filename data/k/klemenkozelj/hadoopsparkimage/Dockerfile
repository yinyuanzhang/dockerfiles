FROM ubuntu:14.04
MAINTAINER klemen.kozelj@comtrade.com
MAINTAINER klemen.kozelj@gmail.com

# metadata
LABEL repository="klemenkozelj/hadoopsparkimage"
LABEL version="1.0"
LABEL description="https://github.com/KlemenKozelj/hadoopsparkimage, https://hub.docker.com/r/klemenkozelj/hadoopsparkimage"

USER root
WORKDIR /root
RUN echo 'root:password' | chpasswd

# update and upgrade ubuntu
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install nano

# installing Java
RUN apt-get -y install default-jre default-jdk
RUN echo export JAVA_HOME="$(update-alternatives --query java | grep 'Value: ' | grep -o '/.*/jre')" >> /root/.bashrc
RUN /bin/bash -c "source /root/.bashrc"

# SSH connection
EXPOSE 22
RUN apt-get -y install openssh-client openssh-server
RUN mkdir /root/.ssh
COPY ./Files/container.key* /root/.ssh/
RUN cat /root/.ssh/container.key.pub >> /root/.ssh/authorized_keys
RUN chmod -R 600 /root/.ssh
RUN echo "service ssh start &> /dev/null" >> /root/.bashrc
COPY ./Files/ssh-agent.sh /root/
RUN cat /root/ssh-agent.sh >> /root/.bashrc
RUN rm /root/ssh-agent.sh
RUN echo "ssh-add /root/.ssh/container.key &> /dev/null" >> /root/.bashrc
RUN /bin/bash -c "source /root/.bashrc"

# installing Hadoop
EXPOSE 50010 50020 50070 50075 50090 8020 9000 19888 8030 8031 8032 8033 8040 8042 8088 49707 2122
RUN mkdir /usr/local/hadoop
ADD http://www.apache.si/hadoop/core/hadoop-2.7.2/hadoop-2.7.2.tar.gz /root/
RUN tar -xzvf /root/hadoop-2.7.2.tar.gz
RUN cp -r /root/hadoop-2.7.2/* /usr/local/hadoop
RUN rm -rf /root/hadoop-2.7.2.tar.gz /root/hadoop-2.7.2
ENV HADOOP_HOME=/usr/local/hadoop

# installing Scala
RUN mkdir /usr/local/scala
ADD http://www.scala-lang.org/files/archive/scala-2.9.0.final.tgz /root/
RUN tar -xzvf /root/scala-2.9.0.final.tgz
RUN cp -r /root/scala-2.9.0.final/* /usr/local/scala
RUN rm -rf /root/scala-2.9.0.final.tgz /root/scala-2.9.0.final
ENV SCALA_HOME=/usr/local/scala

# installing Spark
EXPOSE 7077 8080 8081
RUN mkdir /usr/local/spark
ADD http://www.apache.si/spark/spark-1.6.1/spark-1.6.1-bin-hadoop2.6.tgz /root/
RUN tar -xzvf /root/spark-1.6.1-bin-hadoop2.6.tgz
RUN cp -r /root/spark-1.6.1-bin-hadoop2.6/* /usr/local/spark
RUN rm -rf /root/spark-1.6.1-bin-hadoop2.6.tgz /root/spark-1.6.1-bin-hadoop2.6
ENV SPARK_HOME=/usr/local/spark

# including Hadoop, Scala and Spartk to PATH variable
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SCALA_HOME/bin:$SPARK_HOME/bin