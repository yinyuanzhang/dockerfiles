FROM ubuntu:14.04.1

RUN \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.utf8 && \

    apt-get update -q && \
    apt-get install -qy software-properties-common

RUN apt-get install openjdk-7-jdk -qy

RUN \
    apt-get install -qy \
        poppler-utils \
        wget \
        && \
    apt-get clean

ENV TOMCAT_VERSION 7.0.94
ENV MAVEN_VERSION 3.6.0

RUN \
    cd /usr/lib && \
    wget http://mirror.ibcp.fr/pub/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
    tar -xzf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
    rm apache-maven-$MAVEN_VERSION-bin.tar.gz && \
    ln -s /usr/lib/apache-maven-$MAVEN_VERSION/bin/mvn /usr/bin/mvn && \
    wget http://apache.mediamirrors.org/tomcat/tomcat-7/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz && \
    tar -xzf apache-tomcat-$TOMCAT_VERSION.tar.gz && \
    rm apache-tomcat-$TOMCAT_VERSION.tar.gz && \
    rm -rf /usr/lib/apache-tomcat-$TOMCAT_VERSION/webapps/*

ADD mergepdf.config.json /etc/mergepdf.config.json
ADD src/ /work/

RUN \
    cd /work/ && \
    export MAVEN_OPTS="-Xmx128m" && \
    mvn install -Prelease && \
    cp target/merge-pdf.war /usr/lib/apache-tomcat-$TOMCAT_VERSION/webapps/ROOT.war

RUN apt-get install iptables -qy

CMD /usr/lib/apache-tomcat-$TOMCAT_VERSION/bin/catalina.sh run
