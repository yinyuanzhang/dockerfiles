FROM tomcat:9-jre8
MAINTAINER Jonas Manuel
# See https://github.com/opensourceBIM/BIMserver/wiki/Install-on-Ubuntu

ENV TOMCAT_HOME /usr/local/tomcat
ENV BIMSERVER_APP $TOMCAT_HOME/webapps/bimserver
ENV VERSION 1.5.122

# Delete the example Tomcat app to speed up deployment.
RUN rm -rf $TOMCAT_HOME/webapps/examples

RUN mkdir -p /bimserver/home

ADD https://github.com/opensourceBIM/BIMserver/releases/download/v$VERSION/bimserverwar-$VERSION.war $BIMSERVER_APP.war
RUN unzip $BIMSERVER_APP.war -d $BIMSERVER_APP && rm $BIMSERVER_APP.war
