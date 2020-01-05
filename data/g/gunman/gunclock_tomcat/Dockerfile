FROM tomcat:9.0.1-alpine

ADD gunclock.war /usr/local/tomcat/webapps/gunclock.war

COPY server.xml /usr/local/tomcat/conf/

EXPOSE 8080
#EXPOSE 443

CMD ["catalina.sh", "run"]
