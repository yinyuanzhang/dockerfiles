# Dockerfile to build 2.2 validate
FROM tomcat:7.0.79-jre8
MAINTAINER shaider@paylock.com

# ARG version

RUN rm -rf /usr/local/tomcat/webapps/*
#ADD ./cws-${version}.tar /usr/local/tomcat/webapps/
ADD ./cws-2.2.tar /usr/local/tomcat/webapps/

VOLUME paylock

RUN ln -s /paylock/config/context.xml /usr/local/tomcat/webapps/cws/META-INF/context.xml \
	&& ln -s /paylock/config/cws.lic /usr/local/tomcat/webapps/cws/WEB-INF/cws.lic \
	&& ln -s /paylock/config/smtp.xml /usr/local/tomcat/webapps/cws/WEB-INF/config/email/smtp.xml \
	&& rm /usr/local/tomcat/conf/server.xml \
	&& ln -s /paylock/tomcat/server.xml /usr/local/tomcat/conf/server.xml

EXPOSE 8080

CMD ["catalina.sh", "start" ]
