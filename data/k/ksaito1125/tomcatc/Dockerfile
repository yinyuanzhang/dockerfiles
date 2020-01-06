FROM tomcat:8.0-alpine

COPY ./tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml
COPY ./server.xml.j2 /usr/local/tomcat/server.xml.j2
COPY ./run.sh /usr/local/tomcat/bin
COPY ./web.xml /usr/local/tomcat/webapps/examples/WEB-INF/web.xml
RUN chmod u+x /usr/local/tomcat/bin/run.sh

CMD ["run.sh", "run"]