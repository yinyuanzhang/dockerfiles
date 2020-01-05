FROM maven:3.6-jdk-8

MAINTAINER Maximilian Schmitt

RUN apt-get update \
	&& apt-get install -y jq python-pip curl apt-transport-https \
	&& apt-get clean \
	&& pip install awscli

RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update && apt-get install -y kubectl && apt-get clean
RUN curl -L https://git.io/get_helm.sh | bash
RUN mkdir /root/.kube

RUN curl -sL https://deb.nodesource.com/setup_13.x | bash - \
  && apt-get install -y nodejs git ssh

RUN node -v

RUN npm install -g yarn
