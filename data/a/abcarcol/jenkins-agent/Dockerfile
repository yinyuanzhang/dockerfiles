FROM ubuntu:16.04
MAINTAINER Abel Carrion <abcarcol@gmail.com> based on bibinwilson/jenkins-docker-slave Bibin Wilson <bibinwilsonn@gmail.com>

# Make sure the package repository is up to date.
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y git
# Install a basic SSH server
RUN apt-get install -y openssh-server
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd

# Install JDK 8 (latest edition)
RUN apt-get install -y openjdk-8-jdk

# Add user jenkins to the image
RUN adduser --quiet jenkins
# Set password for the jenkins user (you may want to alter this).
RUN echo "jenkins:jenkins" | chpasswd

#Install python3.6 and pip3
#apt-get install -y python3.6 
RUN apt-get install -y python3-pip

# Standard SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
