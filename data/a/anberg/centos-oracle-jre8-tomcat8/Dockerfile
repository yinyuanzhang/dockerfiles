FROM nimmis/java-centos:oracle-8-jre

MAINTAINER Andreas Berg <andreas.berg@istone.com>

# Install prepare infrastructure
RUN yum -y update && \
 yum -y install wget && \
 yum -y install tar
 
# Prepare environment 
ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

# Install Tomcat
ENV TOMCAT_MAJOR 8
ENV TOMCAT_VERSION 8.5.14

RUN curl -L -O -k "http://apache.mirrors.spacedump.net/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz" && \
  tar -xvf apache-tomcat-${TOMCAT_VERSION}.tar.gz --strip-components=1 && \
  rm bin/*.bat && \
  rm apache-tomcat*.tar.gz && \
  find ${CATALINA_HOME}/webapps/* ! -name 'ROOT' -type d -exec rm -rf {} +

RUN chmod +x ${CATALINA_HOME}/bin/*sh

# Create tomcat user
RUN groupadd -r tomcat && \
 useradd -g tomcat -d ${CATALINA_HOME} -s /bin/bash  -c "Tomcat user" tomcat && \
 chown -R tomcat:tomcat ${CATALINA_HOME}
 
ENV MYSQL_DRIVER_VERSION 5.1.40
RUN curl -Lks http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz -o ${CATALINA_HOME}/lib/mysql-connector.tar.gz

EXPOSE 8080
EXPOSE 8009

USER tomcat
CMD ["catalina.sh", "run"]
