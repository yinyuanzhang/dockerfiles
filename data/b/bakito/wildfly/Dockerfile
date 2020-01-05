FROM bakito/java:latest
MAINTAINER Marc Brugger <github@bakito.ch>


ENV WILDFLY_VERSION 9.0.1.Final
ENV JBOSS_HOME /opt/wildfly
ENV PATH $JBOSS_HOME/bin:$PATH

RUN cd /tmp \
  && wget -q -c -O "wildfly.tar.gz" --no-check-certificate --no-cookies  "http://download.jboss.org/wildfly/${WILDFLY_VERSION}/wildfly-${WILDFLY_VERSION}.tar.gz" \
  && tar -zxvf wildfly.tar.gz > /dev/null \
  && rm /tmp/wildfly.tar.gz -Rf \
  && mv /tmp/wildfly* /opt \
  && ln -s /opt/wildfly* $JBOSS_HOME \
  && rm /tmp/* -Rf

EXPOSE 8080

CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]
