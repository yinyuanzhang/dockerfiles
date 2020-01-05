
FROM ubuntu:14.10

MAINTAINER Larry Liang <ptolemy428@gmail.com>

RUN DEBIAN_FRONTEND=noninteractive apt-get -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install wget vim openvpn openssh-client curl
#RUN DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor
#ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#download jq
RUN wget -O /usr/local/bin/jq http://stedolan.github.io/jq/download/linux64/jq
RUN chmod 700 /usr/local/bin/jq

RUN cat '/etc/init.d/openvpn start' >> /root/.bashrc
