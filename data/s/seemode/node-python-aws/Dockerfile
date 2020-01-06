FROM python:stretch
MAINTAINER Nikolai R Kristiansen <nikolaik@gmail.com>

# Install node prereqs, nodejs and yarn
# Ref: https://deb.nodesource.com/setup_10.x
# Ref: https://yarnpkg.com/en/docs/install
RUN \
	apt-get update && \
	apt-get install -yqq apt-transport-https 
RUN \
	echo "deb https://deb.nodesource.com/node_10.x stretch main" > /etc/apt/sources.list.d/nodesource.list && \
	wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
	echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
	wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
	curl -o /usr/local/bin/ecs-cli https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-linux-amd64-latest && \
	chmod +x /usr/local/bin/ecs-cli && \
	

	apt-get update && \
	apt-get install -yqq nodejs yarn && \
	pip install -U pip && pip install pipenv && \
	pip install awscli && \
	aws --version \
	npm i -g npm@^6 && \
	apt-get install -yqq jq && \
	rm -rf /var/lib/apt/lists/*
