FROM centos:7

EXPOSE 8080
EXPOSE 8443

ENV DB_Type derby
ENV DB_Host localhost
ENV DB_Name mirthdb
ENV DB_User mirth
ENV DB_Password mirth

VOLUME /opt/mirthconnect/appdata

#COPY run.sh /root/bin/run.sh
ADD "http://downloads.mirthcorp.com/connect/3.8.1.b246/mirthconnect-3.8.1.b246-linux.rpm" "/tmp/mirth.rpm"

RUN yum install java-1.8.0-openjdk -y && \
yum localinstall /tmp/mirth.rpm -y && \
yum clean all && \
rm /tmp/* -rf 
#chmod 700 /root/bin/run.sh

#ENTRYPOINT /root/bin/run.sh
ENTRYPOINT /opt/mirthconnect/mcserver
