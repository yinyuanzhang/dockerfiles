########################################################
# This dockerfile will launch an SFTP serveur  via SSHD
########################################################
FROM centos

MAINTAINER Loic Mathieu <loicmathieu@free.fr>

RUN yum -y install openssh-server && rm -rf /var/cache/yum/*

RUN  ssh-keygen -f "/etc/ssh/ssh_host_rsa_key" -N '' -t rsa &&\
     ssh-keygen -f "/etc/ssh/ssh_host_ecdsa_key" -N '' -t ecdsa &&\
     ssh-keygen -f "/etc/ssh/ssh_host_ed25519_key" -N '' -t ed25519

RUN useradd -ms /bin/bash guest && echo 'guest:guest' | chpasswd
RUN echo "root:root" | chpasswd

EXPOSE 22

ENTRYPOINT ["/usr/sbin/sshd", "-D", "-e"]
