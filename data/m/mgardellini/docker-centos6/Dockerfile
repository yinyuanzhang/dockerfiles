FROM centos:centos6
MAINTAINER Mariano Gardellini <mariano.gardellini@gmail.com>

ENV TOMCAT_MAJOR_VERSION 6
ENV TOMCAT_VERSION 6.0.41

ENV ADMIN_USER tomcat
ENV ADMIN_PASS tomcat

RUN yum install -y java-1.7.0-openjdk-devel.x86_64
RUN yum install -y wget
RUN yum install -y *tar
RUN yum install -y mysql

RUN wget -q http://mirrors.koehn.com/apache/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    tar zxf apache-tomcat-*.tar.gz && \
    rm apache-tomcat-*.tar.gz && \
    mv apache-tomcat* tomcat

ENV JAVA_HOME /usr/lib/jvm/jre-1.7.0-openjdk.x86_64
ENV CATALINA_HOME /tomcat
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin

ADD ./run.sh /usr/local/bin/run
RUN chmod +x /usr/local/bin/run

COPY ./simple-api-1.0.war /tomcat/webapps/

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/run"]
