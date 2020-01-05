# This Dockerfile is used to build an image containing basic stuff to be used as a Jenkins slave build node.

FROM ubuntu:xenial
MAINTAINER Stephane Boisvert <stephane.boisvert@lyntoo.com>

# Make sure the package repository is up to date.
RUN apt-get update
RUN apt-get -y upgrade

# Install a basic SSH server
RUN apt-get install -y openssh-server
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd

RUN apt-get install -y openjdk-8-jdk git ca-certificates sudo aptitude uuid-runtime python-dib-utils python-yaml curl apt-transport-https iptables


RUN curl -sSL https://get.docker.com/ | sh

# Add user jenkins to the image
RUN adduser --quiet jenkins
# Set password for the jenkins user (you may want to alter this).
RUN echo "jenkins:jenkins" | chpasswd
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

COPY id_rsa.pub /home/jenkins/.ssh/authorized_keys
RUN chown -R jenkins:jenkins /home/jenkins/.ssh


ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

RUN apt-get clean

# Standard SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
CMD wrapdocker 
