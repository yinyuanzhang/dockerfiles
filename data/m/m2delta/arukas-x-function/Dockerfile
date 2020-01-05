FROM centos:7.4.1708

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm

RUN yum -y upgrade
RUN yum -y install nginx

RUN yum -y install git

WORKDIR /usr/share/nginx/
RUN cd /usr/share/nginx/
RUN git clone https://github.com/ProjectEuropa/Arukas-x-function.git files

RUN mv /usr/share/nginx/files/* /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]