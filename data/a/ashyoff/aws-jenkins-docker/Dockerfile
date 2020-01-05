FROM jenkins/jenkins:lts

MAINTAINER ashyoff <no.where@hell.com>

USER root
RUN apt-get update && \
    apt-get -y install apt-transport-https \
         ca-certificates \
         curl \
         vim \
         groff \
         gnupg2 \
         software-properties-common && \
    curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey && \
    add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
       $(lsb_release -cs) \
       stable" && \
    apt-get update && \
    apt-get -y install docker-ce && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py && \
    pip install awscli && \
    mv /etc/init.d/docker /etc/init.d/docker_bak && \
    groupmod -g 497 docker && \
    usermod -a -G docker jenkins

USER jenkins
