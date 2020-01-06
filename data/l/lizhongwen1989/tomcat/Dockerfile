FROM quay.io/lizhongwen/oracle-jdk:1.8

MAINTAINER github.com/Official-Registry, lizhongwen1989@gmail.com

ENV TOMCAT_VERSION=8.5.6
ENV TOMCAT_HOME=/opt/app/tomcat
ENV JAVA_DEBUG=false
ENV JVM_MIN_MEM=256
ENV JVM_MAX_MEM=1024

RUN apt-get install -y unzip \
  && curl --fail --location --retry 3 \
    https://archive.apache.org/dist/tomcat/tomcat-8/v8.5.6/bin/apache-tomcat-8.5.6.tar.gz \
    -o /tmp/tomcat.tar.gz \
  && tar -zvxf /tmp/tomcat.tar.gz -C /tmp/ \
  && mkdir -p /opt/app/ \
  && mv /tmp/apache-tomcat-${TOMCAT_VERSION} ${TOMCAT_HOME} \
  && rm -rf /tmp/tomcat.tar.gz ${TOMCAT_HOME}/webapps/*

ADD resources/entrypoint.sh ${TOMCAT_HOME}/bin/

RUN chmod +x ${TOMCAT_HOME}/bin/entrypoint.sh

EXPOSE 8080 8888

ENTRYPOINT ["/bin/sh", "-c", "${TOMCAT_HOME}/bin/entrypoint.sh"]
