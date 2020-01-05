FROM ubuntu:16.04

RUN apt-get update

#Install stuff with apt-get
RUN apt-get install --yes curl
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install --yes --no-install-recommends openssl build-essential jq nodejs && apt-get update

# Install latest stable version of SFDX from NPM
RUN npm install sfdx-cli@6.56.0 --global
RUN sfdx --version
RUN sfdx plugins --core

#Install jsforce
RUN npm install jsforce --global