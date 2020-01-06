FROM jenkins/ssh-slave
MAINTAINER Ibnu S Wardy <punyaibun@gmail.com>
LABEL Description="This is a jenkins slave project" Vendor="GITS Indonesia" Version="1.0"

RUN export CLOUD_SDK_REPO="cloud-sdk-stretch" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update -y && apt-get install google-cloud-sdk -y

RUN apt-get install kubectl -y

# Install docker
RUN apt-get install \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     software-properties-common -y
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   stretch \
   stable"
RUN apt-get update -y && apt-get install docker-ce -y
RUN usermod -a -G docker jenkins

# Install Kedge
RUN curl -L https://github.com/kedgeproject/kedge/releases/download/v0.12.0/kedge-linux-amd64 -o kedge && \
    chmod +x kedge && \
    mv ./kedge /usr/local/bin/kedge