FROM jboss/base-jdk:8

USER root
RUN mkdir -p /opt/wildfly

ENV JBOSS_DIRECTORY /opt/wildfly
ENV JBOSS_HOME /opt/wildfly/wildfly-local
ENV LAUNCH_JBOSS_IN_BACKGROUND true

COPY wildfly-local.zip ${JBOSS_DIRECTORY}/

RUN cd ${JBOSS_DIRECTORY} && unzip wildfly-local.zip && rm wildfly-local.zip
COPY wildfly_logo.png /opt/wildfly/wildfly-local/welcome-content/

CMD ["/opt/wildfly/wildfly-local/bin/standalone.sh", "-b", "0.0.0.0"]

