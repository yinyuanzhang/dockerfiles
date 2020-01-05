FROM centos
MAINTAINER danarox

############SUPERVISOR--Configuración##################
RUN \
yum update -y && \
yum install -y epel-release && \
yum install -y iproute python-setuptools hostname inotify-tools yum-utils which jq && \
easy_install supervisor

RUN \
yum clean all && rm -rf /tmp/yum*

ENV USER=danarox
ENV PASSWORD=Truger250

EXPOSE 9001 80
ADD container-files /

RUN \
sed -ri "s/www/${USER}/g" /etc/supervisord.conf && \
sed -ri "s/iaw/${PASSWORD}/g" /etc/supervisord.conf

RUN yum -y install httpd
RUN systemctl enable httpd

RUN rpm -Uvh --replacepkgs https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

RUN yum install -y php56w php56w-opcache php56w-mysql php56w-iconv php56w-mbstring php56w-curl php56w-openssl php56w-tokenizer php56w-soap php56w-ctype php56w-zip php56w-gd php56w-simplexml php56w-spl php56w-pcre php56w-dom php56w-xml php56w-intl php56w-json php56w-ldap php56w-pecl-apcu php56w-odbc php56w-pear php56w-xmlrpc php56w-snmp php56w-pdo curl

RUN yum install -y ghostscript


ENTRYPOINT ["/config/bootstrap.sh"]
