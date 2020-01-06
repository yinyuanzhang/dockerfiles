# BASE IMAGE
FROM node:8-slim

# DEPENDENCIES
RUN apt-get update && \
	apt-get install -y python3 python3-pip python3-dev zip unzip && \
	pip3 install boto3==1.3.0 influxdb

# SonarQube Scanner
RUN curl --insecure -OL https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.2.0.1227-linux.zip && \
	unzip sonar-scanner-cli-3.2.0.1227-linux.zip -d /opt/ && \
	ln -s /opt/sonar-scanner-3.2.0.1227-linux/bin/sonar-scanner /usr/bin/sonar-scanner && \
	rm sonar-scanner-cli-3.2.0.1227-linux.zip

# AdonisJs, Newman, Instanbul
RUN npm i -g @adonisjs/cli && \
	npm i -g newman && \
	npm i -g istanbul
