FROM centos:6

MAINTAINER Onno Lissenberg "https://github.com/orlissenberg"

ENV DEBIAN_FRONTEND=noninteractive

RUN yum install epel-release -y
RUN yum update -y
RUN yum install python git python-pip python-simplejson python-devel -y

RUN yum install openssh-server -y
RUN mkdir /var/run/sshd

RUN echo 'root:root' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN /etc/init.d/sshd restart

CMD    ["/usr/sbin/sshd", "-D"]

EXPOSE 22
