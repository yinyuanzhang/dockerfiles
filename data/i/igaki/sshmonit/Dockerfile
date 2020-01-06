FROM centos:6.4

MAINTAINER igaki version:0.2

RUN yum update -y

RUN cp -p /usr/share/zoneinfo/Japan /etc/localtime

# install passwd
RUN yum install -y passwd

# Install and basic configure sshd
RUN yum install -y openssh-server

##Monit Install
RUN yum install -y http://pkgs.repoforge.org/monit/monit-5.5-1.el6.rf.x86_64.rpm
ADD ./monit.conf /etc/

#sshd setting
RUN sed -i -e "s/#Port 22/Port 22/g" /etc/ssh/sshd_config
RUN sed -i -e "s/##PermitRootLogin yes/PermitRootLogin yes/g" /etc/ssh/sshd_config
RUN sed -i -e "s/UsePAM yes/#UsePAM yes/g" /etc/ssh/sshd_config
RUN sed -i -e "s/#UsePAM no/UsePAM no/g" /etc/ssh/sshd_config
RUN sed -i -e "s/#MaxStartups 10:30:100/MaxStartups 10:30:100/g" /etc/ssh/sshd_config
RUN echo "NETWORKING=yes" > /etc/sysconfig/network
RUN /etc/init.d/sshd start
RUN echo all:all >> /etc/hosts.allow

ADD ./sshd_monit.conf /etc/monit/conf.d/

RUN chown root:root -R /etc/monit*;chmod 700 /etc/monit.conf

#ssh
EXPOSE 22
#monit
EXPOSE 8001

CMD ["/usr/bin/monit", "-I", "-c", "/etc/monit.conf"]