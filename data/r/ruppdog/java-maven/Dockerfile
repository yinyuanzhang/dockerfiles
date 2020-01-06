FROM centos:centos6

ENV docker_build_data "2015-02-17 09:00 MST"

# Update and Install Dependencies
RUN \
	yum update -y && \
	yum install -y \
	tar \
	java-1.7.0-openjdk-devel.x86_64

# Set Java Home
ENV JAVA_HOME /usr/lib/jvm/jre-1.7.0-openjdk.x86_64

# Install Maven
RUN \
	cd /tmp && \
	curl 'http://mirror.cogentco.com/pub/apache/maven/maven-3/3.2.5/binaries/apache-maven-3.2.5-bin.tar.gz' > apache-maven-3.2.5-bin.tar.gz && \
	tar xzf apache-maven-3.2.5-bin.tar.gz && \
	rm apache-maven-3.2.5-bin.tar.gz && \
	mv apache-maven-3.2.5 /usr/local

ENV M2_HOME /usr/local/apache-maven-3.2.5
ENV M2 $M2_HOME/bin
ENV MAVEN_OPTS -Xmx2g -XX:ReservedCodeCacheSize=512m
ENV PATH $M2:$PATH
