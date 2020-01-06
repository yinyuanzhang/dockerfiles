FROM ubuntu:14.04
MAINTAINER Masatoshi Anzawa  "test@test.com"

# Install Packages
RUN apt-get update -y
RUN apt-get install -y openssh-server sudo

# Create user
RUN adduser docker
#RUN passwd -u docker
RUN bash -c 'echo "docker:openstack" | chpasswd'

# setup sudoers
RUN echo "docker    ALL=(ALL)       ALL" >> /etc/sudoers.d/docker

# Init SSHD
RUN mkdir /var/run/sshd
RUN service ssh restart

EXPOSE  22
CMD ["/usr/sbin/sshd", "-D"]

