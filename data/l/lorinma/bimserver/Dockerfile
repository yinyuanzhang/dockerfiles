FROM tomcat:7
MAINTAINER Ling Ma <lingma@technion.ac.il>
# See https://github.com/opensourceBIM/BIMserver/wiki/Install-on-Ubuntu

ENV TOMCAT_HOME /usr/local/tomcat
ENV BIMSERVER_APP $TOMCAT_HOME/webapps/bimserver

# Delete the example Tomcat app to speed up deployment.
RUN rm -rf $TOMCAT_HOME/webapps/examples

ADD https://github.com/opensourceBIM/BIMserver/releases/download/1.4.0-FINAL-2015-05-14/bimserver-tomcat7-1.4.0-FINAL-2015-05-14.war $BIMSERVER_APP.war
RUN unzip $BIMSERVER_APP.war -d $BIMSERVER_APP && rm $BIMSERVER_APP.war