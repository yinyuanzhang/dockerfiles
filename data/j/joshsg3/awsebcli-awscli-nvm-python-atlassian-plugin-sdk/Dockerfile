FROM openjdk:8-jdk

MAINTAINER Joshua Galea <joshua.galea@gmail.com>

RUN apt-get update

RUN apt-get install -y python-pip zip jq apt-transport-https gnupg

RUN pip install --upgrade\
	pip \
	awsebcli \
	awscli \
	untangle

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

ADD http://sdkrepo.atlassian.com/deb-archive/atlassian-plugin-sdk_8.0.7_all.deb /amps.deb

RUN echo "deb http://sdkrepo.atlassian.com/debian/ stable contrib" >>/etc/apt/sources.list \
    && dpkg -i /amps.deb

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash
