FROM centos:7
MAINTAINER levkov

RUN rm -f /etc/localtime && ln -sf /usr/share/zoneinfo/UTC /etc/localtime
RUN yum update -y && \
    yum install -y wget
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN rpm -ivh epel-release-latest-7.noarch.rpm
RUN yum install -y openssh-server openssh-clients python-pip
RUN pip install --upgrade pip
RUN pip install requests==2.5.3 supervisor

RUN rm -f /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key && \
    ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \
    sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
    sed -i "s/UsePAM.*/UsePAM yes/g" /etc/ssh/sshd_config

RUN echo 'root:ContaineR' | chpasswd

COPY conf/supervisord.conf /etc/supervisord.conf
EXPOSE 9001 22
CMD ["/usr/bin/supervisord"]
