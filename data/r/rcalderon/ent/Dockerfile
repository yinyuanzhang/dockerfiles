FROM ubuntu:14.04

MAINTAINER RC

# Commands

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y vim nano git wget libfreetype6 libfontconfig bzip2 supervisor zip unzip openssh-server make g++ patch zlib1g-dev libgif-dev && \
  mkdir -p /srv/var /var/log/supervisor /opt

ENV TOMCAT_VERSION 7.0.70
ENV TOMCAT_PORT 8080
ENV TOMCAT_PATH /opt/tomcat
ENV ACTIVEMQ_VERSION 5.10.0
ENV ACTIVEMQ_PATH /opt/activemq

# ----------- Install java 7 -------------
RUN \
wget -c -O "jdk-7u80-linux-x64.tar.gz" --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/7u80-b15/jdk-7u80-linux-x64.tar.gz" && \

	tar -zxvf  jdk-7u80-linux-x64.tar.gz -C /  && \
	rm jdk-7u80-linux-x64.tar.gz  && \
	mv /jdk1.7.0_80 /jdk

 ENV JAVA_HOME /jdk
 ENV JRE_HOME  $JAVA_HOME/jre
 ENV PATH $PATH:$JAVA_HOME/bin
 RUN java -version
 RUN sed -i 's/jdk.tls.disabledAlgorithms=SSLv3/#jdk.tls.disabledAlgorithms=SSLv3/g' /jdk/jre/lib/security/java.security

# ----------- Install Tomcat -------------#
RUN \
  wget -O /tmp/tomcat.tar.gz http://archive.apache.org/dist/tomcat/tomcat-7/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz && \
  cd /tmp && \
  tar zxf /tmp/tomcat.tar.gz && \
  ls /tmp && \
  mv /tmp/apache-tomcat* $TOMCAT_PATH && \
  rm -rf $TOMCAT_PATH/webapps/*.* && \
  rm -rf $TOMCAT_PATH/webapps/* && \
  rm /tmp/tomcat.tar.gz

EXPOSE $TOMCAT_PORT
EXPOSE 1317
EXPOSE 22

# ----------- Configure SSH -------------
#RUN echo deb http://archive.ubuntu.com/ubuntu trusty main universe > /etc/apt/sources.list.d/trusty.list

# Clean
ADD es_docker_key.pub es_docker_key.pub

RUN \
  mkdir ~/.ssh && \
  touch ~/.ssh/authorized_keys && \
  cat es_docker_key.pub >> ~/.ssh/authorized_keys && \
  rm es_docker_key.pub && \
  /etc/init.d/ssh restart

# Files
ADD tomcat_supervisord_wrapper.sh $TOMCAT_PATH/bin/tomcat_supervisord_wrapper.sh
RUN chmod 755 $TOMCAT_PATH/bin/tomcat_supervisord_wrapper.sh

# ----------- Install swftool -----------
# RUN add-apt-repository -y ppa:guilhem-fr/swftools
RUN apt-get -y install swftools

# ----------- Install WHOIS -------------
# RUN add-apt-repository -y ppa:nathan-renniewaldock/ppa
RUN apt-get -y install whois

# ----------- Modify libraries security for jre (jar)-------------
ADD UnlimitedJCEPolicy/local_policy.jar /jdk/jre/lib/security/local_policy.jar
ADD UnlimitedJCEPolicy/US_export_policy.jar /jdk/jre/lib/security/US_export_policy.jar

# Start
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]


