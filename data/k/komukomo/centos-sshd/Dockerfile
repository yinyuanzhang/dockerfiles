FROM centos:6.7
MAINTAINER komukomo <komukomo@users.noreply.github.com>

RUN yum install -y openssh-server openssh-clients
RUN echo 'root:root' | chpasswd
RUN sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN /sbin/service sshd start && /sbin/service sshd stop

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
