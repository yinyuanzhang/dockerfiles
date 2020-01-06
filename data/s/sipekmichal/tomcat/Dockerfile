FROM sipekmichal/java:1.8.0-amazon-corretto-minideb-jessie

LABEL maintainer mich.sipek@gmail.com

ENV TOMCAT_MAJOR=8 \
    TOMCAT_VERSION=8.5.29 \
    TOMCAT_HOME=/usr/local/tomcat \
    CATALINA_HOME=/usr/local/tomcat \
    CATALINA_OUT=/dev/null

ADD http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz /tmp/apache-tomcat.tar.gz
RUN gunzip /tmp/apache-tomcat.tar.gz && \
    tar -C /opt -xf /tmp/apache-tomcat.tar && \
    ln -s /opt/apache-tomcat-${TOMCAT_VERSION} ${TOMCAT_HOME} && \
    rm -rf ${TOMCAT_HOME}/webapps/* && \
    apt-get autoremove --purge -y && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8080
