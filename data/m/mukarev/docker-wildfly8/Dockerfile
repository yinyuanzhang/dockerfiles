FROM piranha/java8
# this image is provided by adorsys -> https://adorsys.de
# author mko (Markus Kosmal)
MAINTAINER mko <mko@adorsys.de>

# change to what you need and expose as environment variable, so host can check version
ENV WILDFLY_VERSION 8.2.0.Final

RUN apt-get update && apt-get install wget unzip

# change to target destination - download
RUN cd /opt && wget "http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.zip"
# ensure once again target destination - extract - cleanup0
RUN cd /opt && unzip "wildfly-$WILDFLY_VERSION.zip" && rm "wildfly-$WILDFLY_VERSION.zip"

# sym link to have version independent paths
RUN ln -s /opt/wildfly-$WILDFLY_VERSION /opt/wildfly

# set wildfly's home directory - still called JBOSS_HOME
ENV JBOSS_HOME /opt/wildfly

# create executing user and grant rights
RUN groupadd -r wildfly -g 433 && useradd -u 431 -r -g wildfly -d /opt/wildfly -s /bin/false -c "WildFly-Managing" wildfly && chown -R wildfly:wildfly /opt/wildfly*

# Expose access to runtime (8080 by default) and management(9990 by default) if you want
# we expose the default wildfly ports
EXPOSE 8080 9990

# optionally add startup content
COPY ./res/welcome-content /opt/wildfly/welcome-content
COPY ./res/apps/* /opt/wildfly/standalone/deployments

# if you need to customize more,
# insert your code here
#
# sample
# COPY ./res/custom/standalone.xml /opt/wildfly/standalone/configuration/
#
# before user changes to ensure necessary rights

# now we change to the newly created wildfly user, so it can run Wildfly
USER wildfly

# startup and bind to all interfaces
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
