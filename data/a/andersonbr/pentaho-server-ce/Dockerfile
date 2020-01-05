FROM openjdk:8

MAINTAINER Anderson Calixto andersonbr@gmail.com

# Init ENV
ENV BISERVER_VERSION 8.2
ENV BISERVER_TAG 8.2.0.0-342
ENV PENTAHO_HOME /opt/pentaho

# Apply JAVA_HOME
RUN . /etc/environment
ENV PENTAHO_JAVA_HOME $JAVA_HOME
ENV PENTAHO_JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-amd64
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-amd64

# Install Dependences
RUN apt-get update; apt-get install zip -y; \
apt-get install wget unzip git -y; \
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*;
RUN mkdir ${PENTAHO_HOME};
# Download Pentaho BI Server
RUN /usr/bin/wget --progress=dot:giga \
"http://downloads.sourceforge.net/project/pentaho/Pentaho%20${BISERVER_VERSION}/server/pentaho-server-ce-${BISERVER_TAG}.zip" \
-O /tmp/pentaho-server-ce-${BISERVER_TAG}.zip; \
/usr/bin/unzip -q /tmp/pentaho-server-ce-${BISERVER_TAG}.zip -d $PENTAHO_HOME; \
rm -f /tmp/pentaho-server-ce-${BISERVER_TAG}.zip $PENTAHO_HOME/pentaho-server/promptuser.sh; \
sed -i -e 's/\(exec ".*"\) start/\1 run/' $PENTAHO_HOME/pentaho-server/tomcat/bin/startup.sh; \
chmod +x $PENTAHO_HOME/pentaho-server/start-pentaho.sh
RUN useradd -s /bin/bash -d ${PENTAHO_HOME} pentaho; chown -R pentaho:pentaho ${PENTAHO_HOME};

#Always non-root user
USER pentaho
WORKDIR /opt/pentaho
EXPOSE 8080

CMD ["sh", "/opt/pentaho/pentaho-server/start-pentaho.sh"]
