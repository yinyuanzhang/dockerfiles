FROM centos:7
MAINTAINER Herman Junge <herman.junge@telefonica.com>


###############################################################################
#
#  JAVA and other packages
#
###############################################################################


RUN yum update -y
RUN yum install -y wget tar git java-1.7.0-openjdk.x86_64
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.85-2.6.1.2.el7_1.x86_64/jre


###############################################################################
#
#  Apache Flume
#
###############################################################################


RUN wget https://www.apache.org/dist/flume/1.5.2/apache-flume-1.5.2-bin.tar.gz && \
	tar xvfz apache-flume-1.5.2-bin.tar.gz && \
	rm apache-flume-1.5.2-bin.tar.gz && \
	mv apache-flume-1.5.2-bin flume && \
	mkdir -p /flume/plugins.d/cygnus/ && \
	mkdir /flume/plugins.d/cygnus/lib


###############################################################################
#
#  Apache Thrift
#
###############################################################################


RUN wget http://repo1.maven.org/maven2/org/apache/thrift/libthrift/0.9.1/libthrift-0.9.1.jar && \
	rm /flume/lib/libthrift-*.jar && \
	mv libthrift-0.9.1.jar /flume/lib


###############################################################################
#
#  Copy the jar to the plugins directory
#
#  And set cygnus-flume-ng into the flume directory
#
###############################################################################


ADD ./cygnus-0.8.2_SNAPSHOT-jar-with-dependencies.jar \
	/flume/plugins.d/cygnus/lib/cygnus-0.8.2_SNAPSHOT-jar-with-dependencies.jar
ADD ./cygnus-flume-ng /flume/bin/cygnus-flume-ng


###############################################################################
#
#  Expose the Port
#
###############################################################################


EXPOSE 5050
