FROM openjdk:6b38-jdk

# download the jdk 6 version of JBoss AS 5

# Set the WILDFLY_VERSION env variable
ENV JBOSS_VERSION JBoss-5.1.0.GA
ENV JBOSS_FILENAME jboss-5.1.0.GA-jdk6.zip
ENV JBOSS_SHA1 0906717eec83d57a3fdbdf090555cac036bffc6d
ENV JBOSS_HOME /opt/jboss

# Add the WildFly distribution to /opt, and make wildfly the owner of the extracted tar content
# Make sure the distribution is available from a well-known place
RUN cd $HOME \
&& curl -O https://iweb.dl.sourceforge.net/project/jboss/JBoss/$JBOSS_VERSION/$JBOSS_FILENAME \
&& sha1sum ${JBOSS_FILENAME} | grep ${JBOSS_SHA1} \
&& unzip $JBOSS_FILENAME \
&& mv ${HOME}/jboss-5.1.0.GA $JBOSS_HOME \
&& rm $JBOSS_FILENAME

# Ensure signals are forwarded to the JVM process correctly for graceful shutdown
ENV LAUNCH_JBOSS_IN_BACKGROUND true

WORKDIR $JBOSS_HOME

# overwrite profile.xml to resolve JRE incompatability problem
# without patch wrong constructor is used
# java.lang.IllegalArgumentException: Wrong arguments. new for target java.lang.reflect.Constructor expected=[java.net.URI] actual=[java.io.File]
# see https://issues.jboss.org/browse/JBAS-6981
COPY profile.xml ${JBOSS_HOME}/server/default/conf/bootstrap/profile.xml

# Expose the ports we're interested in
EXPOSE 8080

# Set the default command to run on boot and bind to all interface
CMD ["/opt/jboss/bin/run.sh", "-b", "0.0.0.0"]
