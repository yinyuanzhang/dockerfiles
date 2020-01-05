FROM centos:7.5.1804
MAINTAINER Richard <nibocn@gmail.com>

ARG JAVA_VERSION=8u171

RUN cd /tmp \
    && mkdir -p /opt/java \
    && curl -o jdk-${JAVA_VERSION}-linux-x64.tar.gz -L -O -H "Cookie: oraclelicense=accept-securebackup-cookie" -k "http://ftp.wsisiz.edu.pl/pub/pc/pozyteczne%20oprogramowanie/java/${JAVA_VERSION}/jdk-${JAVA_VERSION}-linux-x64.tar.gz" \
    && tar xf jdk-${JAVA_VERSION}-linux-x64.tar.gz -C /opt/java \
    && rm -rf jdk-${JAVA_VERSION}-linux-x64.tar.gz \
    && ln -s /opt/java/jdk* /opt/java/jdk \
    && ln -s /opt/java/jdk /opt/java/jvm \
    && ln -s /opt/java/jdk/bin/java /usr/local/bin \
    && ln -s /opt/java/jdk/bin/javac /usr/local/bin

ENV JAVA_HOME /opt/java/jdk
ENV PATH $JAVA_HOME/bin:$PATH
