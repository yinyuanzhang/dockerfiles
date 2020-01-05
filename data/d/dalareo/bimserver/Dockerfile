FROM tomcat:8.5
MAINTAINER David A. Lareo <dalareo@gmail.com>
# See https://github.com/opensourceBIM/BIMserver/wiki/Install-on-Ubuntu

ENV TOMCAT_HOME /usr/local/tomcat
ENV BIMSERVER_APP $TOMCAT_HOME/webapps/bimserver

# Delete the example Tomcat app to speed up deployment.
RUN rm -rf $TOMCAT_HOME/webapps/examples

ADD https://github.com/opensourceBIM/BIMserver/releases/download/1.4.0-FINAL-2015-11-04/bimserver-1.4.0-FINAL-2015-11-04.war $BIMSERVER_APP.war
RUN unzip $BIMSERVER_APP.war -d $BIMSERVER_APP && rm $BIMSERVER_APP.war
