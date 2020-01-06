FROM centos:6.10

ADD jdk1.8.0_211 /opt/jdk1.8.0_211/
RUN chmod +x /opt/jdk1.8.0_211/bin/java

USER root
RUN groupadd daksa -g 1000 && useradd -u 1000 -g daksa -m -d /home/daksa -s /sbin/nologin -c "jboss user" daksa 


#Set zone time to WIB
RUN rm /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Jakarta /etc/localtime


USER daksa
ENV JAVA_HOME /opt/jdk1.8.0_211
ENV PATH ${PATH}:${JAVA_HOME}/bin

#NOTE : This docker file tagged with daksa/java:v8

