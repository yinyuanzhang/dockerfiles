FROM centos/httpd-24-centos7
USER root
RUN yum -y install wget zip unzip bzip2 
RUN yum -y install tar 
RUN yum -y install rsync
RUN yum -y groupinstall "Development Tools"
RUN yum -y update
USER 1001