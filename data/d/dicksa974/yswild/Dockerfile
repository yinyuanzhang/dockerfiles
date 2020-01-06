FROM jboss/wildfly:9.0.2.Final

ENV POSTGRESQL_VERSION 9.4-1201-jdbc41

ARG DB_HOST=localhost
ARG DB_NAME=ys
ARG DB_USER=egokia
ARG DB_PASS=eG0kia
ARG USER=egokia
ARG USER_PASS=eG0kia
ARG NAYA_USER=naya
ARG NAYA_PASS=GP5c6g
ARG DATASOURCE=ysDS

# adds a management user with the following credentials: admin:admin
# if you want to add an application user, use the '-a' option
RUN /opt/jboss/wildfly/bin/add-user.sh admin admin --silent \
    && /opt/jboss/wildfly/bin/add-user.sh -s -u ${USER} -p ${USER_PASS} \
    && /opt/jboss/wildfly/bin/add-user.sh -s -u ${USER} -p ${USER_PASS} -a --role guest \
    && /opt/jboss/wildfly/bin/add-user.sh -s -u ${NAYA_USER} -p ${NAYA_PASS} -a --role guest

ADD jdbc /opt/jdbc
ADD config /opt/config
ADD amq /opt/amq

USER root
RUN chmod +x /opt/config/execute.sh
USER jboss



RUN /opt/config/execute.sh commands.cli
RUN unzip /opt/amq/activemq-rar-5.10.0.rar -d /opt/jboss/wildfly/modules/org/apache/activemq/main

RUN rm -f /opt/jboss/wildfly/modules/org/apache/activemq/main/broker-config.xml
RUN rm -f /opt/jboss/wildfly/modules/org/apache/activemq/main/log4j*
RUN rm -f /opt/jboss/wildfly/modules/org/apache/activemq/main/slf4j*
RUN rm -f /opt/jboss/wildfly/modules/org/apache/activemq/main/geronimo*

# cleanup
RUN rm -rf $JBOSS_HOME/standalone/configuration/standalone_xml_history
RUN /opt/config/execute.sh add-activemq-rar.cli

# cleanup
RUN rm -rf $JBOSS_HOME/standalone/configuration/standalone_xml_history

RUN /bin/sh -c '$JBOSS_HOME/bin/standalone.sh &' && \
      sleep 10 && \
      cd /tmp && \
      curl --location --output postgresql-${POSTGRESQL_VERSION}.jar --url http://search.maven.org/remotecontent?filepath=org/postgresql/postgresql/${POSTGRESQL_VERSION}/postgresql-${POSTGRESQL_VERSION}.jar && \
      $JBOSS_HOME/bin/jboss-cli.sh --connect --command="deploy /tmp/postgresql-${POSTGRESQL_VERSION}.jar" && \
      $JBOSS_HOME/bin/jboss-cli.sh --connect --command="xa-data-source add --name=${DATASOURCE} --jndi-name=java:jboss/datasources/${DATASOURCE} --user-name=${DB_USER} --password=${DB_PASS} --driver-name=postgresql-9.4-1201-jdbc41.jar --xa-datasource-class=org.postgresql.xa.PGXADataSource --xa-datasource-properties=ServerName=${DB_HOST},PortNumber=5432,DatabaseName=${DB_NAME} --valid-connection-checker-class-name=org.jboss.jca.adapters.jdbc.extensions.postgres.PostgreSQLValidConnectionChecker --exception-sorter-class-name=org.jboss.jca.adapters.jdbc.extensions.postgres.PostgreSQLExceptionSorter" && \
      $JBOSS_HOME/bin/jboss-cli.sh --connect --command=:shutdown && \
      rm -rf $JBOSS_HOME/standalone/configuration/standalone_xml_history/ $JBOSS_HOME/standalone/log/* && \
      rm /tmp/postgresql-9.4*.jar && \
      rm -rf /tmp/postgresql-*.jar
# automatically launch the standalone configuration
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0", "-c", "standalone-full.xml"]