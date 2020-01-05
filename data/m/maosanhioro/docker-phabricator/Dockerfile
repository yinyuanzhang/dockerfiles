# VERSION   0.1
# DOCKER-VERSION  1.4.1
#

FROM centos:centos6
MAINTAINER maosanhioro <maosanhioro@gmail.com>

RUN yum update -y
RUN yum install -y wget git

# Repository (epel, remi)
RUN wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm;\
    wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm;\
    rpm -ivh epel-release-6-8.noarch.rpm remi-release-6.rpm

# Apache, PHP, MySQL
RUN yum --enablerepo=remi,remi-php55 install -y httpd php php-cli php-common php-devel php-gd php-mbstring php-mcrypt php-opcache php-pecl-apcu php-pdo php-process php-mysqlnd mysql-server
ADD ./phabricator.conf /etc/httpd/conf.d/phabricator.conf

# Supervisor
RUN curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
RUN pip install supervisor
RUN mkdir -p /var/log/supervisor
ADD ./supervisord.conf /etc/supervisord.conf

RUN mkdir /usr/share/phabricator
WORKDIR /usr/share/phabricator

# Phabricator
RUN git clone https://github.com/phacility/libphutil.git;\
    cd libphutil && git pull --rebase
RUN git clone https://github.com/phacility/arcanist.git;\
    cd arcanist && git pull --rebase
RUN git clone https://github.com/phacility/phabricator.git;\
    cd phabricator && git pull --rebase

ADD ./setup.sh /opt/setup.sh

EXPOSE 9000
CMD ["/usr/bin/supervisord"]
