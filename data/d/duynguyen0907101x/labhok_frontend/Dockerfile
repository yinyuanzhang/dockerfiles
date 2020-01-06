FROM ubuntu:16.04

RUN apt-get update && apt-get install -y apt-transport-https curl wget
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install -y nodejs && npm install -g yarn @angular/cli tslint typescript codelyzer

COPY package.json /cache/package.json
COPY package-lock.json /cache/package-lock.json

RUN yarn

RUN curl -o /usr/bin/framgia-ci https://raw.githubusercontent.com/framgia/ci-report-tool/master/dist/framgia-ci && chmod +x /usr/bin/framgia-ci
