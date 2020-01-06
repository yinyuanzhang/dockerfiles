FROM centos:7
MAINTAINER hebskjcc
RUN python && whoami && pwd && yum update -y && yum install -y wget python dbus openssh
ADD install.sh /root/
ADD sshd_config /etc/ssh/
RUN cd /root/ && bash install.sh
EXPOSE 888
EXPOSE 8888
EXPOSE 80

