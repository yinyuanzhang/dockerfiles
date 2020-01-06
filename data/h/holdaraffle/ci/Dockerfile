FROM ubuntu:18.04

ENV TERRAFORM_VERSION 0.11.11
ENV NODEJS_VERSION 8.10.0~dfsg-2ubuntu0.4

RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl software-properties-common && \
    (curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -) && \
    (curl -sL https://deb.nodesource.com/setup_8.x | bash -) && \
    (curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -) && \
    (echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list) && \
    (add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable")
RUN apt-get update -y && \
    apt-get install -y python3-pip groff nodejs=${NODEJS_VERSION} yarn git \
                       jq docker-ce nodejs yarn curl build-essential gnupg zip \
                       unzip wget vim
RUN pip3 install awscli --upgrade && \
    pip3 install --upgrade setuptools

# https://askubuntu.com/questions/1036278/npm-is-incorrect-version-on-latest-ubuntu-18-04-installation
RUN npm install -g npm && \
    apt-get purge npm -y && \
    ln -fs /usr/local/bin/npm /bin/npm

RUN mkdir /tmp/terraform && \
    curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -o /tmp/terraform/terraform.zip && \
    cd /tmp/terraform && \
    unzip terraform.zip && \
    mv terraform /bin/terraform && \
    chmod +x /bin/terraform && \
    rm -rf /tmp/terraform

RUN npm install -g expo-cli

ENV PATH=$PATH:/root/bin

WORKDIR /code
