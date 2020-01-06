FROM ubuntu:18.04

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

#=====================
# JAVA + Git + Python/Pip + wget/curl
# @see https://github.com/cloudbees/java-build-tools-dockerfile/blob/master/Dockerfile
#=====================

#================================================
# Customize sources for apt-get
#================================================
RUN DISTRIB_CODENAME=$(cat /etc/*release* | grep DISTRIB_CODENAME | cut -f2 -d'=') \
    && echo "deb http://archive.ubuntu.com/ubuntu ${DISTRIB_CODENAME} main universe\n" > /etc/apt/sources.list \
    && echo "deb http://archive.ubuntu.com/ubuntu ${DISTRIB_CODENAME}-updates main universe\n" >> /etc/apt/sources.list \
    && echo "deb http://security.ubuntu.com/ubuntu ${DISTRIB_CODENAME}-security main universe\n" >> /etc/apt/sources.list

RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install software-properties-common \
  && add-apt-repository -y ppa:git-core/ppa

#========================
# Packages:
# OpenJDK8
# groff is for aws-cli
# tree is convenient for troubleshooting builds
# Python (2.7)
#========================
RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    openssh-client \
    ca-certificates \
    openjdk-8-jdk \
    tar zip unzip \
    wget curl \
    git \
    jq \
    less tree \
    python python-pip \
    groff \
    gosu \
    rubygems \
  && rm -rf /var/lib/apt/lists/* \
  && sed -i 's/securerandom\.source=file:\/dev\/random/securerandom\.source=file:\/dev\/urandom/' ./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security
    
# workaround https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=775775
RUN [ -f "/etc/ssl/certs/java/cacerts" ] || /var/lib/dpkg/info/ca-certificates-java.postinst configure
RUN pip install --upgrade pip setuptools

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

#========================================
# Docker
#========================================

ENV DOCKER_CHANNEL stable
ENV DOCKER_VERSION 18.06.3-ce
ENV DOCKER_ARCH x86_64

RUN if ! curl -fL -o docker.tgz "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${DOCKER_ARCH}/docker-${DOCKER_VERSION}.tgz"; then \
		echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from '${DOCKER_CHANNEL}' for '${DOCKER_ARCH}'"; \
		exit 1; \
	fi; \
	\
	tar --extract \
		--file docker.tgz \
		--strip-components 1 \
		--directory /usr/bin/ \
	; \
	rm docker.tgz;

#========================================
# Add Jenkins User
#========================================
ENV JENKINS_HOME=/home/jenkins

RUN adduser --quiet --home $JENKINS_HOME --shell /bin/bash jenkins \
  && echo "jenkins:jenkins" | chpasswd

RUN touch $JENKINS_HOME/.profile && \
    chown jenkins /home/jenkins/.profile

#==================
# Slave setup
#==================

ARG JENKINS_REMOTING_VERSION=3.29

# See https://github.com/jenkinsci/docker-slave/blob/2.62/Dockerfile#L32
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/$JENKINS_REMOTING_VERSION/remoting-$JENKINS_REMOTING_VERSION.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/slave.jar
  
COPY jenkins-slave entry-point /usr/local/bin/
COPY logging.properties /usr/share/jenkins/logging.properties

RUN chmod a+rwx $JENKINS_HOME
RUN ["chmod", "+x", "/usr/local/bin/entry-point", "/usr/local/bin/jenkins-slave"]
WORKDIR ${JENKINS_HOME}

ENTRYPOINT ["/usr/local/bin/entry-point", "/usr/local/bin/jenkins-slave"]

#===================
# AWS CLI
#===================

USER jenkins
RUN pip install awscli --upgrade --user
# Add pip installs to path
ENV PATH=${PATH}:${JENKINS_HOME}/.local/bin

#======
# NVM 
#======
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash

#=============
# Node 8.10
#=============
USER root
RUN apt-get update && apt-get install nodejs npm -y

#================
# ECS-SERVICE 
#================
RUN npm install -g LoyaltyOne/ecs-service

#==============
# CFN_NAG
#==============
RUN /bin/bash -l -c "gem install cfn-nag"

#================
# Ruby
#================
RUN apt-get update && apt-get install ruby-full -y

#=============
# Hugo
#=============
RUN apt-get update && apt-get install hugo -y

#=============
# install newman
#=============
RUN npm install -g newman
RUN npm install -g newman-reporter-htmlextra
#=============
# Cypress dependencies
#=============
RUN apt-get update && \
  apt-get install -y \
    libgtk2.0-0 \
    libnotify-dev \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libasound2 \
    xvfb

#===================

COPY assume-role /usr/local/bin/
RUN chmod +x /usr/local/bin/assume-role

RUN rm -rf /var/lib/apt/lists/* && apt-get clean
RUN rm $JENKINS_HOME/.profile
