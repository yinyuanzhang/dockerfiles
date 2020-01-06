FROM tomcat:7
MAINTAINER Ruben Silva <rubensilva84@gmail.com>

ENV TOMCAT_HOME /usr/local/tomcat

RUN rm -rf $TOMCAT_HOME/webapps/examples

ENV BIMSERVER_APP $TOMCAT_HOME/webapps/bimserver
ENV BIMSERVER_WAR_URL https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/bimserver/bimserver-1.2.war
RUN set -x \
	&& curl -fSL "$BIMSERVER_WAR_URL" -o $BIMSERVER_APP.war \	
	&& unzip $BIMSERVER_APP.war -d $BIMSERVER_APP  \
	&& rm $BIMSERVER_APP.war 	

ENV BIM_SITE_ADDRESS="http://localhost:8080/bimserver" \
	BIM_SMTP_SERVER="fakesmtp.example.org" \
	BIM_SMTP_SENDER="fake.sender@example.org" \
	BIM_ADMIN_NAME="Admin User" \
	BIM_ADMIN_USERNAME="admin@example.org" \
	BIM_ADMIN_PASSWORD="bimserver"

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["bimserver"]