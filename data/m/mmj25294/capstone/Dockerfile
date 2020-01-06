FROM centos:latest
COPY . var/www/html
RUN yum -y --setopt=tsflags=nodocs update
RUN yum clean all
RUN yum install wget -y
RUN wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
RUN rpm -ivh mysql-community-release-el7-5.noarch.rpm
RUN yum -y install mysql-server
RUN systemctl enable mysqld.service
RUN yum -y --setopt=tsflags=nodocs install httpd
RUN systemctl enable httpd.service
EXPOSE 80
EXPOSE 8080
