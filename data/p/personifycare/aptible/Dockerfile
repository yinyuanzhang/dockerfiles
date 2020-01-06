FROM python:latest

MAINTAINER Ivan Peevski

RUN apt-get update \
 && apt-get install -y jq curl \
# Install npm
 && curl -sSL https://deb.nodesource.com/setup_10.x | bash - \
 && apt-get install -y npm \
# Install snyk
 && npm i -g snyk \
 && apt-get clean \
# Install aws-cli
 && pip install awscli \
# Install aptible-cli
 && curl -o aptible-cli.deb "https://omnibus-aptible-toolbelt.s3.amazonaws.com/aptible/omnibus-aptible-toolbelt/master/176/pkg/aptible-toolbelt_0.16.1%2B20180730142012%7Edebian.8.10-1_amd64.deb" \
 && dpkg -i aptible-cli.deb

