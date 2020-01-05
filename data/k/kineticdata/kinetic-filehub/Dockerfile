FROM tomcat:8.5-jre8

ENV DATA_DIRECTORY=${CATALINA_HOME}/kinetic-filehub-data
ENV JAVAOPT_XMX=256m

# Configure Tomcat
WORKDIR $CATALINA_HOME
COPY tomcat/server.xml conf/server.xml
COPY tomcat/setenv.sh bin/setenv.sh
RUN  chmod +x bin/setenv.sh

# Kinetic Filehub
ARG VERSION=1.2.0
ADD https://s3.amazonaws.com/kineticdata.com/downloads/kinetic-filehub/${VERSION}/kinetic-filehub.war ${CATALINA_HOME}/webapps

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD curl --fail http://localhost:8080/kinetic-filehub || exit 1
