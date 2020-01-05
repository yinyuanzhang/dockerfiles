FROM tomcat:8.0-alpine

COPY klein-bp-0.1.war /usr/local/tomcat/webapps/klein-bp-0.1.war

ADD tomcat-users.xml $CATALINA_HOME/conf 

EXPOSE 8080