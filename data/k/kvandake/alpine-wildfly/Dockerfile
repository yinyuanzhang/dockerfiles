# Use latest frolvlad/alpine-oraclejdk8 image as the base
FROM frolvlad/alpine-oraclejdk8:latest
MAINTAINER Aleksey Nikitin <kvandake@gmail.com>

# Set the WILDFLY_VERSION env variable
ENV WILDFLY_VERSION 9.0.0.Final

# Add the WildFly distribution to /opt
RUN cd $HOME \
	&& wget http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz \
    && tar xz -f wildfly-$WILDFLY_VERSION.tar.gz \
    && mkdir -p /opt \
    && mv $HOME/wildfly-$WILDFLY_VERSION /opt/wildfly \
    && rm wildfly-$WILDFLY_VERSION.tar.gz

ENV LAUNCH_JBOSS_IN_BACKGROUND true

# Expose the ports we're interested in
EXPOSE 8080 9990

# Set the default command to run on boot
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]