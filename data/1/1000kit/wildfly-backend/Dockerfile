FROM 1000kit/wildfly as build

MAINTAINER 1000kit <docker@1000kit.org>


LABEL org.1000kit.vendor="1000kit" \
      org.1000kit.license=GPLv3 \
      org.1000kit.version=1.0.0

COPY --chown=jboss:jboss add-module.cli /tmp/add-module.cli  
RUN curl -o /tmp/postgresql-42.2.8.jar  https://jdbc.postgresql.org/download/postgresql-42.2.8.jar

RUN /opt/jboss/wildfly/bin/jboss-cli.sh --file=/tmp/add-module.cli
RUN rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history

USER root
RUN mkdir -p /opt/liquibase/ && \
    cd /opt/liquibase/ && \
    curl -L https://github.com/liquibase/liquibase/releases/download/liquibase-parent-3.8.0/liquibase-3.8.0-bin.tar.gz | tar xz && \
    cp /tmp/postgresql-42.2.8.jar /opt/liquibase/lib && \
    chown -R jboss:0 ${JBOSS_HOME} && \
    chmod -R g+rw ${JBOSS_HOME}


FROM 1000kit/wildfly
COPY --chown=jboss:jboss --from=build /opt/jboss/wildfly/standalone/configuration/* /opt/jboss/wildfly/standalone/configuration/
COPY --chown=jboss:jboss --from=build /opt/jboss/wildfly/modules/org /opt/jboss/wildfly/modules/org
COPY --chown=jboss:jboss --from=build /opt/liquibase/ /opt/liquibase/

USER root
RUN echo "JBOSS HOME = $JBOSS_HOME" && \
    chown -R jboss:0 ${JBOSS_HOME} && \
    chmod -R g+rw ${JBOSS_HOME}
USER jboss
# default env vars, override with your own values
ENV DB_HOST postgresdb
ENV DB_PORT 5432
ENV DB_USER wildfly
ENV DB_PASS wildfly
ENV DB_NAME wildfly
####END


