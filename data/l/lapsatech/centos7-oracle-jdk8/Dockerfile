FROM centos:7
MAINTAINER "Vadim Isaev" <vadim.o.isaev@gmail.com>
RUN curl -b "oraclelicense=accept-securebackup-cookie" -L -C - -O http://download.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/jdk-8u181-linux-x64.rpm; yum localinstall -y jdk-8u181-linux-x64.rpm; rm -f jdk-8u181-linux-x64.rpm
ENV JAVA_HOME /usr/java/default
ENTRYPOINT ["java"]
