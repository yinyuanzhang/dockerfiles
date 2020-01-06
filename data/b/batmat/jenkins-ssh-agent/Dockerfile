FROM openjdk:11-jdk
MAINTAINER Baptiste Mathus <batmat@batmat.net>

RUN apt-get update -y && \
    apt-get -y upgrade && \
    apt-get install -y \
                        git \
                        subversion \
                        openssh-server && \
    apt-get clean

# Configure the SSH server
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd

# TODO: add Docker CLI
RUN cd /tmp && \
    wget --quiet https://download.docker.com/linux/static/stable/x86_64/docker-17.12.1-ce.tgz --output-document /tmp/docker.tar.gz && \
    tar xvzf docker.tar.gz && \
    mv docker/* /usr/local/bin && \
    rmdir docker && \
    rm docker.tar.gz

# Add user jenkins/jenkins to the image
RUN adduser --quiet jenkins
RUN echo "jenkins:jenkins" | chpasswd

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
