FROM microsoft/dotnet:2.2-sdk AS base

RUN apt-get -qq update && apt-get -qqy --no-install-recommends install wget gnupg \
	git \
	unzip

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g npm@latest
RUN npm install -g aurelia-cli@latest
RUN npm install -g @angular/cli
RUN npm install -g cli-react
RUN npm install -g ember-cli
RUN npm install -g bower