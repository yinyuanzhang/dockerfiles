FROM centos:7.4.1708

MAINTAINER iceyao

ENV COBBLER_VERSION 2.8.2

RUN yum -y install wget epel-release && \
wget -O /etc/yum.repos.d/cobbler28.repo http://download.opensuse.org/repositories/home:/libertas-ict:/cobbler28/CentOS_7/home:libertas-ict:cobbler28.repo && \
yum -y install cobbler tftp-server dhcp openssl cobbler-web supervisor && \
yum -y update && \
yum clean all

ADD loaders.tar.xz /var/lib/cobbler/loaders/
ADD supervisord.d/conf.ini /etc/supervisord.d/conf.ini
ADD start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
