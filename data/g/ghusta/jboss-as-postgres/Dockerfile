# Inspired from jboss/wildfly
FROM ghusta/jboss-as:7
MAINTAINER Guillaume Husta (@ghusta)

###############################################################################
# DRIVER : https://jdbc.postgresql.org/download.html#current
#  TYPE  : JDBC41 Postgresql Driver for Java 7
#   DL   : https://jdbc.postgresql.org/download/postgresql-9.4.1212.jre7.jar
###############################################################################
ENV JDBC_JAR_FILE=postgresql-9.4.1212.jre7.jar
WORKDIR /opt/jboss
RUN curl -O https://jdbc.postgresql.org/download/${JDBC_JAR_FILE} \
    && mkdir -p $JBOSS_HOME/modules/org/postgresql/jdbc/main \
    && mv ${JDBC_JAR_FILE} $JBOSS_HOME/modules/org/postgresql/jdbc/main

ADD modules/org/postgresql/jdbc/main/module.xml $JBOSS_HOME/modules/org/postgresql/jdbc/main
RUN sed -i s/%POSTGRESQL-JAR-FILENAME%/$JDBC_JAR_FILE/g $JBOSS_HOME/modules/org/postgresql/jdbc/main/module.xml

###############################################################################
# Update config : add postgres driver in configuration/standalone.xml
# * https://docs.jboss.org/author/display/AS71/DataSource+configurationhttps://docs.jboss.org/author/display/AS71/DataSource+configuration
# * https://goldmann.pl/blog/2014/07/23/customizing-the-configuration-of-the-wildfly-docker-image/
###############################################################################
ADD jboss-cli/ /tmp/jboss-cli/
#RUN $JBOSS_HOME/bin/jboss-cli.sh --file=jboss-cli/add-driver.cli
#RUN ["chmod", "u+x", "./jboss-cli/execute.sh"]
#RUN chmod +x ./jboss-cli/execute.sh
RUN /tmp/jboss-cli/execute.sh

CMD ["/opt/jboss/jboss-as/bin/standalone.sh", "-b", "0.0.0.0"]

