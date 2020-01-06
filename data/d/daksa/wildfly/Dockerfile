FROM daksa/java

#Set Wildfly env variable
ENV WILDFLY_VERSION 14.0.1.Final
ENV JBOSS_HOME /opt/wildfly
ENV HOME=/home/daksa

USER root
WORKDIR /opt
RUN curl -O https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz \
 && tar xf wildfly-$WILDFLY_VERSION.tar.gz \
 && mv wildfly-$WILDFLY_VERSION $JBOSS_HOME \
 && chown -R daksa.daksa $JBOSS_HOME \
 && rm -rf $JBOSS_HOME/docs \
 && rm wildfly-$WILDFLY_VERSION.tar.gz

RUN echo "hosts: files dns" >> /etc/nsswitch.conf

USER daksa
EXPOSE 8080 9990

