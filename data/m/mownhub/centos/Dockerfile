FROM centos:latest
MAINTAINER Feng Honglin <hfeng@tutum.co>

RUN yum -y install openssh-server epel-release && \
    yum -y install pwgen && \
    rm -f /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key && \
    ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \
    sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
    sed -i "s/UsePAM.*/UsePAM yes/g" /etc/ssh/sshd_config
RUN yum install -y git gcc net-tools make subversion libpcap openssl wget unzip lrzsz screen
RUN rpm -vhU https://nmap.org/dist/nmap-7.12-1.x86_64.rpm
RUN wget https://github.com/sqlmapproject/sqlmap/zipball/master && unzip master && rm -rf master && mv sqlmapproject-sqlmap-*/ sqlmap
ADD set_root_pw.sh /set_root_pw.sh
ADD run.sh /run.sh
RUN chmod +x /*.sh

ENV AUTHORIZED_KEYS **None**

EXPOSE 22
CMD ["/run.sh"]
