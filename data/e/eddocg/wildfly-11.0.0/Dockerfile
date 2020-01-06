
FROM openjdk:8

MAINTAINER eddocg

ENV WILDFLY_VERSION_MAJOR=11
ENV WILDFLY_VERSION_MINOR=0
ENV WILDFLY_VERSION_PATCH=0
ENV WILDFLY_VERSION=${WILDFLY_VERSION_MAJOR}.${WILDFLY_VERSION_MINOR}.${WILDFLY_VERSION_PATCH}
ENV JBOSS_HOME /opt/wildfly

# Add the WildFly distribution to /opt, and make wildfly the owner of the extracted tar content
RUN cd $HOME \
    && wget https://download.jboss.org/wildfly/${WILDFLY_VERSION}.Final/wildfly-${WILDFLY_VERSION}.Final.zip \
    && unzip -d /opt wildfly-${WILDFLY_VERSION}.Final.zip \
    && ln -s /opt/wildfly-${WILDFLY_VERSION}.Final ${JBOSS_HOME} \
    && rm wildfly-${WILDFLY_VERSION}.Final.zip
	
# Ensure signals are forwarded to the JVM process correctly for graceful shutdown
ENV LAUNCH_JBOSS_IN_BACKGROUND true

EXPOSE 9990 8080 8443

# Set the default command to run on boot
# This will boot WildFly in the standalone mode and bind to all interface
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]
