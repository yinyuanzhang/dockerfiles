# Dockerfile which builds a Docker image for a Jenkins slave.
FROM mprisco/ubuntu-java8-scala

MAINTAINER Michele Prisco <michele.prisco@gmail.com>

RUN apt-get update

# Installs Sudo package
RUN apt-get -y install sudo

# Installs SSH server
RUN apt-get -y install openssh-server
RUN mkdir /var/run/sshd

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# Crates jenkins user
RUN useradd -m -d /home/jenkins -s /bin/bash jenkins && \
    echo "jenkins:jenkins" | chpasswd
RUN echo "jenkins  ALL=(ALL)  ALL" >> etc/sudoers

# Updates package repo and clenup
RUN apt-get update && apt-get clean

# Exposes the standard SSH port
EXPOSE 22

# SSH server is started and it runs in the foreground (not deamon)
CMD ["/usr/sbin/sshd", "-D"]
