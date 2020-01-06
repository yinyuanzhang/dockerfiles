FROM jboss/wildfly:17.0.1.Final

ENV JBOSS_HOME /opt/jboss/wildfly

# Set the TEIID_VERSION env variable
ENV TEIID_VERSION 12.3.1
ENV TEIID_CONSOLE_VERSION 3.1.3

# Download and unzip Teiid server
RUN cd $JBOSS_HOME \
    && curl -O https://oss.sonatype.org/service/local/repositories/releases/content/org/teiid/wildfly/teiid-wildfly/$TEIID_VERSION/teiid-wildfly-$TEIID_VERSION-dist.zip \
    && bsdtar -xf teiid-wildfly-$TEIID_VERSION-dist.zip \
    && chmod +x $JBOSS_HOME/bin/*.sh \
    && rm teiid-wildfly-$TEIID_VERSION-dist.zip

RUN cd $JBOSS_HOME \
    && curl -O https://oss.sonatype.org/service/local/repositories/releases/content/org/teiid/hal/dist/$TEIID_CONSOLE_VERSION/dist-$TEIID_CONSOLE_VERSION-overlay.zip \
    && bsdtar -xf dist-$TEIID_CONSOLE_VERSION-overlay.zip \
    && rm dist-$TEIID_CONSOLE_VERSION-overlay.zip
    
VOLUME ["$JBOSS_HOME/standalone", "$JBOSS_HOME/domain"]

USER jboss

ENV LAUNCH_JBOSS_IN_BACKGROUND true

# Expose Teiid server  ports 
EXPOSE 8080 9990 31000 35432 

# Run Teiid server and bind to all interface
CMD ["/bin/sh", "-c", "$JBOSS_HOME/bin/standalone.sh -c standalone-teiid.xml -b 0.0.0.0 -bmanagement 0.0.0.0"]
