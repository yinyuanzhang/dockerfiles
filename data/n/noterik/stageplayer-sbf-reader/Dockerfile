FROM openjdk:8-jdk as builder

# Installs Ant
ENV ANT_VERSION 1.9.4

RUN cd && \
    wget -q http://archive.apache.org/dist/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz && \
    tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \
    mv apache-ant-${ANT_VERSION} /opt/ant && \
    rm apache-ant-${ANT_VERSION}-bin.tar.gz
       
ENV ANT_HOME /opt/ant
ENV PATH ${PATH}:/opt/ant/bin

# COPY OVER JAVA CODE TO DOCKER CONTAINER
COPY src /home/stageplayer-sbf-reader/src/
COPY libs /home/stageplayer-sbf-reader/libs/
COPY WebContent /home/stageplayer-sbf-reader/WebContent/
COPY /build.xml /home/stageplayer-sbf-reader/
COPY /build.properties /home/stageplayer-sbf-reader/

RUN cd /home/stageplayer-sbf-reader && ant

FROM centos:7

ENV CATALINA_HOME /usr/local/tomcat
ENV TOMCAT_VERSION 8.5.23

RUN yum update -y && \
	 yum -y install java-1.8.0-openjdk wget tar.x86_64 && \
	 yum clean all

RUN mkdir -p /opt/hdf /springfield

RUN mkdir -p /opt/hdf /springfield /docker && \
    wget --quiet --no-cookies https://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/tomcat.tgz && \
	tar xzvf /tmp/tomcat.tgz -C /springfield && \
	mv /springfield/apache-tomcat-${TOMCAT_VERSION} $CATALINA_HOME && \
	rm /tmp/tomcat.tgz && \
	rm -rf $CATALINA_HOME/webapps/examples $CATALINA_HOME/webapps/docs

COPY ./docker/tomcat/lib/* $CATALINA_HOME/lib/
COPY ./docker/tomcat/tomcat-users.xml $CATALINA_HOME/conf/tomcat-users.xml
COPY ./docker/tomcat/setenv.sh $CATALINA_HOME/bin/setenv.sh
COPY ./docker/docker-entrypoint.sh /docker/docker-entrypoint.sh

RUN chmod +x $CATALINA_HOME/bin/setenv.sh /docker/docker-entrypoint.sh

COPY --from=builder /home/stageplayer-sbf-reader/dist/stageplayer-sbf-reader.war $CATALINA_HOME/webapps/
COPY ./docker/hdf /opt/hdf

EXPOSE 8080
ENTRYPOINT ["/docker/docker-entrypoint.sh"]