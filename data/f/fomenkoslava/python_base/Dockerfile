FROM centos:7

RUN yum update -y && yum clean all
RUN yum install -y yum-utils
RUN yum-config-manager --enable cr
RUN yum install -y epel-release
RUN yum install -y python-pip
RUN yum install -y python-setuptools
RUN yum install -y nginx

RUN yum install -y python-devel
RUN yum install -y supervisor

RUN yum install -y rabbitmq-server
RUN yum install -y postgresql-devel
RUN yum install -y openssl-devel
RUN yum install -y libffi-devel
RUN yum install -y libxml2-devel
RUN yum install -y libxslt-devel
RUN yum install -y gcc
RUN yum install -y python-devel
RUN yum install -y mysql-devel
RUN yum install -y postgresql-libs
RUN yum install -y unixODBC

RUN yum install -y libjpeg-devel
RUN yum install -y git
RUN pip install uwsgi

# Install Cron
RUN yum install -y cronie

# Set work directory
ENV DIRPATH /home/docker/code/

ADD ./req.txt /home/docker/code/req.txt

# Set local IP
RUN yum install -y iproute

# setup all the configfiles
RUN mkdir /etc/nginx/sites-enabled/
RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.default
RUN ln -s /home/docker/code/docker/conf/nginx.conf /etc/nginx/
RUN ln -s /home/docker/code/docker/conf/nginx-app.conf /etc/nginx/sites-enabled/
RUN ln -s /home/docker/code/docker/conf/supervisor-app.conf /etc/supervisord.d/supervisor-app.ini

RUN mkdir /var/log/uwsgi/

# Install unrar
ADD ./unrar-5.0.3-1.el7.rf.x86_64.rpm /
RUN rpm -Uvh unrar-5.0.3-1.el7.rf.x86_64.rpm

# Install 7zip
RUN yum install -y p7zip p7zip-plugins

RUN pip install -r /home/docker/code/req.txt
RUN localedef -i en_US -f UTF-8 en_US.UTF-8
