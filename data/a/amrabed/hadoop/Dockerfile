# Creates an image with Oracle Java 8 and Hadoop 2.6.0 installed on Ubuntu

FROM ubuntu

MAINTAINER Amr Abed

USER root

# Install Oracle java 8
RUN apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections && \
    apt-get install -y oracle-java8-installer 

# Install Hadoop 2.6.0
WORKDIR /usr/local
RUN apt-get install -y curl && \
    curl -s http://www.us.apache.org/dist/hadoop/common/current/hadoop-2.6.0.tar.gz | tar -xz && \
    mv hadoop-2.6.0 hadoop

# Install OpenSSH
RUN apt-get install -y openssh-server

# Enable SSH connection to localhost without passphrase
RUN ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa && \
    cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys && \
    echo 'Host *\n  UserKnownHostsFile /dev/null\n  StrictHostKeyChecking no' > ~/.ssh/config

# Set environment variables
ENV PATH $PATH:/usr/local/hadoop/bin:/usr/local/hadoop/sbin
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV HADOOP_HOME /usr/local/hadoop
ENV HADOOP_PREFIX /usr/local/hadoop

# Configure Hadoop for running a MapReduce job on YARN in a pseudo-distributed mode
WORKDIR hadoop
RUN sed -i '/^export JAVA_HOME/ s:.*:export JAVA_HOME=/usr/lib/jvm/java-8-oracle\nexport HADOOP_PREFIX=/usr/local/hadoop\n:' etc/hadoop/hadoop-env.sh && \
    sed -i '/<\/configuration>/i\\t<property>\n\t\t<name>fs.defaultFS<\/name>\n\t\t<value>hdfs://localhost:9000<\/value>\n\t</property>' etc/hadoop/core-site.xml && \
    sed -i '/<\/configuration>/i\\t<property>\n\t\t<name>dfs.replication</name>\n\t\t<value>1</value>\n\t</property>' etc/hadoop/hdfs-site.xml  && \
    sed -i '/<\/configuration>/i\\t<property>\n\t\t<name>yarn.nodemanager.aux-services</name>\n\t\t<value>mapreduce_shuffle</value>\n\t</property>' etc/hadoop/yarn-site.xml && \
    sed '/<\/configuration>/i\\t<property>\n\t\t<name>mapreduce.framework.name</name>\n\t\t<value>yarn</value>\n\t</property>' etc/hadoop/mapred-site.xml.template > etc/hadoop/mapred-site.xml

RUN hdfs namenode -format && service ssh start && start-dfs.sh && hdfs dfs -mkdir -p /user/root && hdfs dfs -put etc/hadoop input

EXPOSE 22 8032 8088 9000 50070

# By default, run a sample MapReduce job on YARN in a pseudo-distributed mode
CMD service ssh start && \
    start-dfs.sh && hdfs dfsadmin -safemode leave && \
    start-yarn.sh && \
    hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.6.0.jar grep input output 'dfs[a-z.]+' && \
    hdfs dfs -cat output/* && \
    stop-yarn.sh

