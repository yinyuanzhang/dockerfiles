FROM javergarav/tomee

COPY env/tomee.xml conf/tomee.xml
COPY env/server.xml conf/server.xml

COPY target/tasks-ms.war webapps/tasks-ms.war
EXPOSE 3003
