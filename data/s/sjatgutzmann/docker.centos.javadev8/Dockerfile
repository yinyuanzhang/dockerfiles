#Author https://github.com/sjatgutzmann

# base of this image
FROM sjatgutzmann/docker.centos.oraclejava8
MAINTAINER Sven Jörns <sj.at.gutzmann@gmail.com>

RUN yum -y update; yum clean all \
 && yum -y install vim git

ENV JAVA_TOOLS_HOME=/opt/javatools
RUN mkdir ${JAVA_TOOLS_HOME} && cd ${JAVA_TOOLS_HOME}

ENV M2_HOME=/opt/javatools/maven MAVEN_VERSION=3.3.9
WORKDIR ${JAVA_TOOLS_HOME}
# install maven
# https://maven.apache.org/download.cgi
RUN wget -q http://artfiles.org/apache.org/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
	&& tar -xzf apache-maven-${MAVEN_VERSION}-bin.tar.gz \
	&& ln -s apache-maven-${MAVEN_VERSION} maven \
	&& echo "M2_HOME=${M2_HOME}" > /etc/profile.d/maven.sh \
	&& echo "PATH=\$PATH:\${M2_HOME}/bin" >> /etc/profile.d/maven.sh

# install ANT
ENV ANT_HOME /opt/javatools/ant
ENV ANT_VERSION 1.9.7
RUN wget -q http://ftp.halifax.rwth-aachen.de/apache/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz \
	&& tar xzf apache-ant-${ANT_VERSION}-bin.tar.gz \
	&& ln -s apache-ant-${ANT_VERSION} ant \
	&& echo "ANT_HOME=${ANT_HOME}" > /etc/profile.d/ant.sh \
	&& echo "PATH=\$PATH:\${ANT_HOME}/bin" >> /etc/profile.d/ant.sh


ENTRYPOINT /bin/bash
 
