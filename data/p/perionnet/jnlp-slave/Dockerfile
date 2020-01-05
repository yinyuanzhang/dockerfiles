FROM jenkins/jnlp-slave
MAINTAINER Maayan Yosef <maayan@perion.com>
LABEL Description="This is a base image, which allows connecting Jenkins agents via JNLP protocols" Vendor="Jenkins project" Version="3.19"
USER root

#Ansible
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" | tee -a /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
RUN apt-get update
RUN apt-get install apt-utils ansible jq apt-transport-https -y
#AWSCLI
RUN apt-get install python-pip -y && pip install awscli
#boto
RUN pip install boto boto3 dyn
#Helm
RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash
#Terraform
RUN curl -O https://releases.hashicorp.com/terraform/0.11.7/terraform_0.11.7_linux_amd64.zip && unzip terraform_0.11.7_linux_amd64.zip -d /usr/bin/
#Kubectl  
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && touch /etc/apt/sources.list.d/kubernetes.list && echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list && apt-get update && apt-get install -y kubectl
#Docker  
RUN curl -fsSL get.docker.com -o get-docker.sh
RUN sh get-docker.sh
RUN usermod -aG docker root  
ENTRYPOINT ["jenkins-slave"]
