FROM node:6
MAINTAINER jasonolmstead33

RUN echo $PATH

RUN echo "deb     http://httpredir.debian.org/debian jessie-updates main contrib" >> /etc/apt/sources.list
RUN echo "deb-src http://httpredir.debian.org/debian jessie-updates main contrib" >> /etc/apt/sources.list

RUN apt-get -qq update
RUN apt-get -qq -y install apt-transport-https

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get -qq update
RUN apt-get install -y zip
RUN apt-get install -y curl
RUN apt-get install -y grep
RUN apt-get install -y sed
run apt-get -y install yarn

RUN python --version
RUN apt-get -qq -y install python-dev
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py --user
RUN ~/.local/bin/pip --version
RUN ~/.local/bin/pip install awscli --upgrade --user
RUN ~/.local/bin/aws --version

ADD assume-role.sh /usr/local/bin/assume-role
RUN chmod +x /usr/local/bin/assume-role
RUN assume-role

RUN npm install -g standard
RUN npm install lodash
RUN npm install activedirectory
RUN npm install bluebird
RUN npm install body-parser
RUN npm install compression
RUN npm install express
RUN npm install -g gulp
RUN npm install -g serverless
RUN npm install https-proxy-agent
RUN npm install gulp-apidoc
RUN npm install is-my-json-valid
RUN npm install jwt-simple
RUN npm install newrelic
RUN npm install node-uuid
RUN npm install redis
RUN npm install request
RUN npm install request-promise
RUN npm install request-progress
RUN npm install chai
RUN npm install gulp-istanbul
RUN npm install gulp-mocha
RUN npm install gulp-nodemon
RUN npm install gulp-notify
RUN npm install gulp-plumber
RUN npm install gulp-sequence
RUN npm install gulp-shell
RUN npm install istanbul
RUN npm install mocha
RUN npm install mocha-bamboo-reporter
RUN npm install nock
RUN npm install node-ps
RUN npm install supertest
RUN npm install -g bower
RUN npm install node-cache
RUN npm install chai-things
RUN npm install vinyl-source-stream
