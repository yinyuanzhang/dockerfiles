FROM coong/base-centos:latest
LABEL maintainer="loind89@gmail.com"

# User root user to install software
USER root

# Install Java
RUN yum -y install java-1.8.0-openjdk-devel 

# install maven
RUN wget http://www-eu.apache.org/dist/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.tar.gz \
        && tar xzf apache-maven-3.5.4-bin.tar.gz \
        && rm -f apache-maven-3.5.4-bin.tar.gz \
        && mv apache-maven-3.5.4 maven \        
        && mv -f maven /opt/ \
        && ln -s /opt/maven/bin/mvn /usr/bin/mvn
RUN yum clean all

# Switch back to jboss user
#USER bootapp

# Set the JAVA_HOME variable to make it clear where Java is located
ENV JAVA_HOME /usr/lib/jvm/java
#
ENV M2_HOME /opt/maven
ENV M2_CONFIG "/root/.m2"
