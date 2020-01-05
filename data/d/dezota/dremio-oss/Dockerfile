FROM centos:latest
MAINTAINER bholman@dezota.com

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && yum install -y nano cronie wget which sudo lsof strace htop joe vnstat iftop initscripts; yum clean all

RUN useradd -ms /bin/bash  dremio

RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u172-b11/a58eab1ec242421181065cdc37240b08/jdk-8u172-linux-x64.rpm \
 && yum localinstall -y jdk-8u172-linux-x64.rpm && rm -rf jdk*.rpm; yum clean all

RUN wget https://download.dremio.com/community-server/2.0.5-201806021755080191-767cfb5/dremio-community-2.0.5-201806021755080191_767cfb5_1.noarch.rpm \
 && yum localinstall -y dremio*.rpm \
 && rm -rf dremio*.rpm

RUN chkconfig --level 3456 dremio on
 
COPY dremio.sh /dremio.sh
RUN chmod +x /dremio.sh

EXPOSE 2181 9047 31010 45678

ENTRYPOINT ["/dremio.sh"]
