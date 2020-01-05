FROM tomcat:8-jre8

ENV HYSTRIX_VERSION 1.4.14

RUN rm -rf /usr/local/tomcat/webapps/*
RUN wget -O /usr/local/tomcat/webapps/ROOT.war http://search.maven.org/remotecontent?filepath=com/netflix/hystrix/hystrix-dashboard/${HYSTRIX_VERSION}/hystrix-dashboard-${HYSTRIX_VERSION}.war


