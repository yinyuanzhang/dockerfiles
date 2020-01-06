FROM eiccefetrj/eic-base:1.1

ENV TOMCAT_VERSION 9.0.1

RUN locale-gen pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LC_CTYPE pt_BR.UTF-8

#RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update && apt-get install -y build-essential software-properties-common

RUN wget --quiet --no-cookies http://apache.rediris.es/tomcat/tomcat-9/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/tomcat.tgz && \
tar xzvf /tmp/tomcat.tgz -C /opt && mv /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat

RUN rm /tmp/tomcat.tgz && rm -rf /opt/tomcat/webapps/examples && rm -rf /opt/tomcat/webapps/docs

ENV CATALINA_HOME /opt/tomcat
ENV PATH $PATH:$CATALINA_HOME/bin

EXPOSE 8080
EXPOSE 8009
EXPOSE 4110

#VOLUME "/opt/tomcat/webapps"
WORKDIR /opt/tomcat

CMD ["/opt/tomcat/bin/catalina.sh","run"]
