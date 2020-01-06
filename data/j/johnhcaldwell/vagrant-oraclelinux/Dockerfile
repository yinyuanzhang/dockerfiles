# Oracle Linux 5 configured for Vagrant
# http://github.com/johnhcaldwell/vagrant-docker-oraclelinux
# docker pull johnhcaldwell/vagrant-oraclelinux:5
FROM oraclelinux:5
MAINTAINER John Caldwell "john.caldwell@oracle.com"

# Install sudo and curl
RUN yum -y install sudo curl.x86_64 &&  yum -y clean all && rm -rf /var/cache/yum/*

# Fix sshd PAM config to work properly under docker
RUN sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional pam_loginuid.so/' /etc/pam.d/sshd

# Sudo configuration and fixes
RUN echo 'vagrant ALL=NOPASSWD: ALL' >> /etc/sudoers
RUN sed -ri 's/^Defaults.*requiretty/#Defaults requiretty/' /etc/sudoers

# Create and configure vagrant user
RUN useradd --create-home -s /bin/bash vagrant
RUN echo 'vagrant:vagrant' | chpasswd
RUN echo 'root:vagrant' | chpasswd

# Install vagrant key
RUN mkdir /home/vagrant/.ssh
ADD https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub /home/vagrant/.ssh/authorized_keys
RUN chmod 0600 /home/vagrant/.ssh/authorized_keys
RUN chown -R vagrant:vagrant /home/vagrant/.ssh
RUN chmod 0700 /home/vagrant/.ssh

EXPOSE 22

ADD bin/my_init /sbin/my_init
RUN chmod 0750 /sbin/my_init
CMD ["/sbin/my_init"]
