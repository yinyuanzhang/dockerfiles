FROM java:7 

MAINTAINER CesarDraw cesardraw@gmail.com 

# Init ENV 
ENV BISERVER_VERSION 5.4 
ENV BISERVER_TAG 5.4.0.1-130 
ENV PENTAHO_HOME /opt/pentaho 

# Apply JAVA_HOME 
RUN . /etc/environment 
ENV PENTAHO_JAVA_HOME $JAVA_HOME 
ENV PENTAHO_JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64 
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64 

# Install Dependences 
RUN apt-get update; apt-get install zip -y; apt-get install wget unzip git -y; apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; 
RUN mkdir ${PENTAHO_HOME}; 

# Download Pentaho BI Server 
RUN /usr/bin/wget --progress=dot:giga http://downloads.sourceforge.net/project/pentaho/Business%20Intelligence%20Server/${BISERVER_VERSION}/biserver-ce-${BISERVER_TAG}.zip -O /tmp/biserver-ce-${BISERVER_TAG}.zip; /usr/bin/unzip -q /tmp/biserver-ce-${BISERVER_TAG}.zip -d $PENTAHO_HOME; rm -f /tmp/biserver-ce-${BISERVER_TAG}.zip $PENTAHO_HOME/biserver-ce/promptuser.sh; sed -i -e 's/(exec ".*") start/1 run/' $PENTAHO_HOME/biserver-ce/tomcat/bin/startup.sh; chmod +x $PENTAHO_HOME/biserver-ce/start-pentaho.sh 

RUN useradd -s /bin/bash -d ${PENTAHO_HOME} pentaho; chown -R pentaho:pentaho ${PENTAHO_HOME}; 

#Always non-root user 
USER pentaho 
WORKDIR /opt/pentaho 

EXPOSE 8080 
CMD ["sh", "/opt/pentaho/biserver-ce/start-pentaho.sh"]
