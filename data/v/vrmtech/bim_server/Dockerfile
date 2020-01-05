FROM tomcat:8.5
MAINTAINER Sunil Antony <sunil@vrmtechnology.co.uk>

RUN apt-get update && apt-get -y install jq

ENV TOMCAT_HOME /usr/local/tomcat

RUN rm -rf $TOMCAT_HOME/webapps/examples $TOMCAT_HOME/webapps/ROOT

ENV BIMSERVER_APP $TOMCAT_HOME/webapps/ROOT
ENV BIMSERVER_WAR_URL https://github.com/opensourceBIM/BIMserver/releases/download/v1.5.157/bimserverwar-1.5.157.war

ADD $BIMSERVER_WAR_URL $BIMSERVER_APP.war
RUN unzip $BIMSERVER_APP.war -d $BIMSERVER_APP && rm $BIMSERVER_APP.war

COPY docker-entrypoint.sh /

RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["bimserver"]
