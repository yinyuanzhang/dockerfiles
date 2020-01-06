FROM tomcat:7-jre8-alpine

# server port
EXPOSE 8005

# connector ports
EXPOSE 8080
EXPOSE 8009

# copy configuration
COPY web.xml ${CATALINA_HOME}/conf
COPY tomcat-users.xml ${CATALINA_HOME}/conf
COPY server.xml ${CATALINA_HOME}/conf

# copy war file(s)
COPY sample.war ${CATALINA_HOME}/webapps
