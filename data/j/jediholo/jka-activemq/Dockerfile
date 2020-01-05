# JKA ActiveMQ server based on CentOS 7
FROM centos:7
LABEL maintainer="Fabien Crespel <fabien@crespel.net>"

# Arguments
ARG ACTIVEMQ_VERSION=5.15.8
ARG ACTIVEMQ_URL=http://archive.apache.org/dist/activemq/${ACTIVEMQ_VERSION}/apache-activemq-${ACTIVEMQ_VERSION}-bin.tar.gz

# Environment
ENV ACTIVEMQ_ADMIN_PASSWORD=admin

# Utilities
RUN yum -y install file iproute less socat wget which &&\
	yum -y clean all

# Java
RUN yum -y install java-1.8.0-openjdk-headless &&\
	yum -y clean all

# ActiveMQ
RUN mkdir -p /opt/activemq &&\
	curl -fsSL -o /tmp/apache-activemq.tar.gz ${ACTIVEMQ_URL} &&\
	tar -xzf /tmp/apache-activemq.tar.gz -C /opt/activemq --strip-components=1 &&\
	rm -f /tmp/apache-activemq.tar.gz

# Files
COPY ./root /
RUN chmod +x /run.sh
RUN groupadd activemq &&\
	useradd -d /opt/activemq -g activemq -s /bin/bash activemq &&\
	chown -R activemq:activemq /opt/activemq

# Execution
USER activemq
EXPOSE 61616 5672 61613 1883 61614 8161
CMD ["/run.sh"]
