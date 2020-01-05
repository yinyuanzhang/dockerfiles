FROM centos
MAINTAINER Angelo E. Valdez <angeloe.valdez@gmail.com>

RUN yum update -y && yum install -y wget
RUN wget --no-cookies --no-check-certificate --header \
"Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" \
"http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm"
RUN  yum localinstall jdk-8u131-linux-x64.rpm -y
ENV JAVA_HOME=/usr/java/latest
ENV JRE_HOME=/usr/java/latest/jre
ENV PATH=$JAVA_HOME/bin:$PATH
RUN rm jdk-8u131-linux-x64.rpm && yum clean all




