# Based on plussell/base
FROM plussell/base

MAINTAINER plussell devteam <devteam@plussell.org>

# Copy files
COPY files /tmp/files

# Install updates and java
RUN yum -y upgrade && \
    yum -y install /tmp/files/jre-8u141-linux-x64.rpm && \
    yum clean all

# Clean temporary files
RUN rm -rf /tmp/files

# Switch to jboss user
USER jboss

# Set JAVA_HOME variable
ENV JAVA_HOME /usr/java/default
