FROM tomcat:8.0.21-jre8
MAINTAINER lovesb777 <lovesb777@geninetworks.com>
WORKDIR $CATALINA_HOME

COPY ./deploy $CATALINA_HOME/webapps
COPY ./tomcat_server.xml $CATALINA_HOME/conf/server.xml

RUN rm -rf $CATALINA_HOME/webapps/ROOT

EXPOSE 80
CMD ["catalina.sh", "run"]

# sudo docker run -i -t -p 443:443 <image>
# ctrl + p
# ctrl + q