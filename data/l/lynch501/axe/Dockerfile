# Use an official Python runtime as a parent image
FROM ubuntu:16.04

MAINTAINER David Lynch

ENV TF_VER 0.11.11

ENTRYPOINT "bash"

# Install Ansible
RUN apt-get update && \
    apt-get install --no-install-recommends -y software-properties-common && \
    apt-add-repository ppa:ansible/ansible && \
    apt-get update && \
    apt-get install -y ansible

# Install AXE
RUN apt-get update && apt-get install -y \
    openssh-server \
    git \
    libkrb5-dev \
    python-gssapi \
    python-kerberos \
    python-requests-kerberos \
    python-simplejson \
    bash-completion \
    python-pip \
    virtualenv \
    git \
    jq \
    graphviz \
    build-essential \
    libssl-dev \
    python-dev \ 
    bsdmainutils \
    vim \
    curl \
    unzip && rm -rf /var/lib/apt/lists/*

# Install Chef Inspec
RUN curl https://omnitruck.chef.io/install.sh | bash -s -- -P inspec

ENV AXE_ROOT=/axe
ENV AXE_PATH=/axe

RUN /bin/bash -c "git clone https://bitbucket.org/kxseven/axe.git && cd $AXE_ROOT; virtualenv $AXE_ROOT/local/python; source $AXE_ROOT/etc/axerc; pip install --trusted-host pypi.python.org -r $AXE_ROOT/requirements/requirements.python2" && sed -i 's/3600/28800/g' $AXE_ROOT/etc/functions.d/05-aws-credentials-loader.sh
RUN /bin/bash -c "wget https://releases.hashicorp.com/terraform/${TF_VER}/terraform_${TF_VER}_linux_amd64.zip && \
	          unzip terraform_${TF_VER}_linux_amd64.zip -d /usr/bin"
# Set the working directory to /axe
WORKDIR /axe

COPY config/bashrc /root/.bashrc
