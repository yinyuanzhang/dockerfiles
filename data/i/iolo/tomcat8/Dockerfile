FROM dockerfile/java:oracle-java8
MAINTAINER Dongsu Jang <iolothebard@gmail.com>

ENV CATALINA_HOME /tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

ENV TOMCAT_VERSION 8.0.21
ENV TOMCAT_URL https://www.apache.org/dist/tomcat/tomcat-8/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz

RUN curl "$TOMCAT_URL" | tar -xz --strip-components=1 --exclude='bin/*.bat' --exclude='webapps/*'

#ADD sentenv.sh ${CATALINA_HOME}/bin/setenv.sh
#ADD server.xml ${CATALINA_HOME}/conf/server.xml
#ADD logging.properties ${CATALINA_HOME}/conf/logging.properties

#VOLUME ${CATALINA_HOME}/webapps
#VOLUME ${CATALINA_HOME}/logs
#VOLUME ${CATALINA_HOME}/work
#VOLUME ${CATALINA_HOME}/temp
#VOLUME ${CATALINA_HOME}/bin
#VOLUME ${CATALINA_HOME}/conf

EXPOSE 8080
EXPOSE 8009

CMD ["catalina.sh", "run"]

