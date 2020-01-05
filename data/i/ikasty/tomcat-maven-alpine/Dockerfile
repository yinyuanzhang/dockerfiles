FROM openjdk:8-alpine
MAINTAINER Daeyoun Kang <mail.ikasty@gmail.com>

# predefine values
ENV MAVEN_VERSION=3.3.9 \
	TOMCAT_MAJOR=7 \
	TOMCAT_VERSION=7.0.72

ENV TOMCAT_HOME=/usr/local/tomcat \
	M2_HOME=/usr/lib/mvn

ENV M2=$M2_HOME/bin \
	CATALINA_BASE=/usr/local/tomcat \
	CATALINA_HOME=/usr/local/tomcat \
	CATALINA_TMPDIR=/usr/local/tomcat/temp

ENV PATH=$PATH:$M2_HOME:$M2:$CATALINA_HOME/bin

# install maven
RUN wget http://mirror.navercorp.com/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
	tar xzf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
	rm apache-maven-$MAVEN_VERSION-bin.tar.gz && \
	mv apache-maven-$MAVEN_VERSION /usr/lib/mvn

# install tomcat
RUN apk add --update --no-cache --virtual .build curl && \
	curl -jksSL -o /tmp/apache-tomcat.tar.gz  http://apache.mirror.cdnetworks.com/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
	tar -C /usr -xzf /tmp/apache-tomcat.tar.gz && \
	mv /usr/apache-tomcat-${TOMCAT_VERSION} ${TOMCAT_HOME} && \
	rm -rf /tmp/* && \
	apk del .build

# copy script
COPY ./start.sh /usr/local/tomcat/bin/start.sh
RUN chmod +x /usr/local/tomcat/bin/start.sh
WORKDIR /usr/local/tomcat

CMD start.sh