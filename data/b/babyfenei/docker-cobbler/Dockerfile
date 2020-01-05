FROM centos:7.6.1810

MAINTAINER Jasonli

ENV COBBLER_VERSION 2.8.4

RUN yum -y install wget epel-release && \
    wget -O /etc/yum.repos.d/cobbler28.repo http://download.opensuse.org/repositories/home:/libertas-ict:/cobbler28/CentOS_7/home:libertas-ict:cobbler28.repo && \
    yum -y install cobbler tftp-server dhcp openssl cobbler-web supervisor && \
    yum -y update && \
    yum clean all

ENV SERVER_IP=192.168.1.1 \
    ROOT_PASSWORD=admin@123 \
    DHCP_RANGE=192.168.1.2-192.168.1.254 \
    DHCP_SUBNET=192.168.1.0 \
    DHCP_ROUTER=192.168.1.1 \
    DHCP_DNS=114.114.114.114

ADD supervisord.d/conf.ini /etc/supervisord.d/conf.ini
ADD start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]
VOLUME ["/mnt"]

EXPOSE 69
EXPOSE 80
EXPOSE 443
EXPOSE 25151
