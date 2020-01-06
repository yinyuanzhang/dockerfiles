# Source: https://hub.docker.com/_/tomcat/
FROM tomcat:8.0-jre8

# How to set the administrator password with TOMCAT_PASS environment variable
# https://github.com/b0c1/docker-containers/tree/master/tomcat
ADD conf/tomcat-users.xml ${CATALINA_HOME}/conf/

# Install PSI probe
ADD vendor/psi-probe-web-3.2.0.war ${CATALINA_HOME}/webapps/probe.war

# Copy apps
ADD app/abrabi.war ${CATALINA_HOME}/webapps/abrabi.war
RUN mkdir -p init 

# Set recomended params
RUN export CATALINA_OPTS="$CATALINA_OPTS -Xms192m"
RUN export CATALINA_OPTS="$CATALINA_OPTS -Xmx2024m"

# Initialization
RUN export JAVA_OPTS="-Dabra.init.dir=${CATALINA_HOME}/init"
ADD init/connection.xml ${CATALINA_HOME}/init/connection.xml
ADD init/definition.xml ${CATALINA_HOME}/init/definition.xml