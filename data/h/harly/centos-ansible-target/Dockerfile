FROM centos:latest
MAINTAINER harly

RUN yum -y upgrade

# Set up OpenSSH Server
RUN yum -y install openssh-server 
RUN mkdir /var/run/sshd
RUN /usr/bin/ssh-keygen -A

# Install dependencies
RUN yum -y install openssl 
RUN yum -y install sudo 
RUN yum -y install python

# Add User "ansible" with password "ansible" and sudo rights
RUN useradd -ms /bin/bash -G wheel -p $(openssl passwd -1 ansible) ansible

# Expose port 22
EXPOSE 22

# Servicecommand that keeps the container running
CMD ["/usr/sbin/sshd", "-D"]
