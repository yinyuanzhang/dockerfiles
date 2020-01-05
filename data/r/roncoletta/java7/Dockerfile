FROM roncoletta/supervisor
MAINTAINER Wagner Roncoletta <wagner.roncoletta@gmail.com>

# wget
RUN apt-get update && \
    apt-get install -y wget

# Java 8
# Instalation Variables
ENV java_version 1.7.0_79
ENV java_zip_name jdk-7u79-linux-x64.tar.gz
ENV download_url http://download.oracle.com/otn-pub/java/jdk/7u79-b15/$java_zip_name

# Accepting the license agreement and download
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" -O /tmp/$java_zip_name $download_url

#COnfigurations
RUN mkdir -p /opt/java && tar -zxf /tmp/$java_zip_name -C /opt/java/
ENV JAVA_HOME /opt/java/jdk$java_version
ENV PATH $JAVA_HOME/bin:$PATH

RUN ls /opt/java/
RUN dir /opt/java/

# configure symbolic links for the java and javac executables
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000 && update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac 20000



