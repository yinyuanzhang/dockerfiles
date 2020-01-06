FROM ubuntu:18.04

ARG http_proxy=""
ARG https_proxy=""
ARG no_proxy=""

ARG DOCKER_VERSION=18.06.1~ce~3-0~ubuntu
ARG DOCKER_COMPOSE_VERSION=1.22.0
ARG JENKINS_USER="jenkins"
ARG JENKINS_PASSWORD="jenkins"
ARG NVM_VERSION="v0.33.11"

ENV http_proxy=${http_proxy} https_proxy=${https_proxy} no_proxy=${no_proxy}
ENV JENKINS_USER=${JENKINS_USER}
ENV USER=${JENKINS_USER} PASSWORD=${JENKINS_PASSWORD} GROUP=${JENKINS_USER} USER_ID=1000 USER_GID=1000
ENV HOME=/home/${USER}
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# need docker >= 1.12
SHELL ["bash", "--login", "-c"]

RUN apt-get update && \
	apt-get -yqq install \
		# sshd
		openssh-server \
		# docker
		apt-transport-https ca-certificates curl gnupg2 software-properties-common \
		# jenkins
		openjdk-8-jre-headless \
		# sdkman
		zip unzip \
		chromium-browser \
		# locale support (needed e.g. in aws cli with UTF-8 documents)
		locales locales-all \
		&& \
	# aws cli
	# install through apt to set python2.7 as default for python
	apt -y install python-minimal && \
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
	add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(grep 'VERSION_CODENAME' /etc/os-release | cut -d = -f 2) stable" && \
	apt-get update && \
	# needed for aws-sam-cli
	apt-get -yqq install python-dev build-essential && \
	apt-get -yqq install docker-ce=${DOCKER_VERSION} && \
	apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
	locale-gen en_US.UTF-8 && \
	update-locale LANG=en_US.UTF-8

# docker compose
RUN curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
	chmod +x /usr/local/bin/docker-compose

## SSH Connectivity
RUN	mkdir -p /var/run/sshd && \
	groupadd --gid "${USER_GID}" "${USER}" && \
	useradd --uid ${USER_ID} --gid ${USER_GID} --create-home --shell /bin/bash --password ${PASSWORD} ${USER} && \
	echo "${USER}:${PASSWORD}" | chpasswd && \
	echo "IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config && \
	echo ". ${HOME}/.profile" >> /etc/environment

USER ${USER}

WORKDIR ${HOME}

# install SDKMAN
RUN curl -s "https://get.sdkman.io" | sed 's/\.bashrc/\.profile/g' | bash

# install NVM
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/$NVM_VERSION/install.sh | PROFILE=~/.profile bash

# install aws and sam cli
ENV PATH="${HOME}/.local/bin:${PATH}"
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
	python get-pip.py --user && \
	rm get-pip.py && \
	pip install awscli aws-sam-cli --upgrade --user --no-cache-dir

# default user is root and starts sshd
USER root

# Standard SSH port
EXPOSE 22

# Default command, must run as root
CMD ["/usr/sbin/sshd", "-D"]

