FROM ubuntu:16.04
MAINTAINER Viktor Dlouhy <viktor.dlouhy@dossier.no>

#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#################################################
# Inspired by
# https://github.com/cloudbees/java-build-tools-dockerfile/blob/master/Dockerfile
#################################################


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
# Miscellaneous packages
# iproute which is surprisingly not available in ubuntu:15.04 but is available in ubuntu:latest
# tree is convenient for troubleshooting builds
#========================
RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    iproute \
    openssh-client ssh-askpass\
    ca-certificates \
    tar zip unzip \
    wget curl \
    git \
    build-essential \
    less nano tree \
    jq \
    python python-pip groff \
    rlwrap \
  && rm -rf /var/lib/apt/lists/*

#========================
# Install Oracle JDK
#========================
RUN \
  add-apt-repository ppa:linuxuprising/java && \
  apt-get update && \
  echo oracle-java11-installer shared/accepted-oracle-license-v1-2 select true | debconf-set-selections && \
  apt-get install -y oracle-java11-installer && \
  apt install oracle-java11-set-default && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk11-installer

ENV JAVA_HOME /usr/lib/jvm/java-11-oracle

# workaround https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=775775
#RUN [ -f "/etc/ssl/certs/java/cacerts" ] || /var/lib/dpkg/info/ca-certificates-java.postinst configure

# install COMODO CA certificates
COPY jssecacerts /usr/lib/jvm/java-11-oracle/jre/lib/security

# workaround "You are using pip version 8.1.1, however version 9.0.1 is available."
RUN pip install --upgrade pip setuptools


#==========
# SET UTF8 Locale
#==========

RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    locales locales-all \
  && rm -rf /var/lib/apt/lists/*
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

#==========
# Psql Client
#==========

RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    postgresql-client \
  && rm -rf /var/lib/apt/lists/*

#====================================
# NODE JS
# See https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions
#====================================
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash \
    && apt-get install -y nodejs

#==========
# Maven
#==========
ENV MAVEN_VERSION 3.5.3

RUN curl -fsSL http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven


#==========
# Selenium
#==========

ENV SELENIUM_MAJOR_VERSION 3.11
ENV SELENIUM_VERSION 3.11.0
RUN  mkdir -p /opt/selenium \
  && wget --no-verbose http://selenium-release.storage.googleapis.com/$SELENIUM_MAJOR_VERSION/selenium-server-standalone-$SELENIUM_VERSION.jar -O /opt/selenium/selenium-server-standalone.jar

RUN pip install -U selenium


#==========
# AWS Cli
#==========

RUN pip install -U awscli


#=========
# Chrome
#=========
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y \
	google-chrome-stable


#=============
# Chrome Driver
#=============
ARG CHROME_DRIVER_VERSION=2.20
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/bin/
RUN chmod ugo+rx /usr/bin/chromedriver


#====================================
# MAVEN SETTINGS
#====================================
COPY settings.xml /root/.m2/settings.xml


#====================================
# MAVEN DEFAULT DEPENDENCIES
#====================================
RUN wget -O /tmp/repository.zip https://s3-us-west-1.amazonaws.com/dossierus/repository.zip
RUN mkdir /root/.m2/repository
RUN unzip /tmp/repository.zip -d /root/.m2/repository/

EXPOSE 4444