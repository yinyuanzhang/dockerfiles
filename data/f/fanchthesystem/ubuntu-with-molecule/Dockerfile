from ubuntu:latest

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get -y -o Acquire::GzipIndexes=false update && apt-get -y upgrade && apt-get -y clean

## DOCKER

RUN apt-get -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

RUN apt-get -y update

RUN apt-get -y install docker-ce docker-ce-cli containerd.io

## PYTHON

RUN apt-get -y install python python-dev python-pip python-setuptools python-setuptools-scm python-virtualenv python-pkg-resources

# PYTHON3

RUN apt-get -y install python3 python3-dev python3-pip python3-setuptools python3-setuptools-scm python3-virtualenv python3-pkg-resources

RUN pip3 install -U ansible molecule docker

## ANSIBLE

ENV ANSIBLE_LOAD_CALLBACK_PLUGINS=1

ENV ANSIBLE_STDOUT_CALLBACK=debug

ENV ANSIBLE_ROLES_PATH=/etc/ansible/roles

RUN mkdir -p $ANSIBLE_ROLES_PATH

# as ansible-galaxy does not allow update without force

# COPY requirements.yml $ANSIBLE_ROLES_PATH/

# RUN ansible-galaxy install -r $ANSIBLE_ROLES_PATH/requirements.yml
