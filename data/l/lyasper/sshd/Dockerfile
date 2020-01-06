FROM centos:centos7

RUN yum -y update
RUN yum -y install openssh-server passwd
ADD ./start.sh /start.sh
RUN mkdir /var/run/sshd
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' 

RUN yum -y install bash sudo
RUN yum clean all 
RUN chmod 755 /start.sh
RUN ./start.sh gpadmin changeme
CMD  ["/usr/sbin/sshd", "-D"]
