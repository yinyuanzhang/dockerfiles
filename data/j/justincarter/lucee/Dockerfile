FROM buildpack-deps:jessie-curl

MAINTAINER Justin Carter justin.w.carter@gmail.com

# lucee configuration
ENV LUCEE_VERSION 4.5.1.022
ENV LUCEE_INSTALLER_URL http://railo.viviotech.net/downloader.cfm/id/136/file
ENV LUCEE_INSTALLER="lucee-$LUCEE_VERSION-pl0-linux-x64-installer.run"
ENV LUCEE_PASSWORD password

ENV JRE_HOME /opt/lucee/jdk/jre 

# install lucee
RUN curl $LUCEE_INSTALLER_URL/$LUCEE_INSTALLER -o /tmp/$LUCEE_INSTALLER && \
	chmod -R 744 /tmp/$LUCEE_INSTALLER && \
	/tmp/$LUCEE_INSTALLER --mode unattended --installconn false --installiis false --railopass $LUCEE_PASSWORD && \
	rm -rf /tmp/*

# configure entropy source
RUN echo "java.security.egd=file:/dev/./urandom" >> /opt/lucee/tomcat/conf/catalina.properties

ONBUILD RUN rm -rf /opt/lucee/tomcat/webapps/ROOT/*.* /opt/lucee/tomcat/webapps/ROOT/assets

EXPOSE 8888

WORKDIR /opt/lucee/tomcat
CMD ["/opt/lucee/tomcat/bin/catalina.sh","run"]
