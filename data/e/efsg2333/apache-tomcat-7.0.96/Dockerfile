FROM openjdk:11.0.5-jdk
MAINTAINER june

WORKDIR  /

ADD http://apache.stu.edu.tw/tomcat/tomcat-7/v7.0.96/bin/apache-tomcat-7.0.96.tar.gz /

RUN tar zxvf apache-tomcat-7.0.96.tar.gz

CMD ["/apache-tomcat-7.0.96/bin/catalina.sh", "run"]

EXPOSE 8080