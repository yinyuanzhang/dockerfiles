FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"

RUN apt-get update && \
    apt-get -y install docker-ce && \
    rm -rf /var/lib/apt/lists/* && \
    curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
    usermod -aG docker jenkins && \
    usermod -aG sudo jenkins && \
    echo "jenkins ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers

USER jenkins
